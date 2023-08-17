"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminpanel/', admin.site.urls),
    path('', index,name="index"),
    path('admin_login', admin_login,name="admin_login"),
    path('user_login', user_login,name="user_login"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_home', user_home, name="user_home"),

    path('recruiter_login', recruiter_login,name="recruiter_login"),
]+static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)
