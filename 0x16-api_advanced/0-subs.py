#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers from reddit
    """
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    payload = {"User-agent": "Joey"}
    get_subreddit = requests.get(reddit_url,
                                 headers=payload, allow_redirects=False)
    if get_subreddit.status_code != 200:
        return (0)
    return get_subreddit.json().get('data').get('subscribers')
