class InsurancePolicy() {}
function makeInsurable(o){
    o.addInsurancePolicy = function(p) {this.insurancePolicy = p;}
    o.getInsurancePolicy = function() {return this.insurancePolicy;}
    o.isInsured = function() {return !!this.insurancePolicy;}
}


makeInsurable(Car); // error

const car1 = new Car();
car1.addInsurancePolicy(new InsurancePolicy()); // error

// 되지만 모든 자동차에서 makeInsurable 호출 필요
const car1 = new Car();
makeInsurable(car1);
car1.addInsurancePolicy(new InsurancePolicy()); // works

// 보험 관련 메서드들은 모두 Car 클래스에 정의된 것처럼 동작
makeInsurable(Car.prototype);
const car1 =new Car();
car1.addInsurancePolicy(new InsurancePolicy()); // works

