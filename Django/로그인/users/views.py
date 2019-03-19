from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# '/users/' => 홈페이지
# '/users/login' => 로그인 화면

def home(request):
    return render(request,'users/home.html')

def login_user(request):
    # /users/login Post
    # -> 로그인(유저 검증)
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # 만약에 username, password 넘어온 값이 DB에 저장된 값과 같다면 유저정보 리턴
        # 아니면 None 리턴
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 1. 사용자가 로그인이 되었을 때
            messages.success(request, "성공적으로 로그인 되었습니다.")
            return redirect('home')
        else:
            # 2. 사용자가 로그인이 되지 않았을 때
            messages.success(request, "로그인이 되지 않았습니다. 다시 시도해 주세요.")
            return redirect('login')
    # /users/login GET
    # -> 로그인 창을 render
    else:
        return render(request,'users/login.html')
    return render(request, 'users/login.html')

def logout_user(request):
    # 유저를 로그아웃 시킨다.
    logout(request)
    # 유저에게 로그아웃이 되었다는 메세지를 전달한다.
    messages.success(request, "성공적으로 로그아웃 되었습니다.")
    return redirect('home')