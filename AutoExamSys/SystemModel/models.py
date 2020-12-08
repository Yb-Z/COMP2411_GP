from django.db import models

'''
CREATE TABLE Student
(
  stuID CHAR(9) NOT NULL,
  stuName VARCHAR(100) NOT NULL,
  stuPW VARCHAR(25) NOT NULL,
  stuEmail VARCHAR(100) NOT NULL,
  stuMajor VARCHAR(100) NOT NULL,
  PRIMARY KEY (stuID)
);
'''
class Student(models.Model):
    id=models.CharField('stuID',max_length=9,primary_key=True)
    name=models.CharField('stuName',max_length=100)
    password=models.CharField('stuPW',max_length=25)
    email=models.EmailField('stuEmail')
    major=models.CharField('stuMajor',max_length=50)

    class Meta:
        db_table='Student'
        verbose_name='Student'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

'''
CREATE TABLE Teacher
(
  TID CHAR(9) NOT NULL,
  TName VARCHAR(100) NOT NULL,
  TPW VARCHAR(25) NOT NULL,
  TEmail VARCHAR(100) NOT NULL,
  TDept VARCHAR(100) NOT NULL,
  PRIMARY KEY (TID)
);
'''
class Teacher(models.Model):
    id=models.CharField('TID',max_length=9,primary_key=True)
    name=models.CharField('TName',max_length=100)
    password=models.CharField('TPW',max_length=25)
    email=models.EmailField('TEmail')
    dept=models.CharField('Department',max_length=100)

    class Meta:
        db_table='Teacher'
        verbose_name='Teacher'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;
        
'''
CREATE TABLE Subject
(
  subjID VARCHAR(8) NOT NULL,
  subjName VARCHAR(100) NOT NULL,
  semester INT NOT NULL,
  year INT NOT NULL,
  PRIMARY KEY (subjID)
);
'''
class Subject(models.Model):
    id=models.CharField('subjID',max_length=8,primary_key=True)
    name=models.CharField('subjName',max_length=100)
    semester=models.IntegerField('semester')
    year=models.IntegerField('year')

    class Meta:
        db_table='Subject'
        verbose_name='Subject'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

'''
CREATE TABLE TeachSubj
(
  TID CHAR(9) NOT NULL,
  subjID VARCHAR(8) NOT NULL,
  PRIMARY KEY (TID, subjID),
  FOREIGN KEY (TID) REFERENCES Teacher(TID),
  FOREIGN KEY (subjID) REFERENCES Subject(subjID)
);
'''
class TeachSubj(models.Model):
    subjID=models.ForeignKey('Subject',on_delete=models.CASCADE)
    tid=models.ForeignKey('Teacher',on_delete=models.CASCADE)

    class Meta:
        db_table='TeachSubj'
        verbose_name='TeachSubj'
        verbose_name_plural=verbose_name
        unique_together=("subjID","tid")
    def __str__(self):
        return self.id;

'''
CREATE TABLE Class_
(
  classID VARCHAR(16) NOT NULL,
  subjID VARCHAR(8) NOT NULL,
  TID CHAR(9) NOT NULL,
  PRIMARY KEY (classID),
  FOREIGN KEY (subjID) REFERENCES Subject(subjID),
  FOREIGN KEY (TID) REFERENCES Teacher(TID)
);
'''
class Class(models.Model):
    id=models.CharField('classID',max_length=16,primary_key=True)
    subjID=models.ForeignKey('Subject',on_delete=models.CASCADE)
    tid=models.ForeignKey('Teacher',on_delete=models.CASCADE)

    class Meta:
        db_table='Class'
        verbose_name='Class'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

'''
CREATE TABLE Take
(
  stuID CHAR(9) NOT NULL,
  classID VARCHAR(16) NOT NULL,
  PRIMARY KEY (stuID, classID),
  FOREIGN KEY (stuID) REFERENCES Student(stuID),
  FOREIGN KEY (classID) REFERENCES Class(classID)
);
'''
class Take(models.Model):
    stuID=models.ForeignKey('Student',on_delete=models.CASCADE)
    classID=models.ForeignKey('Class',on_delete=models.CASCADE)

    class Meta:
        db_table='Take'
        verbose_name='Take'
        verbose_name_plural=verbose_name
        unique_together=(("stuID","classID"))
    def __str__(self):
        return self.id;

'''
CREATE TABLE GetResult
(
  grade CHAR(1) NOT NULL,
  comment VARCHAR(2000) NOT NULL,
  stuID CHAR(9) NOT NULL,
  subjID VARCHAR(8) NOT NULL,
  PRIMARY KEY (stuID, subjID),
  FOREIGN KEY (stuID) REFERENCES Student(stuID),
  FOREIGN KEY (subjID) REFERENCES Subject(subjID)
);
'''
class GetResult(models.Model):
    grade=models.CharField('Grade',max_length=1)
    comment=models.CharField('Comment',max_length=2000)
    stuID=models.ForeignKey('Student',on_delete=models.CASCADE)
    subjID=models.ForeignKey('Subject',on_delete=models.CASCADE)
    class Meta:
        db_table='GetResult'
        verbose_name='GetResult'
        verbose_name_plural=verbose_name
        unique_together=(("stuID","subjID"))
    def __str__(self):
        return self.id;

'''
CREATE TABLE Paper
(
  PID CHAR(16) NOT NULL,
  date_ DATE NOT NULL,
  startTime CHAR(8) NOT NULL,
  duration CHAR(9) NOT NULL,
  classID VARCHAR(16) NOT NULL,
  PRIMARY KEY (PID),
  FOREIGN KEY (classID) REFERENCES Class(classID)
);
'''
class Paper(models.Model):
    id=models.CharField('PID',max_length=16,primary_key=True)
    date=models.DateTimeField(auto_now_add=True)
    startTime=models.CharField('startTime',max_length=8)
    duration=models.CharField('duration',max_length=9)
    classID=models.ForeignKey('Class',on_delete=models.CASCADE)

    class Meta:
        db_table='Paper'
        verbose_name='Paper'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;
    def getDurationInSec(self):
        return 3600 * int(self.duration[0:2]) + 60 * int(self.duration[3:5]) + int(self.duration[6:8])

'''
CREATE TABLE Question
(
  QID INT NOT NULL,
  Qtype CHAR(2) NOT NULL,
  Qcontent VARCHAR(2000) NOT NULL,
  optional INT NOT NULL,
  PRIMARY KEY (QID)
);
'''
class Question(models.Model):
    id=models.CharField('QID',max_length=16,primary_key=True)
    type=models.CharField('Qtype',max_length=2)
    content=models.CharField('Qcontent',max_length=2000)
    optional=models.BooleanField('optional',default=True)
    mark=models.IntegerField('Fullmark')

    class Meta:
        db_table='Question'
        verbose_name='Questions'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

'''
CREATE TABLE Question_SA
(
  SAContent VARCHAR(2000) NOT NULL,
  QID INT NOT NULL,
  FOREIGN KEY (QID) REFERENCES Question(QID)
);
'''
class Question_SA(models.Model):
    SAContent=models.CharField('SAContent',max_length=2000)
    qid=models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        db_table='Question_sa'
        verbose_name='Question_SA'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

'''
CREATE TABLE Contain
(
  CSN INT NOT NULL,
  QID INT NOT NULL,
  PID CHAR(16) NOT NULL,
  PRIMARY KEY (QID, PID),
  FOREIGN KEY (QID) REFERENCES Question(QID),
  FOREIGN KEY (PID) REFERENCES Paper(PID)
);
'''
class Contain(models.Model):
    csn=models.IntegerField('CSN')
    qid=models.ForeignKey('Question',on_delete=models.CASCADE)
    pid=models.ForeignKey('Paper',on_delete=models.CASCADE)
    class Meta:
        db_table='Contain'
        verbose_name='Contain'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;
