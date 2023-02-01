from django.shortcuts import render
from app1.models import *
from django.db.models.functions import *
# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name='MSD')
    QSW=Webpage.objects.exclude(name='MSD')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.order_by(Length('name'))
    QSW=Webpage.objects.order_by(Length('name').desc())
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)


def display_access(request):
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.all().order_by('date')
    d={'accessrecords':QSA}
    return render(request,'display_Access.html',d)




