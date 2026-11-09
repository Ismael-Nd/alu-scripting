#!/usr/bin/python3
"""Recursively collect the titles of a subreddit's hot articles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return hot article titles across all available pages, or None."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return None

        data = response.json()["data"]
        titles = list(map(lambda post: post["data"]["title"],
                          data["children"]))
        after = data.get("after")
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return None

    hot_list.extend(titles)

    if after is None:
        return hot_list if hot_list else None

    return recurse(subreddit, hot_list, after)
