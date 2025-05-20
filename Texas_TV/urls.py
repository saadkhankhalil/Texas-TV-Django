"""
URL configuration for Texas_TV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from texas.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('admin_base/',admin_base,name='admin'),
    path('admin_base/add-about/', add_about_feature, name='add_about'),
    path('admin_base/view-about/', view_about_feature, name='view_about'),
    path('admin_base/update-about/<int:id>/', update_about_feature, name="update_about"),
    path('admin_base/delete-about/<int:id>/', delete_about_feature, name="delete_about"),
    path('admin_base/add-checkout/', swipe_images, name='add_checkout'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
