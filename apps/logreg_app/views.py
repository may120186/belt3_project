# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'logreg_app/index.html')

def register(request):
    errors = User.objects.registration_validation(request.POST)
    if len(errors): #there are errors
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/login')
    else:
        person = User.objects.create(
        name = request.POST['name'],
        username = request.POST['username'],
        # alias = request.POST['alias'],
        password = request.POST['password'])
        # email_address = request.POST['email']
        request.session['name'] = request.POST['name']
        request.session['id'] = person.id
        return redirect ('/wishes')

def login(request):
    errors = User.objects.user_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/login')
    else:
        logged_in_user = User.objects.get(username=request.POST['username'])
        print logged_in_user
        request.session['name'] = logged_in_user.name
        request.session['id'] = logged_in_user.id
        return redirect ('/wishes')


def logout(request):
    request.session.clear()
    return redirect("/login")

