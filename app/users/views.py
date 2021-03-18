from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class CreateUser(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'


class UpdateUser(generic.UpdateView):
    model = User
    template_name = 'users/update.html'
