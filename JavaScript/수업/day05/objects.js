// JS에서만 가능하다
tongtong={
    name: 'tongtong',
    poop(){
        return "poop"
    }
}

console.log(tongtong.name)
console.log(tongtong.poop())

// class는 상속의 연속으로 이루어져 있고 그 본질은 object이다.
class Person {
    constructor(name){
        this.name = name
    }

    poop() {
        return "poop"
    }
    hello() {
        return `안녕 나는 ${this.name}야`
    }
}

const saja = new Person("사자")
console.log(saja.name)
console.log(saja.poop())
console.log(saja.hello())