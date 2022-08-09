from atexit import register
from enum import unique
from pydoc import describe
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# misaka enable link binding on comments
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register= template.Library()


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, allow_unicode=True,unique=True)
    descriptions = models.TextField(blank=True, default='')
    descriptions_html =  models.TextField(editable=False,blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.descriptions_html = misaka.html(self.descriptions)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("group:detail", kwargs={"slug": self.slug,"pk":self.pk})
    

 
class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
     