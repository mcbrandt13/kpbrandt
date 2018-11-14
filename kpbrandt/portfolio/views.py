from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    #return render(request, 'index.html')
    return HttpResponse("kevin's kode korner.")