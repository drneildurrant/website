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
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

FEED_URL = "https://neildurrant.substack.com/feed"
OUT = Path(__file__).resolve().parent.parent / "posts.json"
MAX_POSTS = 4          # store a few; the page shows the top 3
EXCERPT_WORDS = 28

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


def main() -> int:
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": "neildurrant.com/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml = resp.read()

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
