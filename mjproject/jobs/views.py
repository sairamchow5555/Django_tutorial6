from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    return HttpResponse("<h1>Hyd job information</h1>")

def bngjobsinfo(request):
    return HttpResponse("<h1>Bng job information</h1>")

def punejobinfo(request):
    return HttpResponse("<h1>Pune job information</h1>")

def biharjobinfo(request):
    return HttpResponse("<h1>Bihar job information</h1>")

def apjobinfo(request):
    return HttpResponse("<h1>Ap job information</h1?")
