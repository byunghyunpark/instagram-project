import json

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from photo.models import Photo, PhotoComment
from photo.serializer import PhotoSerializer, CommentSerializer

User = get_user_model()


# 보통
class PhotoList(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 쉬움
class PhotoListMixinView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 짱쉬움
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentView(APIView):
    def get(self, request):
        comments = PhotoComment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = PhotoComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@csrf_exempt
def photo_add(request):
    data = request.POST
    files = request.FILES

    user_id = data['user_id']
    content = data['content']
    image = files['photo']

    author = User.objects.get(id=user_id)
    photo = Photo.objects.create(
        image=image,
        author=author,
        content=content,
    )
    return HttpResponse(
        json.dumps(photo.to_dict()),
        content_type='application/json'
    )


def photo_list(request):
    photos = Photo.objects.all()
    data = {
        'photos': [photo.to_dict() for photo in photos],
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )


@csrf_exempt
def comment_add(request, photo_pk):
    data = request.POST

    user_id = data['user_id']
    content = data['content']

    author = User.objects.get(id=user_id)
    photo = Photo.objects.get(id=photo_pk)

    photo_comment = PhotoComment.objects.create(
        photo=photo,
        author=author,
        content=content,
    )
    return HttpResponse(
        json.dumps(photo_comment.to_dict()),
        content_type='application/json'
    )