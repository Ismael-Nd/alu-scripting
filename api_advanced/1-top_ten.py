import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        params={"limit": 10},
        allow_redirects=False,
        timeout=10,
    )

    if response.status_code != 200:
        print("HTTP status code:", response.status_code)
        print(None)
        return

    posts = response.json()["data"]["children"]
    for post in posts[:10]:
        print(post["data"]["title"])