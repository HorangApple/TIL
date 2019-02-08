# ORM

변수, 리스트 딕셔너리까지 자료형은 개발되었지만 영구적인 저장수단이 되지 않기에 '파일'로 저장하는 것이 필수가 되었다. 텍스트 파일은 원하는 형식을 저장할 수 없기에 엑셀을 모방한 csv, json 등 여러가지 파일형식을 사용하게 되었다.

클래스(object)로 저장할 수 있다. 클래스로 사용하면 좋은 장점은 저장된 것을 조작할 수 있는 함수를 이용할 수 있다는 점이다. 그런 점에서 ORM(Object-Relational Mapping)이 강점을 발한다.



각 자료형으로 만들어보면 다음과 같다.

```python
# -*- coding: utf-8 -*- 
# articles
# id,title,content,author

# list / tuple
articles_tuple = [
    (1,'제목1','내용1','말미잘'),
    (2,'제목2','내용2','해삼')
]

# dict
articles_dict = [
    {"id":1,"title":"제목1","content":"내용1", "author":"말미잘"},
    {"id":1,"title":"제목2","content":"내용2", "author":"해삼"}
    
]

# object
class Article:
    def __init__(self,id,title,content,author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
    
    def update(self,id,title,content,author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
    
    def delete(self):
        del self
        
    def __str__(self):
        return "이 글은 {}가 쓴 글입니다.".format(self.author)
        
articles_obj = [
    Article(1,'제목1','내용1','말미잘'),
    Article(2,'제목2','내용2','해삼')
]

# tuple
print(articles_tuple[1][3])

# dict
print(articles_dict[1]['author'])
print(articles_dict[1].get('author'))

# obj

hesam = articles_obj[1]
hesam.update(3,'제목3','내용3','멍개')
print(hesam.author)

hesam.delete()
print(hesam.author)
print(hesam)
```

출력결과는 다음과 같다.

```bash
horangapple:~/workspace $ python orm.py
해삼
해삼
해삼
멍개
멍개
이 글은 멍개가 쓴 글입니다.
```

SQLAlchemy 설치는 bash에 다음과 같이 입력한다.

```bash
pip install flask-sqlalchemy
```

*app.py*

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3' # 어떤 DB를 사용할지 결정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 없으면 에러

db = SQLAlchemy(app)

@app.route('/')
def index():
    print(app.config)
    return "hello"
```

위와 같이 app.config을 사용하는데 이것의 내용이 어떤건지 확인하기 위해 출력해봤다.

```bash
<Config {'SERVER_NAME': None, 'JSON_SORT_KEYS': True, 'SESSION_COOKIE_SAMESITE': None, 'TRAP_HTTP_EXCEPTIONS': False, 'USE_X_SENDFILE': False, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SESSION_COOKIE_NAME': 'session', 'TESTING': False, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///blog.sqlite3', 'DEBUG': False, 'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'SQLALCHEMY_POOL_RECYCLE': None, 'SQLALCHEMY_ECHO': False, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': False, 'TRAP_BAD_REQUEST_ERRORS': None, 'SESSION_COOKIE_PATH': None, 'SQLALCHEMY_NATIVE_UNICODE': None, 'PROPAGATE_EXCEPTIONS': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'PREFERRED_URL_SCHEME': 'http', 'SQLALCHEMY_POOL_TIMEOUT': None, 'APPLICATION_ROOT': '/', 'JSONIFY_PRETTYPRINT_REGULAR': False, 'SQLALCHEMY_MAX_OVERFLOW': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'SQLALCHEMY_BINDS': None, 'ENV': 'production', 'MAX_COOKIE_SIZE': 4093, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'SECRET_KEY': None, 'EXPLAIN_TEMPLATE_LOADING': False, 'MAX_CONTENT_LENGTH': None, 'SQLALCHEMY_POOL_SIZE': None, 'SESSION_COOKIE_DOMAIN': None, 'TEMPLATES_AUTO_RELOAD': None, 'SQLALCHEMY_RECORD_QUERIES': None, 'SESSION_COOKIE_HTTPONLY': True, 'JSON_AS_ASCII': True, 'JSONIFY_MIMETYPE': 'application/json', 'SESSION_COOKIE_SECURE': False}>
```

flask ORM을 이용하면 다음과 같이 만들 수 있다.

*app.py*

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3' # 어떤 DB를 사용할지 결정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 없으면 에러

db = SQLAlchemy(app)

db.init_app(app) # app이 시작 될 때 db 추가

# 다음의 SQL과 같은 class를 만든다
"""
CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
"""
# DB 제작
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
    def __str__(self): # __repr__은 html에서 articles만 입력해도 모두 출력된다.
        return "제목 : {},내용 : {}".format(self.title,self.content)

db.create_all()

@app.route('/')
def index():
    articles = Article.query.all() # table에 qurey를 날려 모두 가지고 온다
    return render_template('index.html',articles=articles)
    
@app.route('/create')
def create():
    """DB에 입력받은 제목과 내용을 저장한다."""
    form_title = request.args.get('title')
    form_content = request.args.get('content')
    # db=sqlite3.connect('blog.sqlite3')
    # c=db.curcor()
    # c.execute(url) 과 같은 작업
    # ORM을 사용하여 새로운 Article 객체를 만들어 DB에 저장
    a = Article(title=form_title,content=form_content)
    db.session.add(a) # a 객체를 db에 넣을 준비함
    db.session.commit() # 수정 확정
    
    return redirect('/')
    
@app.route('/delete/<int:id>')
def delete(id):
    target = Article.query.get(id)
    db.session.delete(target)
    db.session.commit()
    return redirect('/')
    
@app.route('/edit/<int:id>')
def edit(id):
    target = Article.query.get(id)
    return render_template('edit.html',target=target)
    
@app.route('/update/<int:id>')
def update(id):
    form_title = request.args.get('title')
    form_content = request.args.get('content')
    target = Article.query.get(id)
    target.title = form_title
    target.content = form_content
    db.session.commit()
    return redirect('/')
```



*templates/index.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/create">
        제목 : <input type="text" name="title"/>
        내용 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    {% for a in articles %}
        <p>
            제목 : {{a.title}}, 내용 : {{a.content}}
            <a href="/delete/{{a.id}}">[삭제]</a>
            <a href="/edit/{{a.id}}">[수정]</a>
        </p>
    {% endfor %}
</body>
</html>
```



*templates/edit.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/update/{{target["id"]}}">
        제목 : <input type="text" name="title" value="{{ target["title"] }}"/>
        내용 : <input type="text" name="content" value="{{ target["content"] }}"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



