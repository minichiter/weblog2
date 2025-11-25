from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic import ListView
from .models import Post


class HomeViews(TemplateView):
    template_name = 'home.html'

class LoginViews(LoginView):
    template_name = 'login.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'