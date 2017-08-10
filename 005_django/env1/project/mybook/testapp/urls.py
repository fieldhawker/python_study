from django.conf.urls import url
from testapp import views

urlpatterns = [
    # インデックス
    url(r'^$', views.index, name='index'),   # トップ
    url(r'^top/$', views.index, name='index'),   # トップ
]
