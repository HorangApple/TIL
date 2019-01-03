# git

<img src = "images/image 001.png">
git bash의 한글 출력 설정은 우클릭의 option에 들어가 위와같이 설정한다.

`git config --get user.name` : 사용하는 유저 이름 출력
`git config --get user.email` : 사용하는 유저 이메일 출력

## gitignore

<img src = "images/image 002.png">
git에서 특정 파일을 추적하고 싶지않다 싶으면 `.gitignore`를 만들어서 무시할 폴더, 파일을 작성하면 된다.
https://github.com/github/gitignore/blob/master/Python.gitignore 처럼 작업 환경에 맞춰 `.gitignore`를 설정하자

## github로 협업하는 법

<img src = "images/image 004.png">

회사 컴에서 `git push`를 하고 집에서 새로 이어서 작업한다면 `git clone`을 사용한다. 이후 작업해서 `git push`를 하고 회사 컴에서 반드시 작업전 `git pull`을 하여 동기화를 한다. 항상 github의 repository를 기준으로 맞춰야한다.

github를 팀으로 운영할 때는 수직적 구조로 운영해야한다. 즉, 팀장이 하라는 대로 해야한다. 그리고 동시에 파일을 수정하지 않는다는 가정하에 작업해야한다.

협업을 할 때 repository의  Setting-Collaborators에 팀원을 추가시킨 다음에 작업해야한다.

origin은 원격 repository의 별명이다. 

## Merge conflict

<img src = "images/image 005.png">

<img src = "images/image 003.png">

merge conflict가 발생시 해당 파일을 열고 선택하고 싶은 정보를 남기고 나머지는 지워서 저장한다. 

push 이후에는 수정할 수 없으므로 신중하게 해야한다.



## branch

`git branch ` : 모든 branch를 보여준다.

`git branch [브랜치 이름]` : 새 branch 생성

`git checkout [브랜치 이름]` : 해당 브랜치 간의 이동, 커밋 간의 이동

`git checkout -b [브랜치 이름]` : 해당 브랜치를 생성하고 전환

`git merge [브랜치 이름]` : 해당 브랜치를 현재 브랜치와 합병

`git branch -d [브랜치 이름]` : 해당 브런치 삭제, 대문자 D로 사용하면 강제 삭제



`git log [브랜치 이름 1]..[브랜치 이름 2]` : 

브랜치 간에 비교할 때

`git diff [브랜치 이름 1]..[브랜치 이름 2]` :

브랜치 간의 상태를 비교 할 때 

`git log --branches --graph --decorate --oneline` :

로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치 명을 표시하고, 한줄로 표시할 때 

## fast forward

<img src = "images/image 006.png">
<img src = "images/image 007.png">
<img src = "images/image 008.png">
<img src = "images/image 009.png">
<img src = "images/image 010.png">

fast forward로 merge가 되면 별도로 commit은 없으나 'recursive' strategy로 merge가 되면 별도의 merge commit이 생성이 된다.

git log --reverse를 통해 알 수 있는 commit id를 통해 git checkout 'commit id'를 하면 해당 commit의 파일 리스트를 볼 수 있다.

git commit --amend 를 하면 commit 을 수정 할 수 있다.

다른 지역 저장소에서 작업할 때 작업 시작전에 git pull을 맨 처음에 해서 원격저장소에 있는 내용을 동기화 시킨다.