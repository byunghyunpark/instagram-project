from django.conf.urls import url

from member.views import LoginFormView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]