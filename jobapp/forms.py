from django import forms


class regform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    username=forms.CharField(max_length=250)
    password=forms.CharField(max_length=100)
    cpassword=forms.CharField(max_length=100)

class reglog(forms.Form):
    username=forms.CharField(max_length=250)
    password=forms.CharField(max_length=100)

class postjobform(forms.Form):
    jname=forms.CharField(max_length=50)
    cname=forms.CharField(max_length=50)
    extype=forms.CharField(max_length=100)
    wptype=forms.CharField(max_length=100)
    wtype=forms.CharField(max_length=100)
    jobname=forms.CharField(max_length=250)