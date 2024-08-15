#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    if word_count is None:
        word_count = {}

    sub_info = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": after},
        headers={"User-Agent": "redquery"},
        allow_redirects=False
    )

    if sub_info.status_code != 200:
        return None

    info = sub_info.json()
    hot_list = [child.get("data").get("title") for child in info.get("data").get("children")]

    if not hot_list:
        return None

    word_list = list(dict.fromkeys(word_list))

    if not word_count:
        word_count = {word: 0 for word in word_list}

    for title in hot_list:
        split_words = title.split()
        for word in word_list:
            for split_word in split_words:
                if split_word.lower() == word.lower():
                    word_count[word] += 1

    if info.get("data").get("after") is not None:
        return count_words(subreddit, word_list, word_count, info.get("data").get("after"))

    sorted_counts = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
    for k, v in sorted_counts:
        if v != 0:
            print(f'{k}: {v}')

    return None
