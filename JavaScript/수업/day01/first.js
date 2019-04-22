// 한 줄 주석
/*
    여러 줄 주석
*/
console.log(document.write("<h1>임마!</h1>"));
// 경고창 출력
alert("야!");
// 입력창 출력
age = prompt("너 몇 살이야!");
if (age > 18) {
    // html에 작성
    console.log(document.write("<h1>너! 그럼 안돼!</h1>"));
} else {
    // 태그 요소를 가져옴
    console.log((document.querySelector("h1").innerText = "나이 만큼 맞자!"));
    for (let i = 0 ; i<age; i++) {
    setTimeout(()=>{console.log(document.write(`<h3>${i}대!</h3>`))},1000*i)
    }
}