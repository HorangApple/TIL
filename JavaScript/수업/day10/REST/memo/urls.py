from django.urls import path,include
from . import views
urlpatterns=[
    path('memos/',views.apiMemo),
    path('memos/<int:memo_id>',views.deleteMemo)
]