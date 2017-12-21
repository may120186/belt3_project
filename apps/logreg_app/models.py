# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from datetime import datetime
from datetime import date, datetime
from time import strptime
# from ..belt3_app.models import Wish

EMAIL_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

class UserManager(models.Manager):
    def registration_validation(self, data):
        errors = {}
        if len(data['name']) < 3:
            errors["name"] = "Name needs to be at least 3 characters"
        
        if len(data['username']) < 3:
            errors["username"] = "Username needs to be at least 3 characters"

        # if len(data['alias']) < 2:
        #     errors["alias"] = "Alias needs to be at least 2 characters"

        # if not re.match(EMAIL_REGEX, data['email']):
        #     errors["Invalid email"] = "Not a valid email address"

        if len(data['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters"
        
        if not data['password'] == data['confirm']:
            errors["password"] = "Passwords do not match"
        return errors

    def user_validation(self,data):
        errors = {}
        
        existing_user = User.objects.filter(username = data['username'])

        if len(existing_user) < 1:
            errors["username"] = "Username does not match our records"

        else:
            print existing_user
            print existing_user[0]
            print existing_user[0].password
            if data['password'] != existing_user[0].password:
                errors["password"] = "Password does not match our records for that username"
        return errors

class User(models.Model):
    name= models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    # alias = models.CharField(max_length = 255)
    # email_address = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    # dob = models.DateField(verbose_name=None)
    # message = models.CharField(max_length = 255)
    objects = UserManager()


