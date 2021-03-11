from django.shortcuts import render
from core.models import vetan5680
from .forms import Uploadpdf


# Create your views here.
def home(request):
    return render (request, 'core/index.html',{'name':'Pankaj'})

def prapatra(request):
    return render(request,'core/prapatra.html')

def rajpatra(request):
    return render(request,'core/rajpatra.html')

# def niyu(request):
#     emp=vetan5680.objects.all()
#     return render(request,'core/5680.html',{'em':emp})

def rankaro(request):
    return render(request,'core/rankaro.html')

def undercons(request):
    return render(request,'core/undercons.html')

def calcform(request):
    return render(request,'core/gradu.html')

def calcu(request):   
    basic1 = int(request.GET['basic'])
    years1=int(request.GET['year'])    
    taxfree_amount = 2000000
    taxable_amount = 0
    perday = basic1 / 26
    gd= years1 * 15
    gra=int(gd*perday)
    if gra>taxfree_amount:
        taxable_amount=gra-taxfree_amount
    graduty={'grad':gra, 'taxamt':taxable_amount,'taxfree':taxfree_amount}
    return render(request,'core/output.html',graduty)

def fancing(request):
    return render(request,'core/fancing.html')

def fancingout(request):
    return render(request,'core/fancoutput.html')

def gurthwise(request):
    return render(request,'core/gurthwise.html')

def fileupload(request):
    if request.method == 'POST':
        fm= Uploadpdf(request.POST)
        # fields=['title','file','linkto']
        if fm.is_valid():
            tit =fm.cleaned_data['title']
            filee=fm.cleaned_data['file']
            link=fm.cleaned_data['linkto']
            print(tit)
            print(filee)
            print(link)
    else:
        fm=Uploadpdf()
    return render(request, 'core/uploadpdf.html',{'form':fm})

# def imageupload(request):
#     if request.method == 'POST':
#         fm= imageupload(request.POST)
#         # fields=['title','image','linkto']
#         if fm.is_valid():
#             tit =fm.cleaned_data['title']
#             filee=fm.cleaned_data['file']
#             link=fm.cleaned_data['linkto']
#             print(tit)
#             print(filee)
#             print(link)
#     else:
#         fm=Uploadpdf()
#     return render(request, 'core/uploadimage.html',{'form':fm})

def dfoletter(request):
    return render(request,'core/dfoletter.html')

def ccfletter(request):
    return render(request,'core/ccfletter.html')