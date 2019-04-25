// http://callbackhell.com/
// 작성하다보면 callback hell이 발생할 수 있다.
// 이에 대해 고안된 것이 promise

const sum = (a,b)=>{a+b}
// 다 만들면 커피를 줄게라는 약속을 함
// 중간에 무슨일이 생기면 알려줌

// resolve 에 성공시 넘겨줄 객체
// reject 에 무슨일이 생길시 발생시킬 에러를 담음
const orderCoffee = (order) => new Promise((resolve,reject) =>{
    let coffee;
    // 커피를 만드는데 1초
    setTimeout(() => {
        if (order===undefined) {
            reject('주문하세요')
        }
        coffee = order;
        resolve(coffee);
    }, 1000);
})

// orderCoffee('Americano') //Promise를 리턴
//     .then((coffee)=>{
//         console.log(`${coffee} 잘 마실게요!`) // Americano 잘 마실게요!
//     })
//     .then((test)=>{
//         console.log(`${test}`) // undefined
//     })
//     .then((coffee)=>{
//         orderCoffee(coffee)
//     })
    // .catch((error) => {
    //     console.log(error)
    // })

orderCoffee() //Promise를 리턴
    .then((coffee)=>{
        console.log(coffee)
        return orderCoffee() // Promise >> Latte
    })
    .then((coffee) => {
        console.log(coffee) // Latte
        // Promise >> undefined
    })
    .then((coffee) => {
        console.log(coffee) // undefined
    })
    .catch((error) => {
        console.log(error)
    })
