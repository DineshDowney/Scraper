from django.shortcuts import render
from AppOne import forms
from AppOne import Scraper as sc
# Create your views here.

def FormFun(request):
    FormObj = forms.FormClass()
    x=""
    y=""
    z=""
    if request.method=='POST':
        FormObj=forms.FormClass(request.POST)
        if FormObj.is_valid():
            para=FormObj.cleaned_data['Name']
            x,y,z=sc.func(para)
    context = {'form_dic1':FormObj, 'x': x, 'y':y,"z":z}
    return render(request,"index1.html",context)
