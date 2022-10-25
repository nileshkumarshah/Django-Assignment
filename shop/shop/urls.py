"""shop URL Configuration

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
from sunglas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('about', views.about, name='about'),
    path('glas', views.glas, name='glas'),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('register', views.regis, name='reg'),
    path('login', views.login, name='log'),
    path('logout', views.logout, name='logout'),
    path('product', views.produ, name='product'),
    path('upload', views.Upload_Images, name='img'),
    path('deleted/<int:id>', views.Delete_Product, name='delete_pro'),
    path('update_product', views.Update_Product, name='updateproduct'),
    path('product/<int:id>', views.addtocart.as_view(), name='addca'),
    path('demo', views.demo, name='demo'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
