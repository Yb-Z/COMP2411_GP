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
        # TODO:求补全& fix 这里 下一行的 time 是错误的！
        time = request.POST.get('time')  # time: a string HH:MM:SS
        timeInSec = 3600 * int(time[0:2]) + 60 * int(time[3:5]) + int(time[6:])  # 考试时间转成秒数

        mc = {  # multiple choice
            'qs' : {
                'score': int,
                'title': str,
                'optionA': str,
                'optionB': str,
                'optionC': str,
                'optionD': str,
            },
            # html 访问了 question.id, question.title, question.score, question.optionA, B, C, D
            'qNum': int,
            'points': int,
        }
        fb = {  # fill in blank
            'qs': [questions],  #FIXME: fix this
            # html 访问了 question.id, question.title, question.score
            'qNum': int,
            'points': int,
        }
        sq = {  # standard questions
            'qs': [questions],  #FIXME: fix this
            # html 访问了 question.id, question.title, question.score
            'qNum': int,
            'points': int,
        }

        exam = {
            "timeInSec": timeInSec,
            "mc": mc,
            "fb": fb,
            "sq": sq,

        }

        data = {
            "student": student, #FIXME: fix this
            "subject":subject, #FIXME: fix this
            "exam": exam
        } # TODO: 还有，记得加
        return render(request, './answer.html', data)

def startExam(request):
    student=models.Student.objects.get(request.GET.get('sid'))
    paper=models.Paper.objects.get(request.GET.get('paper'))
