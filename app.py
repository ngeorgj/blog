from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(40), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return 'Blog post ' + str(self.id)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('posts.html', posts=all_posts)


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        new = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new)
        db.session.commit()
        return redirect('/posts')

    elif request.method == 'GET':
        return render_template('newpost.html')


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect('/posts')

    elif request.method == 'GET':
        return render_template('edit.html', post=post)

    return redirect('/posts')


if __name__ == ('__main__'):
    app.run(debug=True)
