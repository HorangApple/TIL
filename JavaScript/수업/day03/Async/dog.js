function sleep() {
  let start = Date.now();
  while (Date.now() < start + 5000) {}
  console.log("수업 종료");
}

function finish() {
  setTimeout(function() {
    console.log("수업 종료");
  }, 5000);
}

console.log("수업중");
finish();
console.log("집에 가라");

/*
JS의 non-blocking 특성을 가진 함수들은 순서대로 작동하지 않는다.
한 코드가 끝나기까지 기다리지 않는다. 
= 다른 코드가 먼저 실행되는 것을 막지 않는다.
이러한 함수는 콜스텍에 올라가며 완료가 되면 콜스텍에서 삭제된다.
이러한 함수는 끝나고 싶을 때 끝내기 위해 콜백함수로 사용된다.
*/
