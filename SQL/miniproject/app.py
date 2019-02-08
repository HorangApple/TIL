from flask import Flask,render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)


if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route('/articles/')
def articles():
    """DB에 저장된 모든 글들을 보여준다"""
    # 1. DB에 접속하여
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "SELECT*FROM articles"
    c.execute(sql)
    # 2. 저장된 모든 글들을 가져온다.(fetchall())
    data = c.fetchall()
    # 3. index.html에 넣어서 보여준다.
    return render_template('articles.html',data=data)
    
@app.route('/articles/new/')
def new():
    dt = datetime.datetime.now()
    time = dt.strftime("%Y.%d.%m %H:%M:%S")
    return render_template('new.html',time=time)
    
@app.route('/articles/create/')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')
    created_at = request.args.get('created_at')
    
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "INSERT INTO articles (title,content,author,created_at) VALUES ('{}','{}','{}','{}')".format(title,content,author,created_at)
    c.execute(sql)
    db.commit()
    
    sql = "SELECT article_id FROM articles WHERE title='{}' AND author='{}'".format(title,author)
    c.execute(sql)
    article_id=c.fetchone()
    print(article_id)
    return redirect('/articles/{}'.format(article_id[0]))
    
@app.route('/articles/<int:article_id>')
def detail(article_id):
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE article_id = {}".format(article_id)
    c.execute(sql)
    data = c.fetchone()
    return render_template("detail.html",data=data)
    
@app.route('/articles/<int:article_id>/edit/')
def edit(article_id):
    dt = datetime.datetime.now()
    time = dt.strftime("%Y.%d.%m %H:%M:%S")
    
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE article_id = {}".format(article_id)
    c.execute(sql)
    data = c.fetchone()
    return render_template("edit.html",data=data,time=time)
    
@app.route('/articles/<int:article_id>/update')
def update(article_id):
    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')
    created_at = request.args.get('created_at')
    
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "UPDATE articles SET title='{}',content='{}',author='{}',created_at='{}' WHERE article_id = {}".format(title,content,author,created_at,article_id)
    c.execute(sql)
    db.commit()
    return redirect('/articles/{}'.format(article_id))
    
@app.route('/articles/<int:article_id>/delete')
def delete(article_id):
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "DELETE FROM articles WHERE article_id={}".format(article_id)
    c.execute(sql)
    db.commit()
    return redirect('/articles')