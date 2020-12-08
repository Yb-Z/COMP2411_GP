from django.shortcuts import render, redirect
# from SystemModel import models
from SystemModel import models
from AutoExamSys.SystemModel import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.


def index(request):
    return render(request, "./index.html")


def studentLogin(request):
    if request.method == 'POST':
        # 获取表单信息
        stuId = request.POST.get('id')
        password = request.POST.get('password')
        print("id", stuId, "password", password)
        '''
        select student from students
        where id=stuId
        '''
        # 通过学号获取该学生实体
        student = models.Student.objects.get(id=stuId)
        print(student)
        if password == student.password:  # 登录成功
            return render(request, './student.html', {'student': student})
        else:
            return render(request, './student.html', {'message': 'Wrong Password!'})


def teacherLogin(request):
    if request.method == 'POST':
        # 获取表单信息
        teaId = request.POST.get('id')
        password = request.POST.get('password')
        print("id", teaId, "password", password)

        teacher = models.Teacher.objects.get(id=teaId)
        print(teacher)
        if password == teacher.password:  # 登录成功
            return render(request, './teacher.html', {'teacher': teacher})
        else:
            return render(request, './teacher.html', {'message': 'Wrong Password!'})


def getExamPaper(request):
    if request.method == 'POST':
        student = request.POST.get('student')  # FIXME:
        subject = request.POST.get('student')  # FIXME:
        paperID = request.POST.get('examID')  # FIXME:
        paper = models.Paper.objects.get(id=paperID)
        # TODO:获取question并将question 分类： mc, fb, fl


def startExam(request):
    student = models.Student.objects.get(request.GET.get('sid'))
    paper = models.Paper.objects.get(request.GET.get('paper'))
    questions = models.Contain.objects.filter(pid==paper.id).order_by('csn')
    subject=paper.classID.subjID
    questions = questions.qid
    exam = {
        "timeInSec": paper.getDurationInSec(),  # 考试时间转成秒数 # time: 00h00m00s
        "mc": questions.filter(type='MC'), 
        "fb": questions.filter(type='FB'),
        "fl": questions.filter(type='FL'),
    }

    data = {
        "student": student,
        "subject": subject,
        "exam": exam
    }
    return render(request, './answer.html', data)
    student=models.Student.objects.get(request.GET.get('sid'))
    paper=models.Paper.objects.get(request.GET.get('paper'))

def subPrepare(request):
    if request.method == 'POST':
        teacher = request.POST.get('tid')

        numOfQuestion = [
            int(request.POST.get('mcnum')),
            int(request.POST.get('fbnum')),
            int(request.POST.get('flnum'))
        ]  # in order: mc, fb, fl
        pointOfQuestion = [
            int(request.POST.get('mcpoints')),
            int(request.POST.get('fbpoints')),
            int(request.POST.get('flpoints'))
        ]

        questions = { #需要修改
            'mc': [request.POST.get('mc'+str(i+1)) for i in range(numOfQuestion[0])],
            'fb': [request.POST.get('fb'+str(i+1)) for i in range(numOfQuestion[1])],
            'fl': [request.POST.get('fl'+str(i+1)) for i in range(numOfQuestion[2])],
        }
        points = { #需要修改
            'mc': [request.POST.get('mcP'+str(i+1)) for i in range(numOfQuestion[0])],
            'fb': [request.POST.get('fbP'+str(i+1)) for i in range(numOfQuestion[1])],
            'fl': [request.POST.get('flP'+str(i+1)) for i in range(numOfQuestion[2])],
        }

        answer = { #需要修改
            'mc': [request.POST.get('mcA'+str(i+1)) for i in range(numOfQuestion[0])],
            'fb': [request.POST.get('fbA'+str(i+1)) for i in range(numOfQuestion[1])],
        }
        idc = models.Question.Meta.id_count
        for i in range(numOfQuestion[0]):
            q=models.Question.objects.create(id=idc,type='MC',content=questions['mc'][i],optional=False,mark=points['mcP'][i])
            models.Question_SA.objects.create(qid=q,SAContent=answer['mc'][i])
            idc+=1
        for i in range(numOfQuestion[1]):
            q=models.Question.objects.create(id=idc,type='FB',content=questions['fb'][i],optional=False,mark=points['mcP'][i])
            models.Question_SA.objects.create(qid=q,SAContent=answer['fb'][i])
            idc+=1
        for i in range(numOfQuestion[2]):
            q=models.Question.objects.create(id=idc,type='FL',content=questions['fl'][i],optional=False,mark=points['mcP'][i])
            idc+=1

        # TODO: 保存到models
        
        flag=True
        if flag:  # 如果保存成功跳转到teacher
            return render(request,'./teacher.html',{'teacher':teacher})
        else:
            return render(request, './teacher.html', {'message': 'Wrong Password!'})
