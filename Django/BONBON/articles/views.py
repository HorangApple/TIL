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
    print(data)
    data.delete()
    return redirect('articles:index')
    
def comment(request,id):
    content=request.POST.get('content')
    comment=Comment(content=content,article_id=id)
    comment.save()
    return redirect('articles:detail',id)