const arr = [{id:5,name:"Suzanne"},{id:7,name:"Jim"}]
arr.find(o => o.id === 5); // 객체 {id:5,name:"Suzanne"}
arr.find(o => o.id === 2); // undefined