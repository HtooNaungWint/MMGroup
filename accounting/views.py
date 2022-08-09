from django.shortcuts import render
from django.views.generic   import TemplateView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from . import form

# Create your views here.
class homePage(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = form.UserForm
    success_url = reverse_lazy('accounting:login')
    template_name = 'accounting/signup.html'
    #model = 

    