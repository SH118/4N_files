from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required   # 함수형 뷰에서 로그인 검사
import json


# @login_required # 로그인 검사, 일단 당장에는 뷰 확인할 수 있게 주석처리함.
def post_create(request):
    if request.method == 'GET':
        # form = PostForm()
        # return render(request, 'post_create.html', {'form': form})
        return JsonResponse({"message":"게시글 작성 페이지"})

    elif request.method == 'POST':
        try:
            params = json.loads(request.body)
            title = params.get('title')
            content = params.get('content')

            form = PostForm(request.POST)
            if form.is_valid(): # 폼이 유효할 때
                post = form.save(commit=False)
                post.title = title
                post.content = content
                post.save()
                return JsonResponse({"return": "form is valid"})
            else:   # 폼이 유효하지 않을 때
                return JsonResponse({"return": "form is invalid"})
        except json.JSONDecodeError:
            return JsonResponse({'return': 'error'})
