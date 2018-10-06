import os
import requests

from retrying import retry
header = {"User-agent": "PyConEs demo KGB"}

@retry(stop_max_attempt_number=10)
def get_reddit_posts():
    response = requests.get(os.getenv('SUBREDDIT_URL'), headers=header)
    if 199 > response.status_code > 299:
        raise Exception("Reddit is a dick")
    return [x.get('data') for x in response.json().get('data').get('children')]
