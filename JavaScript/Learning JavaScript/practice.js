class Car{
    constructor(make,model){
        this.make = make;
        this.model = model;
        this.userGears = ['P','N','R','D'];
        this.userGear = this.userGears[0];
    }
    shift(gear){
        if(this.userGears.indexOf(gear) < 0)
            throw new Error(`Invalid gear: ${gear}`);
        this.userGear = gear;
    }
}

car1 = new Car('sam','xd')
car1.shift('N');
console.log(car1.userGear);
console.log(Car.prototype.userGear);
console.log(car1.userGears==Car.prototype.userGears);
car1.siva=()=>console.log('hi');
