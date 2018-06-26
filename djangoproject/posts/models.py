# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.
#python manage.py makemigrations 'posts' to make the file.
#to make the table python manage.py migrate.
#after adding login button, register the model in admin.py
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body =  models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"
 
