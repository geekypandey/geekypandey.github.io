# Task
# To automatically publish the article on dev.to
# Get all the articles: Check the names, and publish the ones that isn't published yet.
# Parsing the articles in _post
import os
import re
from pathlib import Path

import frontmatter
import requests

def get_articles_names():
    username = 'geekypandey'
    url = 'https://dev.to/api/articles/me/all'
    headers = {
        'api-key': os.environ.get('API_KEY')
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f'Could not fetch users articles Error code: {res.status_code}')
        exit(1)
    articles = res.json()
    articles = [article.get('title') for article in articles]
    return articles


if __name__ == '__main__':
    articles = get_articles_names()
    posts = Path('../_posts')
    dev_url = 'https://dev.to/api/articles'
    username = 'geekypandey'
    gist = f'https://gist.github.com/{username}'
    api_key = os.environ.get('API_KEY')
    headers = {
        'Content-Type': 'application/json',
        'api-key': api_key
    }

    all_done = True
    for post in posts.iterdir():
        if not post.is_file():
            continue
        p = frontmatter.load(post)
        title = p.get('title')
        if title not in articles:
            # post that article
            metadata = {
                'title': p.metadata.get('title'),
                'series': 'Competitive Programming',
                'published': True
            }
            p.metadata = metadata
            content = frontmatter.dumps(p)
            content = re.sub(r'(gist) (\w+)', rf'\1 {gist}/\2', content)
            article = {}
            article['article'] = {}
            article['article']['body_markdown'] = content
            res = requests.post(dev_url, json=article, headers=headers)
            if res.status_code == 201:
                print(f'{title} published successfully!')
            else:
                all_done = False
                print(f'{title} not published! Error: {res.status_code}')
    if not all_done:
        exit(1)
