```javascript
const Koa = require('koa');
const app = new Koa();

// app.use는 미들웨어에 순서대로 저장한다.
// Koa에서 async, await를 지원한다.
app.use(async (ctx, next) => {
  console.log(1);
  await next();
  console.log('bye');
})

app.use((ctx,next) => {
  console.log(2);
  next();
})

app.use((ctx)=>{
  ctx.body = 'hello world';
});

app.listen(4000, ()=>{
  console.log('listening to port 4000');
})
```

```
const Koa = require('koa');
const Router = require('koa-router');

const app = new Koa();
const router = new Router();

router.get('/', (ctx)=>{
  ctx.body='홈';
});

router.get('/about/:name?', (ctx)=>{
  const {name} = ctx.params;
  ctx.body = name ? `${name}의 소개` : `소개`;
});

router.get('/posts', (ctx)=>{
  const {id} = ctx.query;
  ctx.body = id ? `포스트 #${id}` : '포스트 아이디가 없습니다.';
})

app.use(router.routes()).use(router.allowedMethods());

app.listen(4000, () => {
  console.log('listening to port 4000');
})
```