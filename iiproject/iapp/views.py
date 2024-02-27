from django.shortcuts import render
from . models import Background
from .models import Open
from . models import Choose
from . models import Place
from . models import three

# Create your views here.
def index(request):
    bac=Background.objects.all()
    ope=Open.objects.all()
    cho=Choose.objects.all()
    obj=Place.objects.all()
    the=three.objects.all()



    return render(request,"index.html",{'bac':bac,'ope':ope,'cho':cho,'obj':obj,'the':the})