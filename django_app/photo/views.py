from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from photo.forms import PhotoAddForm
from photo.models import Photo, PhotoComment


# def photo_list(request):
#     photos = Photo.objects.all()
#     context = {
#         'photos': photos,
#     }
#     return render(request, 'photo_list.html', context)


class PhotoList(ListView):
    # queryset = Photo.objects.order_by('content')
    model = Photo
    context_object_name = 'photos'
    paginate_by = 3


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)

