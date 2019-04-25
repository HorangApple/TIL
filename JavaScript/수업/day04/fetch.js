const XHR = new XMLHttpRequest(); // class 인스턴스 생성시 new를 사용
const URL = "https://koreanjson.com/posts/1";

// 요청을 초기화
XHR.open("GET", URL);
// 요청을 보냄
XHR.send();
// 요청이 끝났을 때 함수 실행
XHR.addEventListener("load", event => {
  const rawData = event.target.response;
  const parsedData = JSON.parse(rawData); // JSON으로 변환
  console.log(parsedData.content);
});

// fetch는 promise로 구현되어 있다.
fetch(URL)
    .then((response)=>console.log(response.json()))
    .then((object) => {
        console.log(object)
    })