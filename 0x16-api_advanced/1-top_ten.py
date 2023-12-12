#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import json
import requests


def top_ten(subreddit):
    """ returns 10 hot posts titles listed for a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'hajarita'},
                            allow_redirects=False, params={'limit': 10})

    if response.status_code == 200:
        results = response.json().get('data').get('children')
        [print(t.get('data').get('title')) for t in results]
    else:
        print("None")
