from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=32,blank=True)

    def __str__(self):
        return '%s' % self.name

class TeacherOccupy(models.Model):
    class_name = models.CharField(max_length=32)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    subject = models.CharField(max_length=32)

