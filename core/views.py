from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tenant_home(request):
    return HttpResponse(f"Welcome to Project")