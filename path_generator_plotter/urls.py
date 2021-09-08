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
from machine_app import views as machine
from project_app import views as project

urlpatterns = [
    path('admin/', admin.site.urls),

    path('list_images/', image.ListImageView.as_view(), name='list_images'),
    path('add_image/', image.AddImageView.as_view(), name='add_image'),
    path('detail_image/<int:pk>/', image.DetailImageView.as_view(), name='detail_image'),
    path('delete_image/<int:pk>/', image.DeleteImageView.as_view(), name='delete_image'),

    path('list_machines', machine.ListMachinesView.as_view(), name='list_machines'),
    path('add_machine/', machine.AddMachineView.as_view(), name='add_machine'),
    path('detail_machine/<int:pk>/', machine.DetailMachineView.as_view(), name='detail_machine'),
    path('delete_machine/<int:pk>/', machine.DeleteMachineView.as_view(), name='delete_machine'),

    path('list_tools/', machine.ListToolsView.as_view(), name='list_tools'),
    path('add_tool/', machine.AddToolView.as_view(), name='add_tool'),
    path('delete_tool/<int:pk>/', machine.DeleteToolView.as_view(), name='delete_tool'),

    path('list_projects/', project.ListProjectView.as_view(), name='list_projects'),
    path('add_project/', project.AddProjectView.as_view(), name='add_project'),
    path('detail_project/<int:pk>/', project.DetailView.as_view(), name='detail_project'),
    path('delete_project/<int:pk>/', project.DeleteView.as_view(), name='delete_project'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
