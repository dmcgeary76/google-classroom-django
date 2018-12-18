"""preports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pages.views import page_view, home_view, login_view, investigating_view
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', page_view),
    path('', home_view, name="Home"),
    path('home/', home_view, name="Home"),
    path('login/', login_view, name="Login"),
    path('Investigating/', investigating_view, name="Investigating")
]
