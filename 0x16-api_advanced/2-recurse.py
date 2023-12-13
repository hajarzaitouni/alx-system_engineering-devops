#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit using recursive function
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ returns list of titles of hot articles """
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers={'User-Agent': 'hajarita'},
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        results = response.json().get('data').get('children')
        [hot_list.append(t.get('data').get('title')) for t in results]
        return hot_list
    else:
        return None
