# 1. MySQL 구조
<img src="./images/image 025.png"/>

데이터베이스: 연관된 표(table)를 Grouping 한 것, '스키마'라고도 한다.
데이터베이스 서버: 여러 데이터베이스를 Grouping 한 것

# 2. MySQL 장점
1) 권한 부여
2) 보안

# 3. 스키마 사용
```
DB생성: CREATE DATABASE [DB 이름];
DB삭제: DROP DATABASE [DB 이름];
DB리스트 출력: SHOW DATABASES;
사용할 DB 선택: USE [DB 이름];
암호 설정: SET PASSWORD = PASSWORD('[암호]');
테이블 리스트 출력: SHOW TABLES;
```

**예시**
```sql
CREATE TABLE topic(
  id INT(11) NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  description TEXT NULL,
  created DATETIME NOT NULL,
  author VARCHAR(15) NULL,
  profile VARCHAR(200) NULL,
  PRIMARY KEY(id)
);
```

# 4. CRUD
## 1) INSERT

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**예시**
```sql
INSERT INTO topic (title,description,created,author,profile) 
  VALUES('MySQL','MySQL is...',NOW(),'ane','developer');
```

## 2) SELECT

```sql
SELECT column1, column2, ...
FROM table_name;
```

**예시**
```sql
SELECT * FROM topic;
SELECT id,title,created,author FROM topic;
SELECT id,title,created,author FROM topic WHERE author='ane' ORDER BY id DESC LIMIT 2;
```

## 3) UPDATE

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**예시**
```sql
UPDATE topic SET description='Oracle is ...', title='Oracle' WHERE id=2;
```

## 4) DELETE

```sql
DELETE FROM table_name WHERE condition;
```

**예시**
```sql
DELETE FROM topic WHERE id = 5;
```

# 5. 관계형 데이터베이스 (RDB)
일반적인 데이터베이스를 운용하다보면 중복되는 데이터가 존재할 수 있다. 중복을 줄이고 보다 효율적인 데이터베이스를 만들기위해 테이블을 분산 저장하여 관계를 갖는 관계형 데이터베이스가 등장하였다.