#!/usr/bin/python3
"""Uses Reddit API to get 10 hot posts."""

import requests


def top_ten(subreddit):
    """Fetches the titles of the top 10 hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data").get("children")
    top_ten_posts = "\n".join(post.get("data").get("title") for post in data)
    print(top_ten_posts)
