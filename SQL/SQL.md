

# DB - 190128
데이터베이스는 체계화된 데이터의 모임이다.



### RDBMS 

RDBMS (관계형데이터베이스 관리 시스템)는 관계형 모델을 기반으로하는 데이터베이스 관리시스템이다.

MySQL, PostgreSQL 등 다양한 플랫폼이 있지만 이것들을 조작하는 언어는 SQL 하나이다.

SQLite는 모바일 어플리케이션에서 DB를 구축할 때 사용한다. 다음과 같은 특징을 가지고 있다.

1. 파일보다 더 빠르게 데이터를 접근할 수 있다.
2. 특정 패턴에 맞춰 데이터를 쉽게 추출 할 수 있다.
3. 자체적 권한 시스템을 가지고 있다.
4. 많은 사용자의 동시 접근에 자체 해결방법을 가지고 있다.



### 스키마

<img src = "images/image 002.png">

<img src = "images/image 003.png">

스키마(scheme)는 데이터베이스에서 자료의 구조, 표현방법, 관계, 제약 조건에 관련한 전반적인 명세 등을 정의한 구조를 의미한다.



## SQL

SQL(Structured Query Language)는 RDBMS의 데이터를 관리하기 위해 설계된 특수 목적 프로그램 언어이다. 참고로 python은 범용 프로그램 언어이다. 



```sqlite
horangapple:~/workspace $ sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .exit
```

`sqlite3`를 입력하면 SQLite가 작동되며 모든 sqlite 명령어는 '.' 으로 시작된다.



https://zzu.li/hellodb

```SQL
sqlite> .mode csv
sqlite> .import hellodb.csv hellodb
```

이는 csv 파일을 읽기위해 csv 모드로 변경하고 `hellodb.csv`를 불러들어와 테이블로 `hellodb`로 명명하겠다는 것이다.



```sqlite
sqlite> .databases
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main                                                                       
sqlite> SELECT*FROM hellodb;
1,"길동","홍",600,"충청도",010-2424-1232
```

`.databases`는 현재 내가 갖고 있는 DB를 나타낸다.



```sqlite
sqlite> .mode csv
sqlite> .import question.csv question
sqlite> SELECT*FROM question;
1,hogu,2019년 1월 28일 1시 52분
2,hogu,2019년 1월 28일 2시 19분
3,hogu,2019년 1월 28일 2시 23분
4,hogu,2019년 1월 28일 2시 27분
5,hogu,2019년 1월 28일 2시 28분
6,배고파,2019년 1월 28일 2시 36분
sqlite> SELECT content FROM question LIMIT 3;
hogu
hogu
hogu
```

`SELECT*FROM question;` 처럼 SQL언어는 세미콜론 (';')으로 끝내야하는 것이 규칙이다. 그리고 csv의 첫 줄은 무조건 header로 인식하기 때문에 첫 줄을 건너 뛰고 두 번째 줄부터 불러온다. 그렇기 때문에 csv에는 반드시 header가 존재해야한다.




```sqlite
sqlite> .tables
question  users 
```

`.tables`는 현재 열려있는 테이블의 목록을 볼 수 있는 명령어이다.



```sqlite
sqlite> .header on
sqlite> .mode column
sqlite> SELECT * FROM users LIMIT 3;
id          first_name  last_name   age         country       phone          balance   
----------  ----------  ----------  ----------  ------------  -------------  ----------
1           정호      유         40          전라북도  016-7280-2855  370       
2           경희      이         36          경상남도  011-9854-5133  5900      
3           정자      구         37          전라남도  011-4177-8170  310
```

보다 이쁘게 데이터를 보기 위해 `.header on`과 `.mode column`을 사용한다.



```sqlite
horangapple:~/workspace $ sqlite3 test.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .databases
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/test.sqlite3                       
sqlite> 
```

본격적으로 DB를 만들기 위해서는 확장자가 `.sqlite3`인 파일을 만드는 것으로 시작하면 된다. 이후 테이블을 생성한다.



```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates
```

`PRIMARY KEY`는 고유식별을 하는 요소이다. 실제 정보를 저장할 땐 여러 개의 테이블에 저장되는 것이다.

파일을 경제적으로 저장하기 위해 여러가지 자료형이 정의되어있고 동적으로 상황에 맞게 저장시켜준다.



```sqlite
sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT
);
```

테이블의 구조를 보고 싶다면 `.schema`를 이용해 구조를 보면 된다.



```sqlite
sqlite> .tables
classmates
sqlite> DROP TABLE classmates;
sqlite> .tables
sqlite> 
```

테이블 삭제는 `DROP TABLE`을 이용해 삭제시키면 된다.



*create_students.sqlite3*

```sqlite
CREATE TABLE students(
    id INT,
    name TEXT,
    age INT,
    address TEXT,
);
```

```sqlite
horangapple:~/workspace $ sqlite3 test.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
classmates
sqlite> .read create_students.sqlite3 

sqlite> .tables
classmates  students  
sqlite> 
```

따로 확장자가 `.sqlite3` 파일을 만들어서 SQL 명령문을 입력해 저장해놓으면 `.read`를 통해 쉽게 테이블을 사용할 수 있다.



### 데이터 추가, 읽기, 수정, 삭제 (C,R,U,D)

데이터 추가, 읽기, 수정, 삭제 (C,R,U,D) 를 SQL을 사용하여 구현해보자.

1. 추가


```sqlite
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    address TEXT NOT NULL
);
```

`AUTOINCREMENT`는 자동으로 숫자를 증가 시키는 기능을 하며 이 기능을 사용할 때는 자료형을 정확히 정해줘야 한다.




```sqlite
sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동',34);
Error: NOT NULL constraint failed: classmates.address
```

`classmates` 를 선언할 때 `NOT NULL`을 선언했기 때문에 입력하지 않은 `address` 때문에 오류생겼다.



```sqlite
sqlite> INSERT INTO classmates (id, name, age, address) VALUES (1, '홍길동', 34, '서울');  
sqlite> SELECT * FROM classmates;
1|홍길동|34|서울
sqlite> INSERT INTO classmates (id, name, age, address) VALUES (1, '홍철수', 24, '서울');     
Error: UNIQUE constraint failed: classmates.id
sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍수', 25, '서울');         
sqlite> SELECT * FROM classmates;
1|홍길동|34|서울
2|홍수|25|서울
```

`AUTOINCREMENT` 이 선언되었을 때 순서에 맞게 `id` 값을 넣으면 오류가 발생하지 않지만 같은 값이나 그보다 낮은 값이면 `Error: UNIQUE constraint failed: classmates.id`와 같은 오류가 발생한다.



```sqlite
sqlite> ALTER TABLE bands
   ...> ADD COLUMN members INTEGER;
sqlite> .mode column                
sqlite> .header on
sqlite> SELECT * FROM bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973                  
2           Coldplay    1998                  
3           MCR         2001                  
```

column을 추가시킬 때는 `ALTER TABLE`을 사용한다.



2. 읽기

```sqlite
sqlite> SELECT * FROM classmates;
1|홍길동|34|서울
2|홍수|25|서울
3|박수|15|울산
4|박진수|85|부산
5|진수홍|45|부천
6|진홍|25|천안
sqlite> SELECT name, address FROM classmates LIMIT 3 OFFSET 1;                        
홍수|서울
박수|울산
박진수|부산
sqlite> SELECT name, address FROM classmates LIMIT 3 OFFSET 2;
박수|울산
박진수|부산
진수홍|부천
sqlite> SELECT name, address FROM classmates LIMIT 3 OFFSET 3;
박진수|부산
진수홍|부천
진홍|천안
```

`OFFSET`은 몇 번째 테이블 레이블부터 검색할지 정해준다. 



```sqlite
sqlite> SELECT * FROM classmates WHERE id=4;
4|박진수|85|부산
```

`WHERE`는 일종의 조건문으로 이를 이용해 특정 레이블을 선택할 수 있다.



3. 수정

```sqlite
sqlite> SELECT * FROM classmates;
1|홍길동|34|서울
2|홍수|25|서울
3|박수|15|울산
4|박진수|85|부산
6|진홍|25|천안
sqlite> UPDATE classmates SET address='부산' WHERE id=1;
sqlite> SELECT * FROM classmates;
1|홍길동|34|부산
2|홍수|25|서울
3|박수|15|울산
4|박진수|85|부산
6|진홍|25|천안
```

`UPDATE`와 `SET`, 그리고 `WHERE`를 이용해 column 값을 수정할 수 있다.



4. 삭제

```sqlite
sqlite> DELETE FROM classmates WHERE id=5;
sqlite> SELECT * FROM classmates;
1|홍길동|34|서울
2|홍수|25|서울
3|박수|15|울산
4|박진수|85|부산
6|진홍|25|천안
```

`DELETE FROM`과 함께 `WHERE`를 이용해서 레이블을 특정지어 지울 수 있다. 이름같이 중복되는 요소가 있다면 다 같이 지워지기 때문에 `PRIMARY KEY`인 `id`로 특정지어 삭제하는 것이 안전하다.

`AUTOINCREMENT`를 사용했다면 중간에 레이블이 지워지면 지워진 공간의 번호를 채우지 않고 최신 번호에 이어서 달게 된다. 만약에 중간에 채우는 식으로 작동되었다면 꼬이는 문제가 발생하게 된다.

### 기타

```sqlite
sqlite> SELECT COUNT(*) FROM users;                                                     1000
sqlite> SELECT MAX(age) FROM users;                                                     40
sqlite> SELECT MIN(age) FROM users;                                                     15
sqlite> SELECT SUM(age) FROM users;                                                     27346
sqlite> SELECT AVG(age) FROM users;                                                     27.346
```

위와 같이 산술을 도와주는 함수도 같이 사용할 수 있다. 

```sqlite
sqlite> SELECT first_name, age, MAX(balance) FROM users;                               "선영",37,990000
```

위와 같이 `balance`가 가장 큰 사람의 이름과 나이를 알아볼 수 있듯이 활용할 수 있다.



<img src = "images/image 005.png">

`LIKE`는 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

성능을 따진다면 숫자를 부등호로 비교해서 사용하는 것이 좋지만 글자를 검색해야하는 상황이라면 `LIKE`를 사용하는 것이 좋다.

DB에 대해 공부를 더하고 싶다면 https://www2.eecs.berkeley.edu/Courses/CS186/ 에서 배우자. 유튜브에 CS186 강의가 있다. 그리고 https://w3school.com/ 의 SQL 파트에서 공부할 수도 있다.



```sqlite
sqlite> SELECT * FROM users ORDER BY balance DESC LIMIT 10;                             
627,"선영","김",37,"전라북도",02-1610-2940,990000
124,"상현","나",30,"경상북도",010-4571-2869,99000
235,"정호","이",20,"전라북도",011-1193-3920,99000
259,"상철","이",17,"전라북도",011-3990-3978,99000
500,"지아","최",16,"전라북도",02-4150-9018,9900
768,"준서","박",17,"전라남도",010-9213-9802,9900
296,"미영","문",31,"전라남도",016-3620-8275,980000
327,"하윤","고",32,"제주특별자치도",02-7876-4073,980000
357,"은정","유",17,"강원도",016-8867-7897,980000
751,"서윤","안",29,"경상남도",011-2018-8263,980000
sqlite> SELECT * FROM users ORDER BY balance ASC LIMIT 10;                             
109,"명숙","이",17,"강원도",016-4860-7098,1000
138,"영수","김",40,"전라남도",016-9648-8312,1000
671,"건우","김",16,"제주특별자치도",010-7953-3308,1000
889,"현지","엄",22,"제주특별자치도",016-8784-8075,1000
180,"시우","허",28,"경기도",011-5404-8368,10000
215,"재호","권",19,"경기도",010-4943-4065,10000
670,"수빈","김",21,"제주특별자치도",010-4165-4448,10000
281,"현정","김",31,"전라북도",02-4837-5165,100000
534,"보람","김",33,"경상북도",010-5129-5704,100000
556,"지후","이",19,"경기도",011-4969-6922,100000
```

`ORDER BY` 는  특정 column을 기준으로 정렬을 해주며 `ASC`와 `DESC`로 오름차순, 내림차순으로 정렬해준다. 만약 정렬 대상이 숫자가 아닌 TEXT라면 앞의 두자리만 비교해서 정렬하기 때문에 의도하지 않은 결과가 나온다.



# Python과 함께 - 190129

*db.py*

```python
import sqlite3
# 1. > sqlite3 [데이터베이스 파일명]
# => 데이터베이스에 접속
# 2. SQL 쿼리 접속
# => SELECT*FROM user;
# => 결과를 가져다 줌
# 3. >.exit
# => 작업이 끝나면 콘솔 종료

# DB로써 다룰 수 있는 객체가 리턴됨, DB 접속
db = sqlite3.connect('test.sqlite3')

word = input("검색할 성(씨)을 입력해 주세요: ")

def search(keyword):
    """
    DB에서 검색어를 받아 검색을 해주는 친구
    """
    cur = db.cursor() # DB 조작을 할 수 있는 커서를 만든다.
    cur.execute("SELECT*FROM users WHERE last_name IS '{}'".format(keyword)) # SQL문 실행
    data = cur.fetchall() # 데이터의 구조 : [(),(),...], execute한 것을 한꺼번에 가지고 온다.
    cur.execute("SELECT COUNT(*) FROM users WHERE last_name == '{}'".format(keyword))
    total = cur.fetchone() # 데이터의 구조 : [()], execute한 것을 하나만 가지고 온다.
   
    # 1. 해당 검색 결과의 '수'를 출력하고,
    print("'{}'씨 성을 가진 사람은 {}명입니다.".format(keyword,total[0]),"명단은 다음과 같습니다.")
    # 2. 데이터들을 출력한다.
    for row in data :
        print(row)
    # => '박'씨 성을 가진 사람은 XX명입니다. 명단은 다음과 같습니다.
    # => (박,010)
    
search(word)
```

`fetchone`과 `fetchall`의 차이는 `execute`의 결과 값을 하나씩 가져오느냐 아니면 한꺼번에 들고오느냐다.

```bash
horangapple:~/workspace $ python3 db.py
검색할 성(씨)을 입력해 주세요: 김
'김'씨 성을 가진 사람은 268명입니다. 명단은 다음과 같습니다.
('8', '예진', '김', '33', '충청북도', '010-5123-9107', '3700')
('9', '서현', '김', '23', '제주특별자치도', '016-6839-1106', '43000')
('11', '서영', '김', '15', '제주특별자치도', '016-3046-9822', '640000')
('14', '영일', '김', '35', '전라남도', '011-4448-6198', '720')
('16', '옥자', '김', '19', '경상남도', '011-1038-5964', '720')
```

SQL문과 python 언어가 섞어쓰는 것에 문제가 있어 이를 python으로만 사용하기 위해 사람들은 많은 고민을 하였다.

*orm.py*

```python
# 1. csv, nested-list version
student1 = [
    ['id','name','phone','address'],
    [1, '강주','01011234552','서울'],
    [2, '김수','01011111222','부산']
]

# 2. Json, dictionary version - NOSQL
student2 = [
    {'id':1,'name':'강주','phone':'01011234552','address':'서울'},
    {'id':2,'name':'김수','phone':'01011111222','address':'부산'}
]

# 3. object version - ORM
class Student :
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = adresss

student3 = [
    Student(1,'강주','01011234552','서울'),
    Student(2,'김수','01011111222','부산')
]
```

ORM(Object-relational mapping)은 마치 OOP처럼 데이터베이스를 다루게 만들어준다. ORM과 flask를 같이 사용하면 다음과 같이 구현할 수 있다.

flask와 사용하기 때문에 SQLAlchemy를 이용해 작성한다.

*app.py*

```python
from flask import Flask, render_template, request
import csv
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # db 경로, / 4개는 절대경로, 3개는 상대경로, ///test.db이면 py파일이 있는 곳에 저장이 됨.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #최신 버전에서 발생하는 오류 방지

db = SQLAlchemy(app)

db.init_app(app)
# 테이블(스키마) 설계
class Quest(db.Model):
    __tablename = "questions"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    
db.create_all() # 위의 class Quest가 반영이 됨

@app.route("/") # 주문 받는 방법 (요청을 받는 방법)
def index():
    # DB에 저장된 모든 질문들을 불러온다.
    quests = Quest.query.all() # [<Quest 1>, <Quest 2>,...]로 존재
    # print(quests[0].content) # <Quest 1>의 내용 중 content 출력
    return render_template('index.html', quests=quests)

@app.route("/ask")
def ask():
    # 데이터베이스에 저장
    # PRIMARY KEY로 검색
    q=request.args.get('question')
    # INSERT INTO quetions (id, content) VALUES (1, 사용자의 값)
    
    # ORM을 통해 DB에 데이터를 저장하는 방법
    quest = Quest(content=q)
    db.session.add(quest)
    db.session.commit() # add는 여러 개지만 commit은 한 번만
    
    return redirect('/') # 다시 index 페이지로 돌아감, index.html로 직접 render를 할 수 있겠지만 디자인 패턴 상으로 redirect로 사용하는게 좋다.

@app.route("/delete/<int:id>") # id 값을 받으면 int로 형변환
def delete(id):
    # 특정 데이터 레코드를 지워준다.
    # DELETE FROM questions WHERE id == 1
    # id == 1인 객체가 q에 들어가 있음, Quest.query.filter_by(id=id).first()도 같은 말임.
    q = Quest.query.get(id) 
    db.session.delete(q)
    db.session.commit() # 마무리
    return redirect('/')

```



*index.html*

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
    <h1>익명 질문 앱</h1>
    <p>익명으로 질문하세요</p>
    <form action="/ask">
        <input type="text" name="question"/>
        <input type="submit" value="Submit"/>
    </form>
    <!--quests(리스트) 안에 담긴 모든 질문 객체들을 보여준다.-->
    {% for q in quests %}
        <p>{{ q.id }} : {{ q.content }} <a href="/delete/{{ q.id }}">[삭제]</a></p> 
    {% endfor %}
</body>
</html>
```

<img src = "images/image 006.png">

test.db 가 실제로 저장되는 DB인데 이를 보고 싶다면 SQLite Viewer이나 다음의 콘솔 명령어를 통해 깨지지 않고 볼 수 있다.

```bash
horangapple:~/workspace $ sqlite3 test.db
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
quest
sqlite> SELECT * FROM quest;
1|배고파
2|ㅇㅇ
```



# python과 함께 2 - 190207

*app.py*

```python
from flask import Flask,render_template, request, redirect
import sqlite3

app = Flask(__name__)
# db = sqlite3.connect('board.db') 여기서 선언하게 되면 thread 오류가 출력된다. main의 db와 def 안의 db는 서로 thread가 다르다. multitread를 지원하지 않는 sqlite이기 때문에 오류가 발생한다.

@app.route('/')
def index():
    """DB에 저장된 모든 글들을 보여준다"""
    # 1. DB에 접속하여
    db = sqlite3.connect('board.db') 
    c = db.cursor()
    sql = "SELECT*FROM articles"
    c.execute(sql)
    # 2. 저장된 모든 글들을 가져온다.(fetchall())
    data = c.fetchall()
    # 3. index.html에 넣어서 보여준다.
    return render_template('index.html',data=data)
    
@app.route('/create')
def create():
    """ index 페이지에서 보낸 정보를 받아, DB에 저장 """
    title=request.args.get('title') #유저가 요청을 보낸 정보를 담고 있음, {'title':'제목','content':'내용'}
    content=request.args.get('content')
    # sqlite3를 활용하여, 제목과 내용을 DB에 저장한다.
    # DB 접속, open()함수와 같은 역할, bash에서는 sqlite3
    # /// 3개는 상대경로를 의미
    db = sqlite3.connect('board.db') 
    # 1. 커서를 생성
    c = db.cursor()
    # 2. sql 실행
    sql = "INSERT INTO articles (title,content) VALUES ('{}', '{}')".format(title,content)
    c.execute(sql)
    # 3. commit
    # race condition를 막기위해 접속을 제한할 수 있다. 
    # 그것이 commit의 역할이고 commit을 통해 정확한 정보를 반영한다.
    db.commit()
    
    return redirect('/')

@app.route("/delete/<int:article_id>")
def delete(article_id):
    """ article_id에 저장된 id 값을 가진 레코드를 지운다. """
    db = sqlite3.connect('board.db') 
    c = db.cursor()
    sql = "DELETE FROM articles WHERE id = {}".format(article_id)
    c.execute(sql)
    db.commit() # db 수정이 가해지면 commit, 그렇지 않으면 fetchall/fetchone
    return redirect('/')
    
@app.route("/edit/<int:article_id>")
def edit(article_id):
    """ 글을 편집할 수 있는 페이지를 보여준다. """
    # 1. 편집하고자하는 글을 불러온다.
    # 2. form에 불러온 글을 넣는다.
    db = sqlite3.connect('board.db') 
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE id = {}".format(article_id)
    c.execute(sql)
    article = c.fetchone() # fetchall과 다르게 하나만 들고옴
    
    return render_template('edit.html',article=article)
    
@app.route("/update/<int:article_id>")
def update(article_id):
    """ edit 페이지에서 보낸 내용을 실제 DB에 적용한다. (수정) """
    title = request.args.get('title')
    content=request.args.get('content')
    
    db = sqlite3.connect('board.db') 
    c = db.cursor()
    sql = "UPDATE articles SET title = '{}', content = '{}' WHERE id = '{}'".format(title,content,article_id)
    c.execute(sql)
    db.commit()
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
    <title>게시판</title>
</head>
<body>
    <h1>게시판</h1>
    <form action="/create">
        제목 : <input type="text" name="title"/>
        내용 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    {% for d in data %}
        <p>
            제목 : {{ d[1] }}, 내용 : {{ d[2] }}
            <a href="/delete/{{ d[0] }}">[삭제]</a>
            <a href="/edit/{{ d[0] }}">[수정]</a>
        </p>
    {% endfor %}
</body>
</html>
```

<img src = "images/image 007.png">

*templates/edit.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>게시판</title>
</head>
<body>
    <h1>게시판</h1>
    <form action="/update/{{ article[0] }}">
        제목 : <input type="text" name="title" placeholder="{{ article[1] }}"/>
        내용 : <input type="text" name="content" value="{{ article[2] }}"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

<img src = "images/image 008.png">