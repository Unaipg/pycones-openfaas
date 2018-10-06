from reddit import get_reddit_posts
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    posts = get_reddit_posts()
    news_posts = (x for x in posts if something)

    return req
