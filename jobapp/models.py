from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class regmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)

class postjob(models.Model):
    catchoice=[('remote','remote'),
               ('hybrid','hybrid')]
    jobtype=[('fulltime','fulltime'),
             ('parttime','parttime')]
    exp=[('0-1','0-1'),('2-3','2-3'),('4-5','4-5'),('6-7','6-7'),('8-9','8-9'),('10-11','10-11')]

    jname=models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    extype=models.CharField(max_length=100,choices=exp)
    wptype=models.CharField(max_length=100,choices=catchoice)
    wtype=models.CharField(max_length=100,choices=jobtype)
    jobname=models.CharField(max_length=250)

class applyjob(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    exper=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    iname=models.FileField(upload_to='jobapp/static')
