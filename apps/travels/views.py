# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PlanForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'travels/yeah.html')

def add(request):
    if request.method != "POST":
        form = PlanForm()
        context = {
            "title": "Add Plan",
            "form": form,
            }
        return render(request, 'travels/add.html', context)
    else:
        post = request.POST
        form = PlanForm(post)
        if form.is_valid():
            dest = post.get('dest')
            descr = post.get('descr')
            start = post.get('start')
            end = post.get('end')
            print dest, descr, start, end
            context = {
                "title": "Yep",
            }
            return render(request, 'travels/yeah.html', context)
        else:
            context = {
                "title": "Add Plan",
                "form": form,
            }
            return render(request, 'travels/add.html', context)
