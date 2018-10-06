import os
import requests

from retrying import retry
header = {"User-agent": "PyConEs demo KGB"}

@retry()
def get_reddit_posts():
    response = requests.get(os.getenv('SUBREDDIT_URL'), headers=header)
    if 199 > response > 299:
        raise Exception("Reddit doesn't love us")
    return [x.get('data') for x in response.json().get('data').get('children')]
