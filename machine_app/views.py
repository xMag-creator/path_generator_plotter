from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from machine_app.models import Machine, Tool
from machine_app.form import AddMachineForm, AddToolForm


# Create your views here.
class AddMachineView(CreateView):
    model = Machine
    form_class = AddMachineForm
    template_name = 'machine_templates/add_machine.html'
    success_url = '/'


class ListMachines(ListView):
    model = Machine
    context_object_name = 'machines'
    template_name = 'machine_templates/list_machines.html'


class DetailMachineView(DetailView):
    model = Machine
    context_object_name = 'machine'
    template_name = 'machine_templates/detail_machine.html'


class DeleteMachineView(DeleteView):
    model = Machine
    template_name = 'machine_templates/delete_machine.html'
    success_url = '/'


class AddToolView(CreateView):
    model = Tool
    form_class = AddToolForm
    template_name = 'machine_templates/add_tool.html'
    success_url = '/'


class ListToolsView(ListView):
    model = Tool
    context_object_name = 'tools'
    template_name = 'machine_templates/list_tools.html'


class DeleteToolView(DeleteView):
    model = Tool
    template_name = 'machine_templates/delete_tool.html'
    success_url = '/'
