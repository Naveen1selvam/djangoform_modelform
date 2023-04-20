from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TOF=TopicForm()
    d={'tof':TOF}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is inserted successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'wof':WFO}
    if request.method=='POST':
        WDF=WebpageForm(request.POST)
        if WDF.is_valid():
            WDF.save()
            return HttpResponse('Webpage data insert successfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AOF=AccessrecordForm()
    d={'aof':AOF}
    if request.method=='POST':
        ADF=AccessrecordForm(request.POST)
        if ADF.is_valid():
            ADF.save()
            return HttpResponse('Accessrecord data insert successfully')

    return render(request,'insert_accessrecord.html',d)

