// POST를 통한 posts 생성
const URL = "https://jsonplaceholder.typicode.com/posts/";
const XHR = new XMLHttpRequest();

// 1. XHR.open()
XHR.open("POST", URL);

/*
GET으로 보낼 땐 Header에는 누가 보냈는지의 정보를 User-Agent에 담겨있고
body에 보낼 데이터가 저장되어있다.
*/
XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

// 2. XHR.send()
const data = {
  userId: 1,
  title: "제목",
  body: "내용"
};
XHR.send(JSON.stringify(data));

// 3. XHR.addEventListener()
// https://developer.mozilla.org/ko/docs/XMLHttpRequest/Using_XMLHttpRequest#Monitoring_progress
XHR.addEventListener("load", function(user) {
  console.log(user.target.response);
});
