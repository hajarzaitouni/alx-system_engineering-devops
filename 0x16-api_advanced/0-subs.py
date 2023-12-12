#!/usr/bin/python3
""" returns the number of subscribers """
import requests
import json


def number_of_subscribers(subreddit):
    """ returns total subscribers of a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'hajarita'},
                            allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
