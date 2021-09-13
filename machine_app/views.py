from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from machine_app.models import Machine, Tool
from machine_app.form import AddMachineForm, AddToolForm


# Create your views here.
class AddMachineView(CreateView):
    # view to adding machine
    model = Machine
    form_class = AddMachineForm
    template_name = 'machine_templates/add_machine.html'
    success_url = reverse_lazy('list_machines')


class ListMachinesView(ListView):
    # view to show all machines in data base
    model = Machine
    context_object_name = 'machines'
    template_name = 'machine_templates/list_machines.html'


class DetailMachineView(DetailView):
    # view to show details of the machine
    model = Machine
    context_object_name = 'machine'
    template_name = 'machine_templates/detail_machine.html'


class DeleteMachineView(DeleteView):
    # view to confirm delete machine
    model = Machine
    template_name = 'machine_templates/delete_machine.html'
    success_url = reverse_lazy('list_machines')


class AddToolView(CreateView):
    # view to adding tool
    model = Tool
    form_class = AddToolForm
    template_name = 'machine_templates/add_tool.html'
    success_url = reverse_lazy('list_tools')


class ListToolsView(ListView):
    # view to show all tools in data base
    model = Tool
    context_object_name = 'tools'
    template_name = 'machine_templates/list_tools.html'


class DeleteToolView(DeleteView):
    # view to confirm delete tool
    model = Tool
    template_name = 'machine_templates/delete_tool.html'
    success_url = reverse_lazy('list_tools')
