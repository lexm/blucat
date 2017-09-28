# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm, RegForm
from .models import User
from django.shortcuts import render, redirect
import bcrypt

def index(request):
    form1 = RegForm()
    form2 = LoginForm()
    context = {
        "title": "Testing",
        "form1": form1,
        "form2": form2,
    }
    return render(request, 'logreg/index.html', context)

def register(request):
    if request.method == "POST":
        post = request.POST
        form = RegForm(post)
        if form.is_valid():
            full_name = post.get('full_name')
            alias = post.get('alias')
            email = post.get('email')
            password = post.get('password')
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(full_name=full_name, alias=alias, email=email, hash=hash)
            request.session['id'] = user.id
            return render(request, "logreg/yeah.html")
        else:
            form2 = LoginForm
            context = {
                "title": "Testing",
                "form1": form,
                "form2": form2,
            }
            return render(request, 'logreg/index.html', context)
    else:
        redirect('/')

def login(request):
    if request.method == "POST":
        post = request.POST
        form = LoginForm(request.POST)
        if form.is_valid():
            login = post.get('email')
            passwd = post.get('password')
            user = User.objects.get(email=login)
            request.session['id'] = user.id
            return render(request, "logreg/yeah.html")
        else:
            form1 = RegForm()
            context = {
                "title": "Testing",
                "form1": form1,
                "form2": form,
            }
            return render(request, 'logreg/index.html', context)
    else:
        return redirect('/logreg')

def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return redirect('/logreg')
