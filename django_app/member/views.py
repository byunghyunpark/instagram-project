from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView


#
# def login_fbv(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('photo:photo_list')
#             else:
#                 return HttpResponse('ID or PW incorrect')
#     else:
#         form = LoginForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'member/login.html', context)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class LoginFormView(FormView):
    template_name = 'member/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return HttpResponse("Inactive user.")
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('photo:photo_list')



