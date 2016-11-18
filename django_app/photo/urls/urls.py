from django.conf.urls import url

from photo import apis
from photo import views
from photo.views import PhotoList, PhotoDisplayView

urlpatterns = [
    url(r'^photo/$', PhotoList.as_view(), name='photo_list'),
    url(r'^photo/add/$', views.PhotoAdd.as_view(), name='photo_add'),
    url(r'^photo/(?P<pk>[0-9]+)/$', PhotoDisplayView.as_view(), name='photo_detail'),
]