from django.shortcuts import render
from django.views.generic import CreateView

from image_app.models import Image

from image_app.form import AddImageForm


# Create your views here.
class AddImageView(CreateView):
    model = Image
    form_class = AddImageForm
    template_name = 'image_templates/add_image.html'
    success_url = '/'
