"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# api url을 구분해준다
apis_patterns = [
    url(r'^photo/', include('photo.urls.apis')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apis_patterns)),
    url(r'member/', include('member.urls.urls', namespace='member')),
    url(r'', include('photo.urls.urls', namespace='photo')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
