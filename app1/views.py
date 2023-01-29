from django.shortcuts import render
from app1.models import *
from django.db.models.functions import *
# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)


def display_access(request):
    QSA=AccessRecord.objects.all()  
    d={'accessrecords':QSA}
    return render(request,'display_Access.html',d)



