#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""

from collections import Counter

import requests


def count_words(subreddit, word_list, after=None, counts=None, weights=None):
    """Print keyword counts in descending count and alphabetical order."""
    if weights is None:
        weights = Counter(word.lower() for word in word_list)
    if counts is None:
        counts = Counter()
    if not weights:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return

        data = response.json()["data"]
        for post in data["children"]:
            for word in post["data"]["title"].lower().split():
                if word in weights:
                    counts[word] += weights[word]
        after = data.get("after")
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return

    if after is not None:
        return count_words(subreddit, word_list, after, counts, weights)

    for word, count in sorted(counts.items(),
                              key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, count))
