from flask import Flask
from db_orm import get_authors, get_posts

app = Flask(__name__)


@app.route('/posts')
def posts():
    return get_posts()

@app.route('/authors')
def authors():
    return get_authors()

app.run()