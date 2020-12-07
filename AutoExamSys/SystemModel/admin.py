# Register your models here.
from django.contrib import admin
from .models import Student,Teacher,Subject, Class, Take
# Register your models here.
# 修改名称
admin.site.site_header='Online Exam System Management'
admin.site.site_title='Online Exam System Management'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','major','password','email')# 要显示哪些信息
    list_display_links = ['id']#点击哪些信息可以进入编辑页面
    search_fields = ['id','name']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['major']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept', 'password', 'email')
    list_display_links = ['id']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'semester','year')
    list_display_links = ['id']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'subjID','tid')
    list_display_links = ['id']

@admin.register(Take)
class TakeAdmin(admin.ModelAdmin):
    list_display = ('stuID', 'classID')
    list_display_links = ['stuID']
