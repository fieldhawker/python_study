from django.conf.urls import url
from cybozulive import views

urlpatterns = [
    # インデックス
    url(r'^$', views.postMessage, name='index'),       # トップ
    url(r'^top/$', views.postMessage, name='index'),   # トップ
    url(r'^index/$', views.index, name='index'), # トップ
]
