from django.urls import path
from . import views
app_name='articles' # url별명에 대한 namespace 생성
urlpatterns = [
    path('',views.index,name='index'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('<int:id>/',views.detail,name='detail'),
    path('<int:id>/edit/',views.edit,name='edit'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('<int:id>/update/',views.update,name='update'),
    path('<int:id>/comment/',views.comment,name='comment')
]
# 1. /articles -> 모든 글을 보여주는 곳
# 2. /articles/1 -> 글 상세하게 보는 곳
# 3. /articles/new -> 새 글을 작성
# 4. /articles/create -> 새 글을 저장
# 5. /articles/1/edit -> 글을 편집
# 6. /articles/1/update -> 글을 수정
# 7. /articles/1/delete -> 글을 삭제
