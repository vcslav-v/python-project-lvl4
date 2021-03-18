from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(auth_views.LoginView):
    next_page = reverse_lazy('main')
