from django.conf.urls import url

from photo.views import PhotoDisplayView
from .. import views

urlpatterns = [
    url(r'^photo/$', views.PhotoList.as_view(), name='photo_list'),
    url(r'^photo/add/$', views.PhotoAdd.as_view(), name='photo_add'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo_detail'),
]