from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    """インデックス"""
    # return HttpResponse('インデックス')
    return render(request,
              'index.html',     # 使用するテンプレート
              {'index': ''})    # 引数
