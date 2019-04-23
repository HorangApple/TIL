var _ = require("lodash");
var menus = ["짜장면", "짬뽕", "볶음밥"]; // Array 배열
var pick = _.sample(menus);
console.log(`${pick} 먹으러 가자`);
var object = {
  짜장면:
    "http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg",
  짬뽕:
    "https://png.pngtree.com/element_origin_min_pic/00/00/11/095823383855d7e.jpg",
  볶음밥:
    "http://food.chosun.com/site/data/img_dir/2012/08/08/2012080802054_0.jpg"
};
// document.write(`<img src=${object[pick]}>`);
console.log(`<img src=${object[pick]}>`);

const numbers = _.range(1, 46);
const picks = _.sampleSize(numbers, 6);
// document.write(`<p>오늘의 행운의 번호는 ${picks}</p>`);
console.log(`<p>오늘의 행운의 번호는 ${picks}</p>`);

const luckyNumber = [5,7,32,2,36,26]
function match(luckyNumber){
    const numbers = _.range(1, 46);
    const picks = _.sampleSize(numbers, 6);
    return _.intersection(luckyNumber,picks);
}

console.log(`${match(luckyNumber).length}개가 일치`);


function getMin(a, b) {
  if (a > b) {
    return b;
  }
  return a;
}

function getMinFromArray(numbers) {
  var min = Infinity;
  // TODO: 배열에서 최소값을 구하여 min에 할당
  for (num of numbers) {
    min = min>num ? min=num : min
  }
  return min
}
// document.write(`<p>가장 작은 수는 ${getMinFromArray(picks)}</p>`);

// var 함수단위 스코프
// let, const 블록단위 스코프
function tests() {
    if (false){
        var name = 'name'; // 변수;
        name = 'jason';
    } 
    console.log(name);
}
tests()
const gender = 'man';
gender = 'woman'
console.log(gender)