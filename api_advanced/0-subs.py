#!/usr/bin/python3
"""Query Reddit for a subreddit's total subscriber count."""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers, or 0 if the request cannot be completed."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0 (by /u/KingCash/)"
    }
    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.exceptions.RequestException, ValueError):
        return 0
