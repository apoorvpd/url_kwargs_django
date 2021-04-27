"""url_kwargs_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from wishlist.views import Login, Register, UserView, GiftView, LogoutView, SuccessView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name="register"),
    path('user/', UserView.as_view(), name="user"),
    path('gifts/', GiftView.as_view(), name="gifts"),
    url(r'^gifts/(?P<username>[a-zA-Z0-9]+)', GiftView.as_view(), name="gifts"),
    path('', Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/success/', SuccessView.as_view(), name="success"),
]