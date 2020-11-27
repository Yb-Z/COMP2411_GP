from django.shortcuts import render,redirect
from student import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,"/Users/zyb/Desktop/Class/comp2411/COMP2411_GP/AutoExamSys/templatates/index.html")