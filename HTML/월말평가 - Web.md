# 월말평가 - Web
- 총 3문제 출제
- VS Code, 결과 확인을 위한 브라우저(크롬)까지만 실행 가능. Django 서버 실행을 위한 cmd 또는 git bash
  실행 불가능.

## 1. HTML/CSS
- HTML 파일 제공

- position, display, background-image 같은 속성들은 출제 안됨.

- 예시 결과를 보고 CSS를 직접 작성해서 HTML Tag에 적용하는 형식. (주로 텍스트를 꾸미는 형식, 수업시간 및
    프로젝트에서 자주 사용했던 속성들 위주로 출제)

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <!--클래스 정의는 . 찍고 작성하면 된다.-->
      <style>
          .salmon{
              color:darksalmon;
              font-size: 20px;
              font-style: italic;
              font-family: 'Times New Roman', Times, serif;
              font-weight: bold
          }
          p{
              color: deeppink;
          }
          body{
              background-color:gray;
          }
          h1{
              color:blue
          }
          h2{
              color: yellow
          }
          h3{
              color: purple
          }
          hr{
              height:1px; background-color: seagreen
          }
  
      </style>
  </head>
  <body>
      <h1>프로그래밍 교육</h1> <!--파란색-->
      <hr> <!--초록색-->
      <div id=python>
          <h2>파이썬</h2>
          <h3>Number type</h3> <!--보라색-->
          <p class="salmon">파이썬에서 숫자형은 아래와 같이 있다.</p>
          <!--리스트의 모든 요소들은 orange로 색을 바꾸세요-->
          <ol class="salmon">
              <li style="color: red">int</li> 
              <!--Cascading 적용, 대상을 명확하게 특정할수록 명시도가 높아지고 우선순위가 높아진다.-->
              <li>float</li>
              <li>complex</li>
              <li><s>str</s></li> <!--취소선은 <s> 태그-->
          </ol>
          <h3>Sequence</h3>
          <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
          <h3>시퀀스는 for문을 돌릴 수 있다!!</h3>
          <ol class="salmon">
              <li>str</li>
              <li>list</li>
              <li>tuple</li>
              <li>range</li>
          </ol>
      </div> 
      <hr>
      <div>
          <h2>웹</h2>
          <h3>기초</h3>
          <ul>
              <!-- css를 이용해 모양을 바꿀 수 있다.-->
              <li style="list-style-type:square">HTML</li>
              <li style="list-style-type:square">CSS</li>
          </ul>
      </div>
  </body>
  </html>
  ```

  만약 style만 따로 css 파일로 빼고 싶다면 `<link rel="stylesheet" href="style.css">` 를 이용하자

  

- tag 선택자, class 선택자, id 선택자만 사용해도 되도록 출제.

- class 선택자, id 선택자를 이용하여 작성한 CSS를 HTML Tag에 적용하는 방법 숙지 필요.

  ### 선택자 및 우선 순위 (월말평가에도 나옵니다 미리 공부하세요.)

  `#X`은 id를, `.X`는 클래스를 가리킴

  ```css
  /*후손셀렉터*/
  /*문서 구조에서 특정 요소의 자손(자식,손자, 이후에 후손까지)을 선택하는 선택자로 div에서 p를 선택하여 그 이하의 p까지 속성을 적용한다.*/
  div p{
      color: crimson;
  }
  /*자식셀렉터*/
  /*특정 요소의 직계 자식만(손자, 후손은 제외) 선택하는 선택자로 오직 p에만 적용되며 그 아래까진 적용되지 않는다.*/
  
  div > p{
      color: crimson;
  }
  ```

  `X Y`는 X의 하위에 있는 Y를 가리킴

  #### X > Y

  ```css
  div#container > ul{
  	border: 1px solid black;
  }
  ```

  일반 `X Y`와 `X > Y`의 차이점은 후자가 직계 자식만을 선택한다는 것입니다. 가령, 아래 마크업을 생각해 보세요.

  ```html
  <div id="container">
  	<ul>
          <li>List Item
          	<ul>
                  <li>Child</li>
              </ul>
          </li>
          <li>List Item</li>
          <li>List Item</li>
          <li>List Item</li>
      </ul>
  </div>
  ```

  `#container > ul `선택자는 `id`가 `container`인 `div`의 직계 자손인 `ul`만 대상으로 삼습니다. 예를 들어 첫 번째 `li`의 자식인 `ul`은 대상이 되지 않습니다.

  이런 이유로 자식 선택자를 이용해 성능을 향상할 수 있습니다. 사실, 자바스크립트를 기반으로 하는 CSS 선택자 엔진으로 작업할 때 추천합니다.

  <img src="C:/Users/JongMin/Documents/gitgit/TIL/HTML/images/image%20007.png"/>

  

  #### X:nth-child(n)

  ```css
  li:nth-child(2) {
      color:red;
  }
  ```

  여러 요소 중에서 특정 요소를 지목하는 방법이 없었던 시절이 기억나나요? 그 문제를 풀어줄 `nth-child` 가상 클래스가 있답니다! nth는 'n번째'를 가리키는 말입니다.

  `nth-child`는 변숫값을 정수(integer)로 받습니다. 0부터 시작하지는 않습니다. 두 번째 항목을 대상으로 하고 싶다면 `li:nth-child(2)`로 작성합니다.

  자식 요소의 변수 집합을 선택하는 데에도 이 방식을 활용할 수 있습니다. 가령, 항목의 4번째마다 선택하려면 `li:nth-child(4n)`로 작성하면 됩니다.

  #### X:nth-last-child(n)

  ```css
  li:nth-last-child(2) {
      color: red;
  }
  ```

  만약 `ul`에 항목이 엄청 많고, 여러분은 끝에서 세 번째 항목만 필요하다고 한다면 어떨까요? `li:nth-child(397)`로 작성하지 말고 `nth-last-child` 가상 클래스를 쓰면 됩니다.

  이 선택자는 16번과 거의 동일합니다. 다만 집합의 끝에서부터 출발하면서 동작한다는 게 다릅니다.

  #### X:nth-of-type(n)

  ```css
  ul:nth-of-type(3) {
      border: 1px solid black;
  }
  ```

  `child`를 선택하지 않고 요소의 `type`을 선택해야 하는 날이 있을 것입니다.

  순서를 정하지 않은 목록 5개가 있는 마크업을 상상해 보세요. 세 번째 `ul`에만 스타일을 지정하고 싶은데 그것을 지정할 유일한 `id`가 없다면, `nth-of-type(n)` 가상 클래스를 이용할 수 있습니다. 위의 코드에서 세 번째 `ul`에만 테두리 선이 둘려집니다.

  #### X:nth-last-of-type(n)

  ```css
  ul:nth-last-of-type(3) {
      border: 1px solid black;
  }
  ```

  일관성을 유지하도록 목록 선택자의 끝부터 출발해 지정한 요소를 대상으로 하는 `nth-last-of-type`을 사용할 수도 있습니다.

## 2. Bootstrap
- Grid System에 관한 문제를 출제.

- Responsive Grid를 위한 Breakpoint 관련 내용은 문제에서 주어짐.

- 공식문서를 반드시 볼 것. (최소한 Grid의 Offsetting columns까지, 세로 정렬은 출제 안됨.)

  ### 그리드 시스템

  https://www.vikingcodeschool.com/web-design-basics/designing-with-grid-systems

  bootstrap의 꽃은 Container이다. Container라는 박스를 활용하여 깔끔하게 배치를 도와준다.

  모던 그리드 시스템은 총 격자가 12개를 사용한다. 왜냐하면 약수가 많기 때문에 깔끔하게 떨어뜨리는게 용이하다.

  margin은 공간을 밀면서 확장하기 때문에 적당하지 않으면 줄이 넘어버린다.

  <img src = "images/image 006.png">

  그렇다고 해서 padding으로 줄어도 소용 없는 것이 border 내의 background가 색이 들어가 있기에 실질적으로 줄어들지 않은 것처럼 보인다.

  컨텐츠를 보여줄 화면의 크기는 pc화면 기준 1200px을 사용한다. 왜냐하면 모니터 보급률을 따르면 1280px 대가 많이 보급이 되었기 때문이다.

  Small(sm) : 540px / Medium(md) : 720px / Large(lg) : 992px / Extra large(xl) : 1200px

  좌우 전체를 다 채우고 싶다면 'container-fluid'로 바꿔서 사용한다.

  컨텐츠가 너무 많으면 반응형을 안쓰는 것이 낫다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <!--bootstrap file-->
      
  	<!--bootstrap end-->
      <title>Document</title>
  </head>
  <body>
      <div class="container">
          <div class="row">
              <div class="col-sm-3">
                  25%
              </div>
              <div class="col-sm-6">
                  50%
              </div>
              <div class="col-sm-3">
                  25%
              </div>
          </div>
      </div>
  </body>
  </html>
  ```



- 미리 작성된 HTML 파일 제공. (CDN을 통하여 Bootstrap도 추가되어 있음)
- 예시 결과를 보고 알맞는 클래스를 채워 넣는 형식.
- Bootstrap 사이트 접속 불가능.

## 3. Django
- Django 프로젝트 코드 제공. (runserver를 통한 서버 실행은 불가능)

- [R]ead(List, Detail), [D]elete(Delete) 중에 하나를 작성하는 문제 출제.

- 부분 점수를 위해서 최대한 많이 작성할 것.

- views.py 에 새로운 함수 작성하여 페이지 만드는 법, template(html) 파일 만드는 법 숙지 필요.

- Django Template Language의 기본적인 사용법, '반복문', '조건문', '템플릿 상속(extends)', '페이지 출력(render)' 숙지 필요.

  ### 기초적인 DTL 문법 (truncatewords와 같은 필터 메소드 제외)

  ```html
  {% load static %} 
  : base template에서 static 폴더에 있는 외부파일(css 등)을 부를 때 사용
  {% extends 'articles/base.html' %}
  : base template을 불러옴
  {% block body %}~{% endblock %}
  : base template 내에서는 block 지정, 그 외의 곳에서는 block 작성
  {% for i in 변수명 %}~{% endfor %}
  : for문과 동일
  {{ 변수명 }}
  ```

  views.py

  ```python
  from django.shortcuts import render,redirect
  from .models import Articles,Comment
  # Create your views here.
  # 1. /articles -> 모든 글을 보여주는 곳
  # 2. /articles/1 -> 글 상세하게 보는 곳
  # 3. /articles/new -> 새 글을 작성
  # 4. /articles/create -> 새 글을 저장
  # 5. /articles/1/edit -> 글을 편집
  # 6. /articles/1/update -> 글을 수정
  # 7. /articles/1/delete -> 글을 삭제
  
  def index(request):
      data=Articles.objects.all()
      print(data)
      return render(request,'articles/index.html',{'data':data})
      
  def new(request):
      return render(request,'articles/new.html')
      
  def create(request):
      title=request.GET.get('title')
      content=request.GET.get('content')
      data=Articles(title=title,content=content)
      data.save()
      return redirect('articles:detail',data.id)
  
  def detail(request,id):
      article=Articles.objects.filter(id=id).first()
      return render(request,'articles/detail.html',{'article':article})
      
  def update(request,id):
      title=request.GET.get('title')
      content=request.GET.get('content')
      data=Articles.objects.filter(id=id).first()
      data.title=title
      data.content=content
      data.save()
      return redirect('articles:index',data.id)
  
  def edit(request,id):
      data=Articles.objects.filter(id=id).first()
      return render(request,'articles/edit.html',{'id':data.id,'title':data.title,'content':data.content})
      
  def delete(request,id):
      data=Articles.objects.filter(id=id).first()
      data.delete()
      return redirect('articles:index')
      
  def comment(request,id):
      content=request.POST.get('content')
      comment=Comment(content=content,article_id=id)
      comment.save()
      return redirect('articles:detail',id)
  ```

  ### 