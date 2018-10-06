import requests

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    requests.get('http://google.com')
    return req
