from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from photo.forms import PhotoAddForm
from photo.models import Photo, PhotoComment


class PhotoDisplayView(DetailView):
    """
    PhotoDetail에서 get요청이 온 경우, 이 뷰를 사용
    Photo인스턴스의 Detail View
    """
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhotoCommentForm()
        return context


class PhotoCommentForm(forms.Form):
    """
    PhotoComment 인스턴스를 만들기 위한 Form
    content만 받으며, is_valid를 통과후에 photo와 author필드를 채워줘야 한다
    """
    content = forms.CharField(widget=forms.Textarea)


class PhotoCommentFormView(SingleObjectMixin, FormView):
    template_name = 'photo/photo_detail.html'
    form_class = PhotoCommentForm
    model = Photo

    def form_valid(self, form):
        self.instance = self.get_object()
        content = form.cleaned_data['content']
        PhotoComment.objects.create(
            photo=self.instance,
            author=self.request.user,
            content=content
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo:photo_detail', kwargs={'pk': self.instance.pk})


class PhotoDetail(View):
    def get(self, request, *args, **kwargs):
        view = PhotoDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PhotoCommentFormView.as_view()
        return view(request, *args, **kwargs)


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

