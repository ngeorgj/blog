from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'posts.db'
db = SQLAlchemy(app)


all_posts = [
    {
        'title': 'post 1',
        'content': 'This is the content of post 1, lalala',
        'author': 'Nivaldo',
    },
    {
        'title': 'post 2',
        'content': 'This is the content of post 2, lalala',
        'author': 'Nivaldo',
    },
    {
        'title': 'post 3',
        'content': 'This is the content of post 3, lalala',
        'author': 'Nivaldo',
    },
    {
        'title': 'post 4',
        'content': 'This is the content of post 4, lalala',
        'author': 'Nivaldo',
    }
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == ('__main__'):
    app.run(debug=True)
