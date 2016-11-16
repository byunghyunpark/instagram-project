from django.conf.urls import url

from photo import apis
from photo import views
from photo.views import PhotoDisplayView


urlpatterns = [
    url(r'^photo/$', apis.PhotoList.as_view(), name='photo_list'),
    url(r'^photo/add/$', views.PhotoAdd.as_view(), name='photo_add'),
]