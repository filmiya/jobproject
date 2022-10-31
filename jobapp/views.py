from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.core.mail import send_mail
from jobproject.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .forms import *
from .models import *
from django.conf import settings
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'index.html')
def joblogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(joblogin) #login
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect(joblogin)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(joblogin)
        #home(request,user)
        ob=profile.objects.filter(user=user)
        return render(request,'jobprofile.html',{'company':ob})
    return render(request,'login.html')
#register
def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if User.objects.filter(username=username).first():
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)
        if password==cpassword:
             user_obj=User(username=username,email=email)
             user_obj.set_password(password)
             user_obj.save()
             user_obj.set_password(cpassword)

             user_obj.save()
             auth_token=str(uuid.uuid4())
             profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
             profile_obj.save()
             send_mail_regis(email,auth_token)
             return redirect('/verify')
    return render(request,'register.html')

def emailsuccess(request):
    return render(request,'success.html')
def emailverify(request):
    return render(request,'token_send.html')
def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)
def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(joblogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(joblogin)
    else:
        return redirect('/error')

def error(request):
    return render(request,'errorpage.html')
def jobpro(request):
    pro=User.objects.all()
    for i in pro:
        nm=i.username
        em=i.email
        id=i.id
    return render(request,'jobprofile.html',{'name':nm,'email':em,'id':id})
def edit_comp(request,mail,token):

    if request.method=='POST':
        a=User.objects.filter(email=mail).first()
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.save()
        b=profile.objects.filter(auth_token=token)
        return render(request,'jobprofile.html',{'company':b})
    c=profile.objects.get(auth_token=token)
    return render(request,'edit_user.html',{'c':c})
def regcomp(request):
    x=User.objects.all()
    li=[]
    email=[]
    for i in x:
        nm=i.username
        em=i.email
        li.append(nm)
        email.append(em)
        li1=li[1:]
        em1=email[1:]
    mylist=zip(li1,em1)
    return render(request,'regcomp.html',{'mylist':mylist})
    # comp=User.objects.get(id=id)
    # if request.method=='POST':
    #     comp.username=request.POST.get('cname')
    #     comp.email=request.POST.get('email')
    #     comp.save()
    #     return redirect(success)
    # context={'comp':comp}
    # return render(request,'edit_user.html',context)

# def regcomp(request):
#     mylist=User.objects.all()
#     return render(request,'regcomp.html',{'mylist':mylist})
def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        b=regmodel.objects.filter(username=username).first()
        if b is None:
            messages.success(request,'username not found')
            return redirect(userlogin)
        c = regmodel.objects.filter(password=password).first()
        if c is None:
            messages.success(request, 'password not found')
            return redirect(userlogin)
        a=regmodel.objects.filter(username=username)
        return render(request,'user_profile.html',{'user':a})
    return render(request, 'userlogin.html')
    # if request.method=='POST':
    #     a=reglog(request.POST)
    #     if a.is_valid():
    #         unm=a.cleaned_data['username']
    #         psd=a.cleaned_data['password']
    #         b=regmodel.objects.all()
    #
    #         for i in b:
    #             if (unm==i.username and psd==i.password):
    #
    #                 return redirect(user_profile)
    #         else:
    #             messages.success(request, 'invalid username or password')
    # return render(request,'userlogin.html')
def userregister(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fnm=a.cleaned_data['fname']
            lnm=a.cleaned_data['lname']
            unm=a.cleaned_data['username']
            psd=a.cleaned_data['password']
            cpsd=a.cleaned_data['cpassword']
            b=regmodel(fname=fnm,lname=lnm,username=unm,password=psd,cpassword=cpsd)
            b.save()
            return redirect(userlogin)
        else:
            messages.success(request,'Registration failed')
    return render(request,'userregister.html')

def post_job(request):
    if request.method=='POST':
        a=postjobform(request.POST)
        if a.is_valid():
            jname1=a.cleaned_data['jname']
            cname1=a.cleaned_data['cname']
            extype1=a.cleaned_data['extype']
            wptype1=a.cleaned_data['wptype']
            wtype1=a.cleaned_data['wtype']
            jobname1 = a.cleaned_data['jobname']
            b=postjob(jname=jname1,cname=cname1,extype=extype1,wptype=wptype1,wtype=wtype1,jobname=jobname1)
            b.save()
            return HttpResponse('job posted')
        else:
            return HttpResponse('error')
    return render(request,'postjob.html')
def jobshow(request):
    postjob1=postjob.objects.all()
    return render(request,'jobshow.html',{'postjob1':postjob1})
def jobshow1(request,id):
    postjob2=postjob.objects.get(id=id)
    return render(request, 'jobshow1.html', {'postjob2':postjob2})

def apply_job(request):

    if request.method=='POST':
        prod=applyjob()
        prod.username=request.POST.get('username')
        prod.email=request.POST.get('email')
        prod.exper=request.POST.get('exper')
        prod.location=request.POST.get('location')
        prod.iname=request.FILES['iname']
        prod.save()
        messages.success(request, 'Apply job successfully')
        return redirect(apply_job)
    return render(request,'applyjob.html')
def user_profile(request):

    return render(request,'user_profile.html')
def view_profile(request):
    x=applyjob.objects.all()
    li=[]
    nam=[]
    em=[]
    expe=[]
    loca=[]
    for i in x:
        path=i.iname
        li.append(str(path).split("/")[-1])
        nm=i.username
        nam.append(nm)
        em1=i.email
        em.append(em1)
        exp1=i.exper
        expe.append(exp1)
        loc1=i.location
        loca.append(loc1)
    mylist=zip(li,nam,em,expe,loca)
    return render(request, 'view_profile.html',{'mylist':mylist})
def user_edit(request,id):
    a = regmodel.objects.get(id=id)
    if request.method=='POST':
        a.fname = request.POST.get('fname')
        a.lname = request.POST.get('lname')
        a.username = request.POST.get('username')
        a.password = request.POST.get('password')
        a.cpassword = request.POST.get('cpassword')
        a.save()
        messages.success(request, 'Profile edited')
    context={'addd':a}
    return render(request, 'user_edit.html',context)

