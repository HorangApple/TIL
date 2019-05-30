/*
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
*/

function XO(str){
  str=str.toLowerCase()
  let sum = 0
  for ( k of str){
    if (k==="o"||k==="x") sum+=k.charCodeAt(0)
  }
  if (sum===0) return true;
  return (sum%231===0)?true:false;
}

console.log(XO('Oo'))

/*
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/match

function XO(str) {
  let x = str.match(/x/gi);
  let o = str.match(/o/gi);
  return (x && x.length) === (o && o.length);
}

정규표현식을 사용한다.
*/