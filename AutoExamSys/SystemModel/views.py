from django.shortcuts import render,redirect
# from SystemModel import models
from AutoExamSys.SystemModel import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,"./index.html")
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
            return render(request,'./student.html',{'message':'Wrong Password!'})
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
            return render(request, './teacher.html', {'message': 'Wrong Password!'})
            
def getExamPaper(request):
    if request.method == 'POST':
        student = request.POST.get('student')  #FIXME:
        subject = request.POST.get('student') #FIXME:
        paperID = request.POST.get('examID')  #FIXME:
        paper = models.Paper.objects.get(id=paperID)
        # TODO:获取question并将question 分类： mc, fb, fl

        exam = {
            "timeInSec": paper.getDurationInSec(), # 考试时间转成秒数 # time: 00h00m00s
            "mc": .filter(type=mc),
            "fb": .filter(type=fb),
            "fl": .filter(type=fl),
        }

        data = {
            "student": student,
            "subject": subject,
            "exam": exam
        }
        return render(request, './answer.html', data)

def startExam(request):
    student=models.Student.objects.get(request.GET.get('sid'))
    paper=models.Paper.objects.get(request.GET.get('paper'))
