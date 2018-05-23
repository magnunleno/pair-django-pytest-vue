#!/usr/bin/env python3
# encoding: utf-8

from django.shortcuts import render
from .models import Tarefa


def index(request):
    queryset = Tarefa.objects.all()
    context = {'queryset': queryset}
    return render(request, 'todo/index.html', context)
