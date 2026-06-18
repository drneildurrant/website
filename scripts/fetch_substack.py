#!/usr/bin/env python3
"""Refresh posts.json from the Substack RSS feed.

Pulls the latest posts from the "Provocations" feed and writes the newest few
to posts.json (same-origin file the home page fetches). Pure standard library
so the GitHub Action needs no pip install. Run: python3 scripts/fetch_substack.py
"""

import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

FEED_URL = "https://neildurrant.substack.com/feed"
OUT = Path(__file__).resolve().parent.parent / "posts.json"
MAX_POSTS = 4          # store a few; the page shows the top 3
EXCERPT_WORDS = 28

# Substack sits behind Cloudflare, which 403s requests that don't look like a
# real browser. Send a browser User-Agent and the headers a browser would.
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.5",
    "Accept-Language": "en-US,en;q=0.9",
}
RETRIES = 3            # transient 403/429/5xx happen; back off and retry

_TAGS = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")


def clean_excerpt(raw: str) -> str:
    text = html.unescape(_TAGS.sub(" ", raw or ""))
    text = _WS.sub(" ", text).strip()
    words = text.split(" ")
    if len(words) > EXCERPT_WORDS:
        text = " ".join(words[:EXCERPT_WORDS]).rstrip(".,;:— ") + "…"
    return text


def fmt_date(raw: str) -> str:
    try:
        dt = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return ""
    # e.g. "15 May 2026" — %-d is Linux/macOS; lstrip for portability.
    return dt.strftime("%d %b %Y").lstrip("0")


def fetch_feed() -> bytes:
    """Fetch the feed, retrying transient failures with exponential backoff."""
    req = urllib.request.Request(FEED_URL, headers=REQUEST_HEADERS)
    last_err: Exception | None = None
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except (urllib.error.HTTPError, urllib.error.URLError) as err:
            last_err = err
            if attempt < RETRIES - 1:
                wait = 2 ** attempt
                print(f"Feed fetch failed ({err}); retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)
    raise SystemExit(f"Could not fetch {FEED_URL}: {last_err}")


def main() -> int:
    xml = fetch_feed()

    root = ET.fromstring(xml)
    channel = root.find("channel")
    if channel is None:
        print("No <channel> in feed", file=sys.stderr)
        return 1

    posts = []
    for item in channel.findall("item")[:MAX_POSTS]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not title or not link:
            continue
        posts.append({
            "title": title,
            "url": link,
            "date": fmt_date(item.findtext("pubDate") or ""),
            "excerpt": clean_excerpt(item.findtext("description") or ""),
        })

    data = {
        "publication": (channel.findtext("title") or "Provocations").strip(),
        "url": "https://neildurrant.substack.com",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "posts": posts,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(posts)} posts to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
