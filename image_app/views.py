from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from image_app.models import Image
from image_app.form import AddImageForm


# Create your views here.
class AddImageView(CreateView):
    # view to adding image
    model = Image
    form_class = AddImageForm
    template_name = 'image_templates/add_image.html'
    success_url = reverse_lazy('list_images')


class ListImageView(ListView):
    # view to show all images in data base
    model = Image
    context_object_name = 'images'
    template_name = 'image_templates/list_image.html'


class DeleteImageView(DeleteView):
    # view to confirm delete image
    model = Image
    template_name = 'image_templates/delete_image.html'
    success_url = reverse_lazy('list_images')


class DetailImageView(DetailView):
    # view to show details of the image
    model = Image
    context_object_name = 'image'
    template_name = 'image_templates/detail_image.html'
