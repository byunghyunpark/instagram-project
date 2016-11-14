from django.shortcuts import render
from django.views.generic import ListView

from photo.models import Photo


# def photo_list(request):
#     photos = Photo.objects.all()
#     context = {
#         'photos': photos,
#     }
#     return render(request, 'photo_list.html', context)


class PhotoList(ListView):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 3

