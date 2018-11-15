from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

#TODO add templates
#TODO NAVBAR
#TODO BOOTSTRAP
#TODO FIlE DOWNLOAD FOR PDF
def index(request):
    return render(request, 'index.html')
