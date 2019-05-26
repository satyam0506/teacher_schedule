from django.contrib import admin
from .models import Teacher,TeacherOccupy


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone','email')

@admin.register(TeacherOccupy)
class TeacherOccupyAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'teacher','start_time','end_time','subject')


