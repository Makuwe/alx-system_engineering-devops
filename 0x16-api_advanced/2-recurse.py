#!/usr/bin/python3
"""Uses Reddit API to get all hot posts."""

import requests


def recurse(subreddit, hot_list=None, after=""):
    """Recursively fetches hot posts from a given subreddit."""
    if hot_list is None:
        hot_list = []

    if after is None:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")

    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))

    return hot_list + recurse(subreddit, hot_list, r_json.get("data").get("after"))
