# OAuth 2.0

본 내용은 생활코딩의 [WEB2 - OAuth 2.0](https://opentutorials.org/module/3668)을 정리한 내용이다.


<img src="./images/image 001.png"/>

## 용어

- Resource Owner: 사용자

- Client: 홈페이지, front-end

- Resource Server: 서버, back-end 또는 서비스 제공자(firebase 등)

## 작동 순서

1) Resource Server에 Client를 등록하기위해 Client ID와 Client Secret, Authorized redirect URL (예: `https://client/callback`)을 넘긴다.

2) Resource Owner가 Client에 접속을 하면 Client는 Resource Server에 접속할 수 있는 주소 (예: `https://resource.server/?client_id=1&scope=B,C&redirect_uri=https://client/callback`)를 포함한 로그인 창을 제공한다.

3) Resource Owner가 Resource Server에 접속을 시도하면 Resource Server로부터 제공하는 서비스들(예: 기능 A,B,C,D) 중 사용할 기능(API)에 대한 권한(예: B,C)을 요청한다. 이 권한의 범위(예: B,C)를 Scope라 한다.

4) 권한 승인이 이루어지면 해당 유저에 대한 정보(User ID, Scope)를 Resource Server가 저장한다.

5) Resource Server에서 Authorization Code가 포함된 Authorized redirect URL (예: `https://client/callback?code=3`)을 Resource Owner에게 넘긴다.

6) Resource Owner는 넘겨받은 Redirect URL에 접속하여 Client에게 Authorization Code를 전달한다.

7) Client ID와 Client Secret, Authorization Code를 Resource Server에 전달하여 Authorization Code를 비교한다. (예: `https://resource.server/token?grant_type=authorization_code&code=3&redirect_uri=https://client/callback&client_id=1&client_secret=2`)

8) Authorization Code 확인이 완료되면 Client와 Resource Server 내에 저장된 Authorization Code를 삭제한다.

9) Resource Server로부터 Access Token을 Client에게 전달한다. 

## Access Token

- Access Token는 고유한 값이기 때문에 이를 통해 유저를 인식할 수 있다.
  
- Access Token를 통해 Resource Server에서 제공하는 개인 서비스(API)를 이용할 수 있다. 예를 들어 Google의 Firebase Auth를 통해 발급 받은 Access Token을 이용해 Google API (예: Google 캘린더 등)를 활용할 수 있다.
  
- Access Token의 LifeTime이 정해져있기 때문에 만료가 되면 다시 재발급을 받아야하는데 이 때 Refresh Token을 사용한다.
  
  <img src="./images/image 002.png"/>
  *출처 - RFC 6749*