from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

class UserLogin(TemplateView):
    template_name = 'user/login.html'
    success_url = '/admin'

class UserSignIn(TemplateView):
    template_name = 'user/signup.html'
    success_url = '/admin'
