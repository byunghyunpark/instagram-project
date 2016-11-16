from django.conf.urls import url

from photo.apis import PhotoViewSet
from .. import apis


photo_list = PhotoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
photo_detail = PhotoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^photo/$', photo_list, name='photo_list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', photo_detail, name='photo_detail'),
    url(r'^photo/add/$', photo_list, name='photo_add'),

]

# urlpatterns = [
#     url(r'^photo/add/$', apis.PhotoListMixinView.as_view(), name='photo_add'),
#     url(r'^photo/$', apis.PhotoListMixinView.as_view(), name='photo_list'),
#     url(r'^(P<photo_pk>[0-9]+)/comment/add/$', apis.comment_add, name='photo_add')
# ]