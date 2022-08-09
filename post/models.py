from atexit import register
from enum import unique
from pydoc import describe
from tokenize import group
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# misaka enable link binding on comments
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register= template.Library()

from group.models import Group,GroupMember

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    public= models.BooleanField(default=False)
    #group = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="posts",null=False, blank=False,on_delete=models.CASCADE)


    def __str__(self):
        return self.message
    
    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"username" : self.user.username,"group" : self.group,"pk": self.pk})
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ('user','message','group')
        
    

