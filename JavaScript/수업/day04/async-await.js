// 브라우저 콘솔에서 실행
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

const getCoffee = async() => {
    try{
        const coffee = await orderCoffee() // Americano
        console.log(coffee) //Americano
    }
    catch(e){
        console.log(e)
    }
}

getCoffee()

const XHR = new XMLHttpRequest(); // class 인스턴스 생성시 new를 사용


const getData = async() => {
    const URL = "https://koreanjson.com/posts/1";
    const response = await fetch(URL);
    const data = await response.json()
    console.log(data)
}