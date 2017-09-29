# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from .models import Plan
from .forms import PlanForm
from ..logreg.models import User
# Plan = apps.travels.get_model('Plan')
from django.shortcuts import render, redirect
from django.db.models import Q

def index(request):
    if not 'id' in request.session:
        return redirect('/main')
    user = User.objects.get(id=request.session['id'])
    trips = Plan.objects.filter(Q(planned_by=user) | Q(joined_by=user))
    print user, trips
    mytrips = []
    for trip in trips:
        print trip
        mytrip = {}
        mytrip['dest'] = trip.dest
        mytrip['start'] = trip.start
        mytrip['end'] = trip.end
        mytrip['descr'] = trip.descr
        mytrip['id'] = trip.id
        mytrips.append(mytrip)
    others = []
    notmytrips = Plan.objects.filter(~Q(planned_by=user) & ~Q(joined_by=user))
    for nother in notmytrips:
        other = {}
        other['dest'] = nother.dest
        other['start'] = nother.start
        other['end'] = nother.end
        other['descr'] = nother.descr
        other['id'] = nother.id
        others.append(other)
    context = {
        "title": "Travel Dashboard",
        "name": user.full_name,
        "trips": mytrips,
        "others": others,
    }
    return render(request, 'travels/index.html', context)

def add(request):
    if not 'id' in request.session:
        return redirect('/main')
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
            print post
            dest = post.get('dest')
            descr = post.get('descr')
            start = post.get('start')
            end = post.get('end')
            print dest, descr, start, end
            user = User.objects.get(id=request.session['id'])
            # Plan.objects.create(dest=dest,descr=descr,start=start,end=end,planned_by=user)
            return redirect('/travels')
        else:
            context = {
                "title": "Add Plan",
                "form": form,
            }
            return render(request, 'travels/add.html', context)

def trip(request, id):
    plan = Plan.objects.get(id=id)
    joiners = User.objects.filter(joined_trips=plan)
    context = {
        "plan": plan,
        "joiners": joiners,
    }
    return render(request, 'travels/trip.html', context)

def join(request, id):
    user = User.objects.get(id=request.session['id'])
    plan = Plan.objects.get(id=id)
    plan.joined_by.add(user)
    plan.save()
    return redirect('/travels')
