#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit using recursive function
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ returns list of titles of hot articles """
    global after
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    params = {'after': after}

    response = requests.get(url, headers={'User-Agent': 'Hajar-Zait'},
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for p in posts:
            hot_list.append(p.get('data').get('title'))

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    return None
