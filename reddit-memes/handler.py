from reddit import get_reddit_posts

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    posts = get_reddit_posts()
    image_posts = [post for post in posts if post.get('url').endswith(('jpg', 'png', 'gif'))]
    txt = '<br/><ln/>'.join(f"<h3>{post.get('title')}</h3><br><img src={post.get('url')}>" for post in image_posts)
    return txt
