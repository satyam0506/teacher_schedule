from django.shortcuts import render
from .models import Teacher,TeacherOccupy
from django.utils import timezone
from datetime import timedelta

now = timezone.now()
time_to_fetch = now + timedelta(minutes=5)

def hourly_start_task():
    '''this is a cron task
    run in interval of 60 mins starting from 8:55 and emds at 3:55 for monday to sat'''
    teacher_occupy_objs = TeacherOccupy.objects.filter(start_time=time_to_fetch)
    mail_subject = 'Your Class is about to start'
    for t in teacher_occupy_objs:
        mail_receipnt = t.teacher.email
        subject_name = t.subject
        class_name = t.class_name
        start_time = t.start_time
        send_mail(mail_subject,mail_receipnt,subject_name,class_name,start_time)


def hourly_end_task():
    '''this id cron task
    run in interval of 60 mins startiing from 9:55 and ends at 4:55 for monday to sat'''
    teacher_occupy_objs = TeacherOccupy.objects.filter(end_time=time_to_fetch)
    message = 'Please wrap your class'
    for t in teacher_occupy_objs:
        send_notification(t.teacher.name,message)

def send_mail(mail_subject,mail_receipnt,subject_name,class_name,start_time):
    '''trigger by hourly start_task
    send email to user'''
    # user 3rd party mail client to send mails
    pass

def send_notification(user,message):
    '''trigger by hourly end_task
    send notification to users'''
    # configure FCM
    pass