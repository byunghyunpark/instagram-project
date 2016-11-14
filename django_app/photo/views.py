from django.views.generic import ListView

from photo.models import Photo


class PhotoList(ListView):
    model = Photo
    context_object_name = 'photos'
