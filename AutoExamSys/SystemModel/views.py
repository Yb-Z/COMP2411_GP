from django.shortcuts import render,redirect
from SystemModel import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
'''
def index(request):
    return render(request,"./index.html")
'''
def login(request):
    return render(request, "./login.html")
    
def demo(request):
    return render(request, "./demo.html")

def studentLogin(request):
    if request.method=='POST':
        # 获取表单信息
        stuId=request.POST.get('id')
        password=request.POST.get('password')
        print("id",stuId,"password",password)
        '''
        select student from students
        where id=stuId
        '''
        # 通过学号获取该学生实体
        student=models.Student.objects.get(id=stuId)
        print(student)
        if password==student.password:  #登录成功
            return render(request,'./student.html',{'student':student})
        else:
            return render(request, './student.html', {'message': 'Wrong Password!'})

def teacherLogin(request):
    if request.method=='POST':
        # 获取表单信息
        teaId=request.POST.get('id')
        password=request.POST.get('password')
        print("id",teaId,"password",password)
       
        teacher=models.Teacher.objects.get(id=teaId)
        print(teacher)
        if password==teacher.password:  #登录成功
            return render(request,'./teacher.html',{'teacher':teacher})
        else:
        teacher = models.Teacher.objects.get(id=teaId)'message':'Wrong Password!'})

def logout(request):
    return render(request, "./login.html")

def showQuestion(request):
    if request.method=='POST':
        # 获取表单信息
        TODO:
        paper=request.POST.get('paperID')
        password=request.POST.get('password')
        print("id",stuId,"password",password)
        '''
        select student from students
        where id=stuId
        '''
        # 通过学号获取该学生实体
        student=models.Student.objects.get(id=stuId)
        print(student)
        if password==student.password:  #登录成功
            return render(request,'./student.html',{'student':student})
        else:
            return render(request, './student.html', {'message': 'Wrong Password!'})

def nextQuestion(request):
