# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from .models import Wish
from ..logreg_app.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all(),
        'items': Wish.objects.filter(added_by=User.objects.get(id=request.session['id'])),
        'other_items': Wish.objects.exclude(added_by=User.objects.get(id=request.session['id']))
    }
    return render(request, 'belt3_app/index.html', context)


def new(request):
    return render(request, 'belt3_app/add_item.html')

def create(request):
    if request.method == 'POST':
        errors = Wish.objects.wish_validation(request.POST)
        if len (errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect("/wishes/new")
        else:
            user = User.objects.get(id=request.session['id'])
            item = Wish.objects.create(item= request.POST['item'], created_by= user)
            item.added_by.add(user)
            item.save()
            return redirect("/wishes")
    else:
        return redirect("/wishes")

def show(request, user_id):
    context = {
        'item': Wish.objects.get(id=user_id)
    }
    return render(request, 'belt3_app/index.html', context)


def addwish(request, item_id):
    user = User.objects.get(id=request.session['id'])
    item = Wish.objects.get(id=item_id)
    item.added_by.add(user)
    item.save()
    return redirect("/wishes")

def remove(request, item_id):
    user = User.objects.get(id=request.session['id'])
    item = Wish.objects.get(id=item_id)
    item.added_by.remove(user)
    item.save()
    return redirect("/wishes")

def delete(request, item_id):
    item = Wish.objects.get(id=item_id)
    item.delete()

    return redirect("/wishes")


def info(request, item_id):
    item = Wish.objects.get(id=item_id)
    context = {
        'item': item,
        'other_users': User.objects.exclude(created_wish__created_by=item.created_by)
    }
    return render(request, 'belt3_app/item_info.html', context)


# def del_remove(request, item_id):
#     user = User.objects.get(id=request.session['id'])
#     item = Wish.objects.get(id=item_id)

#     if created_by_item_id != logged_in_user_id:
#         item.added_by.remove(user)
#         item.save()
#         return redirect("/wishes")

#     else:
#         if created_by_item_id == logged_in_user_id:
#             item.added_by.delete(user)
#             item.save()
#             return redirect("/wishes")
                


