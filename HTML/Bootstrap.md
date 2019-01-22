## bootstrap

`bootstrap-4.2.1\dist\css\bootstrap.css`

이 파일을 편집할 html가 있는 폴더에 들고가서 link를 이용해 연결시킨다.

*bootstrap.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel='stylesheet' href="bootstrap.css">
</head>
<body>
    <h1>Bootstrap</h1>
</body>
</html>
```

그냥 이렇게 해도 h1태그에 css가 적용이 되는 것을 확인 할 수 있다. 

h1 margin의 기본 픽셀이 16px인데 bootstrap의 css는 0.5rem으로 설정되어있기에 달라지는 것을 확인할 수 있다.

```html
<button class="btn btn-primary">부트스트랩 버튼</button> 
```

위와 같이 색상이 들어간 버튼을 만들 수 있다. `warning`, `danger` 등으로 색을 지정할 수 있고 이외의 원하는 색상은 직접 작성하여 사용한다. 클래스를 여러개 사용할 때 띄어쓰기로 구분한다. 윗처럼 클래스 작성 순서가 아닌 클래스가 선언된 순서를 기준으로 작동한다. `bootstrap.css`를 보면 요소가 가장 많은 `btn`이 상위에 선언되어있고 `btn-primary`이 상대적으로 나중에 선언되어있다. 그리고 `btn-primary`이 선언된 내용이 `btn`에 있는 내용인데 오버라이딩 되어 겹치는 요소만 `btn-primary`의 요소로 변경된다. 나머지 겹치지 않은  `btn`의 요소는 그대로 적용이 된다.



## CDN (Content Delivery(Distribution) Network)

여러 노드에 가진 네트워크에 데이터를 제공하는 시스템으로 end-user의 가까운 서버를 통해 빠르게 전달 가능하고 외부 서버를 활용함으로써 본인 서버의 부하가 적어진다. CDN은 보통 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있다.



Bootstrap을 이용하면 간단하게 이쁜 페이지를 만들 수 있다.

html을 다 로드한 다음에 js를 로드하는 것이 성능이 좋다.

http://lorempixel.com/ 더미데이터를 넣고 싶다면 활용하자.

확장자 .min 파일은 들여쓰기, 띄여쓰기 등 컴퓨터가 알아 볼 정도로 축소시킨 파일이다.



`bootstrap-4.2.1\dist\css\bootstrap-reboot.css` 는 html의 쓸데없는 margin을 제거해준다.



## Utility

.m-0 : 클래스를 이용해 마진을 조절한다. m-0은 마진을 0으로 설정해준다.

.my-0, .mx-0 : 한 축에 대해 마진을 조절한다. 클래스 안에 있는 `!important`는 cascading을 무시하여 가장 우선순위로 설정하게 끔 해준다.

숫자의 의미 : 1-4 (16px x 0.25) / 2-8 (16px x 0.5) / 3-16 (16px x 1)/ 4-24 (16px x 1.5) / 5-48 (16px x 3)

.p-0 : padding을 조절한다.

.d-block, .d-none, .d-inline

d-sm-none : 반응형, 화면이 작아지면 그 태그가 보인다. sm을 lg로 바꾸면 sm보다 덜 바꿔도 태그가 생성된다. sm, lg, xl로 사이즈가 나눠져 있다.



머터리얼 디자인을 사용하고 싶다면 https://materializecss.com에 들어가서 적용하자



# Grid system

https://www.vikingcodeschool.com/web-design-basics/designing-with-grid-systems

bootstrap의 꽃은 Container이다. Container라는 박스를 활용하여 깔끔하게 배치를 도와준다.

모던 그리드 시스템은 총 격자가 12개를 사용한다. 왜냐하면 약수가 많기 때문에 깔끔하게 떨어뜨리는게 용이하다.

margin은 공간을 밀면서 확장하기 때문에 적당하지 않으면 줄이 넘어버린다.

<img src = "images/image 006.png">

그렇다고 해서 padding으로 줄어도 소용 없는 것이 border 내의 background가 색이 들어가 있기에 실질적으로 줄어들지 않은 것처럼 보인다.

컨텐츠를 보여줄 화면의 크기는 pc화면 기준 1200px을 사용한다. 왜냐하면 모니터 보급률을 따르면 1280px 대가 많이 보급이 되었기 때문이다.

좌우 전체를 다 채우고 싶다면 'container-fluid'로 바꿔서 사용한다.

컨텐츠가 너무 많으면 반응형을 안쓰는 것이 낫다.

https://flexboxfroggy.com/#ko