# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg_app.models import User

class WishManager(models.Manager):
    def wish_validation(self, postData):
        errors = {}
        
        if len(postData['item']) < 3:
            errors['item'] = "Field cannot be left empty AND must be 3 or more characters"
        return errors



class Wish(models.Model):
    item = models.CharField(max_length = 255)
    added_by = models.ManyToManyField(User, related_name = "add_wish")
    created_by = models.ForeignKey(User, related_name = "created_wish")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = WishManager()
    def products(self):
        return self.added_by.exclude(id=self.created_by.id)
    
