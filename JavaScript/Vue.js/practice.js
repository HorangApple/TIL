// 지역 컴포넌트 내용
let cmp = {
  template: '<div>{{message}}</div>',
  props:['propsData']
}

// 인스턴스도 컴포넌트이다.
new Vue({
  el: "#app",
  data:{
    "message":"data from Parent Component"
  },
  components:{
    'child-component': cmp
  }
});