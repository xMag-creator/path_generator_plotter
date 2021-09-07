"""path_generator_plotter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from image_app import views as image

urlpatterns = [
    path('admin/', admin.site.urls),

    path('list_images/', image.ListImageView.as_view(), name='list_images'),
    path('add_image/', image.AddImageView.as_view(), name='add_image'),
    path('detail_image/<int:pk>/', image.DetailImageView.as_view(), name='detail_image'),
    path('delete_image/<int:pk>/', image.DeleteImageView.as_view(), name='delete_image'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
