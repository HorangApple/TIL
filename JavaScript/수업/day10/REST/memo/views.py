from django.shortcuts import render,get_object_or_404
from .serializers import MemoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Memo

# Create your views here.
@api_view(['GET', 'POST'])
def apiMemo (request):
    if request.method == 'GET':
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer=MemoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"작성되었습니다."})
    # elif request.method == 'DELETE':
    #     memo=get_object_or_404(Memo,pk=request.data['id'])
    #     memo.delete()
    #     return Response({"message":"삭제되었습니다."})

@api_view(['DELETE'])
def deleteMemo (request,memo_id):
    memo=get_object_or_404(Memo,pk=memo_id)
    memo.delete()
    return Response({"message":"삭제되었습니다."})