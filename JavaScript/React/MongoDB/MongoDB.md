# MongoDB
## 1. 관계형 데이터베이스(RDBMS)의 한계
### 1) 데이터 스키마가 고정적이다
> 만약 새로 등록하는 데이터 형식이 기존에 있던 데이터들과 다르다면 기존 데이터를 모두 수정해야 새 데이터를 등록할 수 있다. 이 때 양이 많다면 스키마를 변경하는 작업이 매우 번거로워진다.

### 2) 비싼 확장성
> RDBMS는 저장하고 처리해야 할 데이터양이 늘어나면 여러 컴퓨터에 분산시키는 것이 아닌 해당 DB 서버의 성능을 업그레이드하는 방식으로 확장해주어야 한다.

이러한 한계를 극복한 문서(document) 지향적 NoSQL DB인 MongoDB가 등장하게 되었다.

## 2. document
RDBMS의 record와 비슷한 개념으로 document의 데이터 구조는 한 개 이상의 key-value 쌍으로 되어 있다. 바이너리 형태의 JSON인 BSON를 사용하기 때문에 JSON 형태로 받은 데이터를 쉽게 DB에 등록할 수 있다.

`_id`는 document를 만들면 자동으로 생성되는 고유값이며 시간, 머신 아이디, 프로세스 아이디, 순차 번호로 되어 있다.

```json
{
  "_id": ObjectId("고유값"),
  "username": "hello1"
},
{
  "_id": ObjectId("고유값"),
  "username": "hello2",
  "phone": "010-1234-1233"
}
```

컬렉션은 여러 document가 들어 있는 곳이다. 기존과 다르게 다른 스키마를 가지고 있는 document들이 한 컬렉션에서 공존할 수 있다.

## 3. 스키마 디자인
기존 방식은 기능별로 여러 테이블을 만들어 필요에 따라 JOIN 해서 사용했지만 NoSQL에서는 모든 것을 document 하나에 넣는다.

문서 내부에 또 다른 문서들이 위치할 수 있는데, 이를 subdocument라고 한다. 이 또한 일반 문서를 다루는 것처럼 쿼리할 수 있다.

문서 하나에는 최대 16MB만큼 데이터를 넣을 수 있는데 초과할 여지가 있다면 컬렉션을 분리시키는 것이 좋다.

## 4. MongoDB 설치
윈도우에서는 공식 홈페이지에서 다운로드하여 설치한 후 환경변수-PATH에 MongoDB 설치 경로(예:`C:\Program Files\MongoDB\Server\4.0\bin`)를 입력한다.

이후 다음 명령어를 통해 DB 디렉터리를 임의로 설정하여 서버를 구동시킨다.

```bash
$ mongod -dbpath "경로"
```
## 5. mongoose 설치
Node.js 환경에서 사용하는 MongoDB 기반 ODM(Object Data Modelling) 라이브러리이며 DB 문서들을 JS 객체처럼 사용할 수 있게 한다.

```bash
$ yarn add mongoose dotenv
```
dotenv는 환경변수들을 파일에 넣고 사용할 수 있게 하는 개발 도구이다.