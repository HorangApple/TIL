# Django rest framework

<https://www.django-rest-framework.org/>

Modelform == Restframework



DRF 설치 및 설정

```bash
$ pip install djangorestframework
```

*api/settings.py*

```python
INSTALLED_APPS = [
    #...
    'rest_framework',
    #...
]
```

RESTful하게 아래와 같은 url로 만들 것이다.

```
GET(R): /music, /music/1

POST(C): /music

PUT, PATCH(U): /music/1

DELETE(D): /music/1
```


*music/models.py*

```python
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    content = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
```

*music/urls.py*

```python
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # api/v1/
    path('music/',views.music_list),
    path('music/<int:music_id>',views.music_detail)
]
```

Javascript에서의 JSON.parse() <-> JSON.stringify 관계를 갖고 있는데 Django에서는 Serializer를 통해 JSON 객체로 만들어서 보낸다.  별도의 `serializers.py`를 만들어야한다.

*serializers.py*

```python
from rest_framework import serializers
from .models import Music
'''
from django import forms
 class MusicForm(forms.ModelsForm)
   class Meta:
    model = Music
    fields = ['id','title','artist']
'''
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','title','artist']
```



*views.py*

```python
from django.shortcuts import render
from .models import Artist,Music,Comment
from .serializers import MusicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET']) # GET인 경우 이 함수를 사용한다.
def music_list(request):
    # 모든 음악들을 가져온다.
    music = Music.objects.all()
    serializer = MusicSerializer(music,many=True) # args: 무엇을 serialize?, 여러개인지 한개인지
    
    return Response(serializer.data) 
    # return render(request, 'list.html', {'musics':musics})
```

Django에서는 GET과 POST 밖에 사용을 못하기 때문에 DRF에 있는 view를 가지고 와서 사용해야한다.

