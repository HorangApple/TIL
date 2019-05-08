# Firebase

유입->전환->재구매를 분석하는데 여러 도구가 있지만 그 중 firebase를 다뤄본다.



## Realtime database

<img src="images/image 001.png"/>

테스트 모드로 실행한다.

일정 사용량을 초과하면 과금이 부과된다.

<https://firebase.google.com/docs/web/setup?hl=ko>

```html
<script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
<script>
  // Initialize Firebase
  // TODO: Replace with your project's customized code snippet
  const config = {
    apiKey: "<API_KEY>",
    authDomain: "<PROJECT_ID>.firebaseapp.com",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    projectId: "<PROJECT_ID>",
    storageBucket: "<BUCKET>.appspot.com",
    messagingSenderId: "<SENDER_ID>",
  };
  firebase.initializeApp(config);
</script>
```

API, PROJECT_ID 등을 직접 설정하고 html에 삽입하여 firebase를 사용할 수 있게끔 한다.



<https://github.com/vuejs/vuefire>

<https://cdnjs.com/libraries/vuefire>

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/vuefire/1.4.5/vuefire.min.js"></script>
```

vue와 firebase를 연결시키기 위해 vuefire CDN도 같이 작성한다.



```html
    <script>
      // Initialize Firebase
      // TODO: Replace with your project's customized code snippet
      const config = {
        apiKey: "AIzaSyAOc4P0n6Jy87ZlF9-gamRQoZUyZvyLdeg",
        databaseURL: "https://dero-29540.firebaseio.com",
        projectId: "dero-29540"
      };

      firebase.initializeApp(config);
      const db = firebase.database();
      const app = new Vue({
        el: "#app",
        data: {
          newTodo: "",
        },
        methods: {
          addTodo: function(input) {
            // newTodo를 todos 추가
            // firebaseRefs는 firebase에서 해주는 것
            this.$firebaseRefs.todos.push(this.newTodo)
            this.newTodo = "";
          }
        },
        // vuefire가 담당, ORM도 vuefire쪽
        firebase: {
          todos: db.ref('todos')
        },
        computed:{
          current: function(){
            return this.todos
          }
        }
      });
    </script>
```

<img src="images/image 002.png">

<img src="images/image 003.png"/>

Realtime Database는 JSON 파일 형식으로 data를 보내준다.