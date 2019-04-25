/*
1급 객체란
1. 인자로 넘길 수 있어야 한다.
2. 변수나 데이터에 할당할 수 있어야 한다.
3. 객체의 리턴값으로 리턴할 수 있어야 한다.
*/

// 숫자로 된 배열을 받아서 모두 더한다.
const numbersAddEach = numbers => {
  let sum = 0;
  for (const number of numbers) {
    sum = sum + number;
  }
  return sum;
};

// 숫자로 된 배열을 받아서 모두 뺀다.
const numbersSubEach = numbers => {
  let sum = 0;
  for (const number of numbers) {
    sum -= number;
  }
  return sum;
};

// 순자로 된 배열을 받아서 모두 곱한다.
const numbersMulEach = numbers => {
  let sum = 0;
  for (const number of numbers) {
    sum *= number;
  }
  return sum;
};

const numbersEach = (numbers, callback) => {
  for (const number of numbers) {
    callback(number);
  }
};
let numbers = [4, 5, 6];
let sum = 0;
numbersEach([4, 5, 6], number => {
  sum += number;
});

console.log(sum);

numbers.forEach(number => {
  sum += number;
});

console.log(sum);

const orderCoffee = (order, serving) => {
    let coffee;
    // 커피를 만드는데 1초
  
    setTimeout(() => {
      coffee = order;
      serving(coffee, () => {});
    }, 1000);
    return coffee;
  };
  
  orderCoffee("Americano", console.log);