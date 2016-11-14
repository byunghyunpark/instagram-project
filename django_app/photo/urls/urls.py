from django.conf.urls import url, include
from .. import views

urlpatterns = [
    # url(r'^list/$', views.photo_list, name='photo_list'),
    url(r'^photo/$', views.PhotoList.as_view(), name='photo_list'),
    url(r'^photo/add/$', views.PhotoAdd.as_view(), name='photo_add'),
]