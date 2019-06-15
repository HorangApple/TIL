# chapter 03. SQL

## section 69. SQL - DDL

### 1. DDL(Data Definition Language)의 개념
> 스키마, 도메인, 테이블, 뷰, 인덱스를 정의하거나 변경 또는 제거할 때 사용하는 언어이다.
- DDL로 정의한 내용은 메타데이터(Metadata)가 되며, 시스템 카탈로그(System Catalog)에 저장한다.
- DDL의 유형으로 CREATE, ALTER, DROP이 있다.

### 2. CREATE SCHEMA (스키마 정의)
```
CREATE SCHEMA 스키마명 AUTHORIZATION 사용자_ID;
```

### 3. CREATE DOMAIN (도메인 정의)
```
CREATE DOMAIN 도메인명 데이터_타입
  [DEFAULT 기본값]
  [CONSTRAINT 제약조건명 CHECK (범위 값)];
```

### 4. CREATE TABLE (테이블 정의)
```
CREATE TABLE 테이블명
  (속성명 데이터_타입 [NOT NULL], ...
  [, PRIMARY KEY (기본키_속성명, ...)]
  [, UNIQUE (대체키_속성명, ...)]
  [, FOREIGN KEY (외래키_속성명, ...)
    REFERENCES 참조테이블 (기본키_속성명)]
    [ON DELETE 옵션]
    [ON UPDATE 옵션]
  [, CONSTRAINT 제약조건명] [CHECK (조건식)]);
```

### 5. CREATE VIEW (뷰 정의)
```
CREATE VIEW 뷰명[(속성명[, 속성명, ...])]
AS SELECT문;
```
- UNION이나 ORDER BY 절을 사용할 수 없다.

### 6. CREATE INDEX (인덱스 정의)
```
CREATE [UNIQUE] INDEX <인덱스명>
  ON 테이블명({속성명 [ASC|DESC] [, 속성명[ASC|DESC]]})
  [CLUSTER];
```

### 7. CREATE TRIGGER (트리거 정의)
```
CREATE TRIGGER 트리거명 [동작시기 옵션][동작 옵션] ON 테이블명
REFERENCING [NEW|OLD] TABLE AS 테이블명
FOR EACH ROW
WHEN 조건식
트리거 BODY
```
- 트리거 BODY는 BEGIN과 END 블록으로 이루어져 있다.

### 8. ALTER TABLE (테이블 수정)
```
ALTER TABLE 테이블명 ADD 속성명 데이터_타입 [DEFAULT '기본값'];
ALTER TABLE 테이블명 ALTER 속성명 [SET DEFAULT '기본값'];
ALTER TABLE 테이블명 DROP COLUMN 속성명 [CASCADE];
```

### 9. DROP (제거)
```
DROP SCHEMA 스키마명 [CASCADE|RESTRICT];
DROP DOMAIN 도메인명 [CASCADE|RESTRICT];
DROP TABLE 테이블명 [CASCADE|RESTRICT];
DROP VIEW 뷰명 [CASCADE|RESTRICT];
DROP INDEX 인덱스명 [CASCADE|RESTRICT];
DROP TRIGGER 트리거명 [CASCADE|RESTRICT];
DROP CONSTRAINT 제약조건명;
```

## section 70. SQL - SELECT
### 1. SELECT문의 일반 형식
```
SELECT [PREDICATE] [테이블명.]속성명[ AS 별칭][, [테이블명.]속성명, ...]
FROM 테이블명[, 테이블명, ...]
[WHERE 조건]
[GROUP BY 속성명[, 속성명, ...]]
[HAVING 조건]
[ORDER BY 속성명 [ASC|DESC][, 속성명 [ASC|DESC], ...]]
```
GROUP BY는 그룹 함수와 함께 사용된다.
**그룹 함수**
- COUNT(속성명): 그룹별 튜플 수를 구하는 함수
- MAX(속성명): 그룹별 최댓값를 구하는 함수
- MIN(속성명): 그룹별 최솟값를 구하는 함수
- SUM(속성명): 그룹별 합계를 구하는 함수
- AVG(속성명): 그룹별 평균를 구하는 함수

## section 71. SQL - JOIN
### 1. JOIN의 개념
> 2개의 테이블에 대해 연관된 튜플들을 결합하여, 하나의 새로운 릴레이션을 반환한다.

### 2. INNER JOIN
**EQUI JOIN**
> 대상 테이블에서 공통 속성을 기준으로 '='비교에 의해 같은 값을 가지는 행을 연결하여 결과를 생성한다.
```
// WHERE절 이용
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1, 테이블명2, ...
WHERE 테이블명1.속성명 = 테이블명2.속성명;

// NATURAL JOIN 이용
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 NATURAL JOIN 테이블명2;

// JOIN ~ USING절 이용
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 JOIN 테이블명2 USING(속성명);
```

**NON-EQUI JOIN**
> '='를 제외한 나머지 비교 연산자(>, <, <>, >=, <=)를 사용하여 결과를 생성한다.
```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1, 테이블명2, ...
WHERE (NON-EQUI JOIN 조건);
```

### 3. OUTER JOIN
> JOIN 조건에 만족하지 않는 튜플도 결과로 출력하기 위한 JOIN 방법

**LEFT OUTER JOIN**
> 일치하지 않는 좌측 항에 NULL 값이 들어가는 JOIN 연산

```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 LEFT OUTER JOIN 테이블명2
ON 테이블명1.속성명 = 테이블명2.속성명;

SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1, 테이블명2
WHERE 테이블명1.속성명 = 테이블명2.속성명(+);
```

**RIGHT OUTER JOIN**
> 일치하지 않는 우측 항에 NULL 값이 들어가는 JOIN 연산

```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 RIGHT OUTER JOIN 테이블명2
ON 테이블명1.속성명 = 테이블명2.속성명;

SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1, 테이블명2
WHERE 테이블명1.속성명(+) = 테이블명2.속성명;
```

**FULL OUTER JOIN**
> 일치하지 않는 모든 항에 NULL 값이 들어가는 JOIN 연산

```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 FULL OUTER JOIN 테이블명2
ON 테이블명1.속성명 = 테이블명2.속성명;
```

### 4. SELF JOIN
> 같은 테이블에서 2개의 속성을 연결하는 JOIN 연산

```
SELECT [별칭1.]속성명, [별칭2.]속성명, ...
FROM 테이블명1 [AS] 별칭1 RIGHT OUTER JOIN 테이블명2 [AS] 별칭2
ON 별칭1.속성명 = 별칭2.속성명;

SELECT [별칭1.]속성명, [별칭2.]속성명, ...
FROM 테이블명1 [AS] 별칭1, 테이블명2 [AS] 별칭2
WHERE 별칭1.속성명 = 별칭2.속성명;
```

## section 72. SQL - DML
### 1. DML(Data Manipulation Language)의 개념
> 응용프로그램이나 질의어를 통해 저장된 데이터를 실질적으로 관리하는데 사용되는 언어
- DB 사용자와 DBMS 간의 인터페이스를 제공
- INSERT, DELETE, UPDATE

### 2. INSERT (튜플 삽입)
```
INSERT INTO 테이블명[(속성명1, 속성명2, ...)]
VALUES (데이터1, 데이터2, ...)
```

- 대응하는 속성과 데이터는 개수와 데이터 타입이 일치해야한다.
- 테이블의 모든 속성을 삽입할 때는 속성명을 생략 가능하나 CREATE TABLE문에서 기술된 속성 순으로 속성 값들을 지정해야한다.

### 3. DELETE (튜플 삭제)
```
DELETE FROM 테이블명[ WHERE 조건];
```

### 4. UPDATE (튜플 수정)
```
UPDATE 테이블명
SET 속성명=데이터[, 속성명=데이터, ...]
WHERE 조건;
```
## section 73. SQL - DCL
### 1. DCL(Data Control Language)의 개념
> 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는 데 사용하는 언어
- DBA가 데이터 관리 목적으로 사용
- COMMIT, ROLLBACK, GRANT, REVOKE

### 2. COMMIT / ROLLBACK
**COMMIT**
> 트랜잭션의 모든 변경 내용들을 영구적으로 DB에 반영하는 명령어

**ROLLBACK**
> 변경된 모든 내용들을 취소하고 DB를 이전 상태로 되돌리는 명령어

### 3. GRANT / REVOKE
> DB 사용자에게 권한을 부여하고 취소하기 위한 명령어

**GRANT**
> 권한 부여를 위한 명령어

**REVOKE**
> 권한 취소를 위한 명령어

```
// 사용자등급 지정 및 해제
GRANT 사용자등급 TO 사용자_ID_리스트[IDENTIFIED BY 암호];
REVOKE 사용자등급 FROM 사용자_ID_리스트;

// 테이블 및 속성에 대한 권한 부여 및 취소
GRANT 권한_리스트 ON 개체 TO 사용자 [WITH GRANT OPTION];
REVOKE [GRANT OPTION FOR] 권한_리스트 ON 개체 FROM 사용자 [CASCADE];
```

- 권한_리스트 : ALL, SELECT, INSERT, DELETE, UPDATE, ALTER 등

## section 74. 뷰(VIEW)
### 1. 뷰(View)의 개념
> 하나 이상의 기본 테이블에서 유도되는 가상(Virtual) 테이블이다.

### 2. 뷰의 특징
- 기본 테이블과 조작이 유사하다.
- 가상 테이블이기 때문에 물리적으로 구현되어 있지 않다.
- 뷰를 통해서만 데이터에 접근함으로써 뷰에 나타나지 않는 데이터를 안전하게 보호할 수 있다.
- 기본 테이블의 기본키를 포함한 속성 집합으로 뷰를 구성해야만 삽입, 삭제, 갱신 연산이 가능하다.
- 정의된 뷰는 다른 뷰의 정의에 기초가 될 수 있다.

### 3. 뷰 연산 시의 제약성
- 뷰의 열이 테이블의 열(속성)이 아닌 상수, 계산식, 그룹 함수를 사용해 만들어 졌다면 그 뷰는 변경할 수 없다.
- DISTINCT, GROUP BY, HAVING을 사용해 만들어진 뷰는 변경할 수 없다.
- 둘 이상의 테이블에서 유도된 뷰는 변경할 수 없다.
- 변경하지 못하는 뷰를 토대로 하여 생성된 뷰는 변경할 수 없다.

### 4. CREATE VIEW (뷰 정의)
```
CREATE VIEW 뷰명[(속성명[, 속성명, ...])]
AS SELECT문
[WITH CHECK OPTION];
```

### 5. DROP VIEW (뷰 제거)
```
DROP VIEW 뷰명 {RESTRICT|CASCADE};
```

## selection 75. 내장 SQL
### 1. 내장(Embedded) SQL의 개념
> 호스트 프로그램 언어에 삽입한 SQL이다.

### 2. 내장 SQL의 특징
- 프로그램 어느 곳에서나 사용할 수 있다.
- 실행 결과가 여러 개의 튜플이어도 맨 처음의 튜플 하나만을 반환한다.
- 튜플에 일반 변수를 사용하여 저장할 수 있다.
- 컴파일할 때 선행 처리기에 의해 분리되어 컴파일된다.
- SQL 실행 상태는 SQL 상태 변수에 전달된다.

이후 생략

## selection 76. 스토어드 프로시저(Stored Procedure)
### 1. 스토어드 프로시저(Stored Procedure)의 개념
- 연속된 SQL문들을 하나로 모아 SQL 서버에 미리 컴파일해서 저장해 놓은 것을 말한다.
- 클라이언트로부터 호출문을 통해 복잡한 SQL의 일괄 작업을 수행하는데 적합하다.
- 선언부, 실행부, 예외처리부로 구성되어 있다.

### 2. 스토어드 프로시저의 장점
- 모듈별 프로그래밍 허용
- 빠른 SQL 실행 시간
- 보안성 향상
- 네트워크 통신량 감소

### 3. CREATE PROCEDURE (스토어드 프로시저 생성)
```
CREATE [OR REPLACE] PROCEDURE 프로시저명(파라미터)
[지역변수 선언]
프로시저 BODY;
```

### 4. DROP PROCEDURE (스토어드 프로시저 제거)
```
DROP PROCEDURE 프로시저명;
```

### 5. EXECUTE (스토어드 프로시저 실행)
```
EXECUTE 프로시저명;
EXEC 프로시저명;
```
