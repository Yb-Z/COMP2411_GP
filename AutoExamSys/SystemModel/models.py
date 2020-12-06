from django.db import models

# Create your models here.
# 为性别,学院 指定备选字段
GENDER=(
    ('Male','Male'),
    ('Female','Female'),
)
DEPT=(
    ('Department of Computing','Department of Computing'),
)

class Student(models.Model):
    id=models.CharField('Student ID',max_length=20,primary_key=True)
    name=models.CharField('Name',max_length=50)
    gender=models.CharField('Gender',max_length=8,choices=GENDER,default=None)
    dept=models.CharField('Department',max_length=50,choices=DEPT,default=None)
    major=models.CharField('Major',max_length=50,default=None)
    password=models.CharField('Password',max_length=50,default='111')
    email=models.EmailField('Email',default=None)

    class Meta:
        db_table='student'
        verbose_name='Student'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

class Teacher(models.Model):
    id=models.CharField('Teacher ID',max_length=20,primary_key=True)
    name=models.CharField('Name',max_length=50)
    gender=models.CharField('Gender',max_length=8,choices=GENDER,default=None)
    dept=models.CharField('Department',max_length=50,choices=DEPT,default=None)
    password=models.CharField('Password',max_length=50,default='111')
    email=models.EmailField('Email',default=None)

    class Meta:
        db_table='teacher'
        verbose_name='Teacher'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;
