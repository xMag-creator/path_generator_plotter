from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from image_app.models import Image
from image_app.form import AddImageForm


# Create your views here.
class AddImageView(CreateView):
    model = Image
    form_class = AddImageForm
    template_name = 'image_templates/add_image.html'
    success_url = '/'


class ListImageView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'image_templates/list_image.html'


class DeleteImageView(DeleteView):
    model = Image
    template_name = 'image_templates/delete_image.html'
    success_url = '/'


class DetailImageView(DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'image_templates/detail_image.html'
