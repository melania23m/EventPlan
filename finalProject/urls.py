"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.urls import path, include
# from userextend.forms import AuthenticationLoginForm, PasswordChangeFormExtend, PasswordResetFormExtend
from userextend.forms import AuthenticationLoginForm, PasswordChangeFormExtend, PasswordResetFormExtend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('',include('todo_app.urls')),
    path('login/', LoginView.as_view(form_class=AuthenticationLoginForm), name='login'),
    path('password_change/', PasswordChangeView.as_view(form_class=PasswordChangeFormExtend), name='password_change'),
    path('password_reset/', PasswordResetView.as_view(form_class=PasswordResetFormExtend), name='password_reset'),
    path('', include('django.contrib.auth.urls')),
    path('', include('userextend.urls')),
    path('', include('providers.urls')),
    path('', include('event.urls')),

]
