from django.conf.urls import url

from .. import views

urlpatterns = [
    url(r'^list/$', views.PhotoList.as_view(), name='photo_list'),
    url(r'^add/$'
        , views.PhotoAdd.as_view(), name='photo_add'),
]