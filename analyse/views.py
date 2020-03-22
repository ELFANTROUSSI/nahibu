from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import *
from django import forms
from .forms import *
from django.core.mail import send_mail
from wsgiref.util import FileWrapper
import json
# Create your views here.

def index(response):
    kitnb = response.GET['kitnb']
    res=NahibuClient.objects.values_list('results', flat=True).filter(kitNumber=kitnb)
    res2=Result.objects.values_list('document', flat=True).filter(kitNumber=kitnb)
    if(len(res)!=0):
        if res[0]=="nolink":
            if len(res2)!=0:
                fname=NahibuClient.objects.values_list('firstName', flat=True).filter(kitNumber=kitnb)
                lname=NahibuClient.objects.values_list('lastName', flat=True).filter(kitNumber=kitnb)
                mail=NahibuClient.objects.values_list('mail', flat=True).filter(kitNumber=kitnb)
                analyse=res2[0].replace("documents/","")
                print("********************",analyse)
                return render(response,"analyse/profil.html",{"analyse":analyse,
                                                            "fname":fname[0],
                                                            "nb":kitnb,
                                                            "lname":lname[0],
                                                            "mail":mail[0],})
            else:
                return render(response,"analyse/wait.html",{})
        else:
            name=NahibuClient.objects.values_list('firstName', flat=True).filter(kitNumber=kitnb)
            return render(response,"analyse/profil.html",{"analyse":res[0],
                                                        "name":name[0]})
    else:
        return render(response,"analyse/form.html",{"nb":kitnb})


def form(response):
    form=response.GET
    knb=form["kitnumber"]
    res=Result.objects.values_list('document', flat=True).filter(kitNumber=knb)
    fname=form["fname"]
    lname=form["lname"]
    mail=form["mail"]
    t=NahibuClient(kitNumber=knb,firstName=fname,lastName=lname,mail=mail)
    t.save()
    if len(res)!=0:
        return HttpResponse(res[0])
    return render(response,"analyse/wait.html",{})
def addFile(request):
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail("Hello From Django",
                        "Hi its a test",
                        "oussama@elfantroussi.com",
                        ["elfantroussi.oussama@gmail.com"],
                        fail_silently=False)
            return HttpResponse("Le mail est envoyé")
    else:
        form = ResultForm()
    return render(request, 'analyse/addFile.html', {
        'form': form
    })

def downloadResult(request,analyse):
    analyse="media/documents/Classeur_test_dev.xlsx"
    with open(analyse, "rb") as excel:
        data = excel.read()
    response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s_Report.xlsx'
    return response
