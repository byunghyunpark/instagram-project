from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from django import forms
from rest_framework.response import Response
from rest_framework.views import APIView

from photo.models import Photo, PhotoComment
from photo.serializer import PhotoSerializer


# class PhotoList(APIView):
#     def get(self, request):
#         photos = Photo.objects.all()
#         serializer = PhotoSerializer(photos, many=True)
#         return Response(serializer.data)
from photo.task import photo_add_after


class PhotoList(ListView):
    model = Photo
    context_object_name = 'photos'
    queryset = Photo.objects.order_by('-created_date')
    paginate_by = 3


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list' )

    def form_valid(self, form):
        form.instance.author = self.request.user
        ret = super().form_valid(form)
        photo_add_after.delay(self.object)
        return ret


class PhotoDisplayView(DetailView):
    """
    PhotoDetail에서 get요청이 온 경우
    """
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhotoCommentForm()
        return context


class PhotoCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class PhotoCommentFormView(SingleObjectMixin, FormView):
    template_name = 'photo/photo_detail.html'
    form_class = PhotoCommentForm
    model = Photo

    def form_valid(self, form):
        self.object = self.get_object()
        content = form.cleaned_data['content']
        PhotoComment.objects.create(
            photo=self.object,
            author=self.request.user,
            content=content,
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDetail(View):

    def get(self, request, *args, **kwargs):
        view = PhotoDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PhotoCommentFormView.as_view()
        return view(request, *args, **kwargs)

