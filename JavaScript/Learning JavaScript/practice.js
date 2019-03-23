const x = 3;

function f() {
    console.log(x);  // 3
    console.log(y);  // 5, y는 정적 스코프에 해당
}

{
    y=5;
    f();
}