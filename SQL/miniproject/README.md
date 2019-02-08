# 190207 mini project

*app.py*

```python
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
```



*/templates/articles.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--- bootstrap 링크 --->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/layout.css')}}">
    <title>글 목록</title>
</head>
<body>
    <header class="font-nanum-Myeongjo">
        <h1>몽키매직 게시판</h1>
    </header>
    <p style="text-align: right;"><a class = "btn btn-primary" href="/articles/new/">새 글 등록</a></p>
    <div class = "font-nanum-Gothic list-group">
        {% for i in data %}
            <a class = "list-group-item list-group-item-action" href="/articles/{{ i[0] }}">{{ i[1] }}</a>
        {% endfor %}
    </div>
</body>
</html>
```





*app.py*

```python
...
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
...
```



*/templates/new.html*

```html
...
<body>
    <div>
        <header class="font-nanum-Myeongjo">
            <h1>새 글 생성</h1>
        </header>
    </div>
    <div class = "font-nanum-Gothic">
        <form action="/articles/create" method="get">
            <p class = 'mb-1'>제목</p>
            <p><input class="form-control" type="text" name="title"/></p>
            <p class = 'mb-1'>글쓴이</p>
            <p><input class="form-control" type="text" name="author"/></p>
            <p class = 'mb-1'>내용</p>
            <p><textarea class="form-control" rows="15" type="text" name="content"></textarea></p>
            <input type="hidden" name="created_at" value="{{time}}" />
            <p><input class="btn btn-primary my-1 float-right" type="submit" value="Submit"/></p>
        </form>
    </div>
</body>
</html>
```



*app.py*

```python
...
@app.route('/articles/<int:article_id>')
def detail(article_id):
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE article_id = {}".format(article_id)
    c.execute(sql)
    data = c.fetchone()
    return render_template("detail.html",data=data)
...
```



*/templates/detail.html*

```html
...
<body>
    <header class="font-nanum-Myeongjo">
        <h3>{{data[1]}}</h3>
    </header>
    <div class = "font-nanum-Gothic">
        <hr class = "my-1">
        <p class="d-flex justify-content-between"><span>{{data[4]}}</span><span>{{data[3]}}</span></p>
        <p style="white-space: pre-wrap">{{data[2]}}</p>
        <hr>
        <p class="float-right"><a class="btn btn-primary" href="/articles">목록</a> <a class="btn btn-primary" href="/articles/{{data[0]}}/edit">수정</a> <a class="btn btn-primary" href="/articles/{{data[0]}}/delete">삭제</a> </p>
    </div>
</body>
</html>
```



https://developer.mozilla.org/ko/docs/Web/CSS/white-space

`white-space`는 html의 `pre`태그와 비슷하게 공백을 생략하지 않고 나타내준다.



*app.py*

```python
...
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
...
```



*/templates/edit.html*

```html
...
<body>
    <div>
        <header class="font-nanum-Myeongjo">
            <h1 style="text-align:center">글 수정</h1>
        </header>
    </div>
    <div class = "font-nanum-Gothic">
        <form action="/articles/{{ data[0] }}/update",method="get">
            <p class = 'mb-1'>제목</p>
            <p><input class="form-control" type="text" name="title" value="{{data[1]}}"/></p>
            <p class = 'mb-1'>글쓴이</p>
            <p><input class="form-control" type="text" name="author" value="{{data[4]}}"/></p>
            <p class = 'mb-1'>내용</p>
            <p><textarea class="form-control" rows="6" type="text" name="content">{{data[2]}}</textarea></p>
            <input type="hidden" name="created_at" value="{{time}}" />
            <p><input class="btn btn-primary my-1 float-right" type="submit" value="Submit"/></p>
        </form>
    </div>
</body>
</html>
```



*app.py*

```python
...
@app.route('/articles/<int:article_id>/delete')
def delete(article_id):
    db = sqlite3.connect('blog.db') 
    c = db.cursor()
    sql = "DELETE FROM articles WHERE article_id={}".format(article_id)
    c.execute(sql)
    db.commit()
    return redirect('/articles')
```

