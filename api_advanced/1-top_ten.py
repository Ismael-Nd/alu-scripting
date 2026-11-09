#!/usr/bin/python3
"""Print the titles of a subreddit's first ten hot posts."""

import requests


def top_ten(subreddit):
    """Print up to ten hot post titles, or None if the request fails."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "linux:alu-scripting:v1.0"},
            params={"limit": 10},
            allow_redirects=False,
            timeout=10,
        )
        if response.status_code != 200:
            print(None)
            return

        posts = response.json()["data"]["children"]
    except (requests.exceptions.RequestException, ValueError, KeyError):
        print(None)
        return

    for post in posts[:10]:
        print(post["data"]["title"])
