from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from user_app.models import Resources
from django.views.generic import CreateView

from user_app.form import AddUserForm


# Create your views here.
class AddUserView(CreateView):
    model = User
    form_class = AddUserForm
    template_name = 'user_templates/add_user.html'
    success_url = reverse_lazy('list_projects')

    def post(self, request, *args, **kwargs):
        response = super(AddUserView, self).post(request)
        self.object.set_password(self.object.password)
        self.object.save()
        return response


class LoginUserView(LoginView):
    pass


class LogoutUserView(LogoutView):
    pass


class ChangeUserPasswordView(PasswordChangeView):
    pass
