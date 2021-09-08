from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.views.generic.detail import SingleObjectMixin

from project_app.models import Project
from project_app.form import AddProjectForm


# Create your views here.
class AddProjectView(CreateView):
    model = Project
    form_class = AddProjectForm
    template_name = 'project_template/add_project.html'
    success_url = '/'


class ListProjectView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_template/list_projects.html'


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'project_template/delete_project.html'
    success_url = '/'


class DetailProjectView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project_template/detail_project.html'
