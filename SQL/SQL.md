

# DB - 190128
데이터페이스는 체계화된 데이터의 모임이다.



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

본격적으로 DB를 만들기 위해서는 확장자가 `.sqlite3`인 파일을 만드는 것으로 시작하면 된다.

이후 테이블을 생성한다.

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

위와 같이 활용할 수 있다.



`LIKE`는 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

<img src = "images/image 005.png">

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