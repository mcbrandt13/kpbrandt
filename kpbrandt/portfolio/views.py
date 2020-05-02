from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse


# TODO FILE DOWNLOAD FOR PDF
def index(request):
    return render(request, 'index.html')

def videos(request):
    return render(request, 'videos.html')

def ava(request):
    return render(request, 'ava.html')