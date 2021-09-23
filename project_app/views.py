from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from project_app.models import Project
from project_app.form import AddProjectForm


# Create your views here.
class AddProjectView(CreateView):
    # view to adding project
    model = Project
    form_class = AddProjectForm
    template_name = 'project_template/add_project.html'
    success_url = reverse_lazy('list_projects')

    def post(self, request, *args, **kwargs):
        response = super(AddProjectView, self).post(request)
        self.object.resolution = self.object.calculate_resolution()
        self.object.g_code = self.object.generate_g_code()
        self.object.save()
        return response


class ListProjectView(ListView):
    # view to show all projects in data base
    model = Project
    context_object_name = 'projects'
    template_name = 'project_template/list_projects.html'


class DeleteProjectView(DeleteView):
    # view to confirm delete project
    model = Project
    template_name = 'project_template/delete_project.html'
    success_url = reverse_lazy('list_projects')


class DetailProjectView(DetailView):
    # view to show details of the project
    model = Project
    context_object_name = 'project'
    template_name = 'project_template/detail_project.html'


class EditProjectView(UpdateView):
    model = Project
    form_class = AddProjectForm
    context_object_name = 'project'
    template_name = 'project_template/edit_project.html'
    success_url = reverse_lazy('list_projects')

    def post(self, request, *args, **kwargs):
        response = super(EditProjectView, self).post(request)
        self.object.resolution = self.object.calculate_resolution()
        self.object.g_code = self.object.generate_g_code()
        self.object.save()
        return response
