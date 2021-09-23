from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from image_app.models import Image
from image_app.form import AddImageForm, EditImageForm


# Create your views here.
class AddImageView(CreateView):
    # view to adding image
    model = Image
    form_class = AddImageForm
    template_name = 'image_templates/add_image.html'
    success_url = reverse_lazy('list_images')

    def post(self, request, *args, **kwargs):
        response = super(AddImageView, self).post(request)
        image_size = self.object.read_image_size()
        self.object.width = image_size[0]
        self.object.height = image_size[1]
        self.object.save()
        return response


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


class EditImageView(UpdateView):
    model = Image
    form_class = EditImageForm
    context_object_name = 'image'
    template_name = 'image_templates/edit_image.html'
    success_url = reverse_lazy('list_images')
