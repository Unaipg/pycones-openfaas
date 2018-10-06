from reddit import get_reddit_posts

def generate_html(posts):
    HTML = "<head><title>NOTICIAS</title></head><body>"
    for post in posts:
        HTML += f"""<a href="{post['url']}><h3>{post['title']}</h3></a><br>"""
    HTML += "</body>"
    return HTML

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    posts = [post for post in get_reddit_posts() if post['media'] is None]
    resulting_html = generate_html(posts)
    return resulting_html
