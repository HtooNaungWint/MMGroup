from gc import get_objects
from sqlite3 import IntegrityError
from django.views.generic   import TemplateView,CreateView,DeleteView,UpdateView,ListView,RedirectView
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib import messages 

from django.urls import reverse
from django.views.generic import (DetailView,TemplateView,
                                        CreateView,DeleteView,UpdateView)

from .models import Group,GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name','descriptions' )
    model = Group
     
class DetailGroup(LoginRequiredMixin,DetailView):
    model = Group

    

class ListGroup(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):
    print("hello there")
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:detail', kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try: 
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,('Warning already exists'))
        else:
            messages.success(self.request,('Welcome to the group '+group.name))
             
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:detail', kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        
        try: 
            MemberData = GroupMember.objects.filter(user = self.request.user, group__slug = self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,('You are not in the group'))
        else:
            MemberData.delete()
            messages.success(self.request,('Bye Bye '))
             
        return super().get(request, *args, **kwargs)