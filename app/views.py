from django.shortcuts import render

# Create your views here.
 
from django.http import HttpResponse
from app.models import *

def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]

        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)


    return render(request,'insert_topic.html')

def insert_Webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_Webpage.html',d1)

    return render(request,'insert_Webpage.html',d)

def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#['C','FB','VB']
        #print(tn)
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)

        d1={'webpages':QLWO}
        return render(request,'display_Webpage.html',d1) 

    return render(request,'select_multiple_webpage.html',d)



def checbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',d)