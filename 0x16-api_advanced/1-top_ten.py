#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    returns the hot hot absolute hot top 10 redit posts
    """
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-agent": "Joey"}
    payload = {"limit": "10", "g": "GLOBAL"}
    get_subreddit = requests.get(reddit_url, params=payload,
                                 headers=header, allow_redirects=False)
    if get_subreddit.status_code != 200 or not get_subreddit:
        return print("None")
    result = get_subreddit.json().get('data').get('children')
    for content in result:
        print(content.get('data').get('title'))
