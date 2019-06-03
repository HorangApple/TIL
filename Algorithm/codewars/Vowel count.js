/*
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
*/

function getCount(str) {
  var vowelsCount = 0;
  let list = ['a','e','o','u','i']
  let a = str.split("")
  a.forEach((input)=>{
    if (list.includes(input)) {
      vowelsCount++
    }
  })
  
  return vowelsCount;
}

console.log(getCount('abracadabra'))

/*
정규표현식 이용
function getCount(str) {
  return (str.match(/[aeiou]/ig)||[]).length;
}
*/