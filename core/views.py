from django.shortcuts import render
from core.models import vetan5680,pdffile
from .forms import Uploadpdf


# Create your views here.
def home(request):
    return render (request, 'core/index.html',{'name':'Pankaj'})

def niyu(request):
    emp=vetan5680.objects.all()
    return render(request,'core/5680.html',{'em':emp})

def rankfg(request):
    heading="वनरक्षक की पदक्रम सूची"
    return render(request,'core/RankingListTemplate.html',{'heading':heading})

def rankforester(request):
    heading="वनपाल की पदक्रम सूची"
    return render(request,'core/RankingListTemplate.html',{'heading':heading})

def rankaro(request):
    heading="उपवनक्षेत्रपाल की पदक्रम सूची"
    return render(request,'core/RankingListTemplate.html',{'heading':heading})

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
            fm.save()
    else:
        fm=Uploadpdf()
    return render(request, 'core/uploadpdf.html',{'form':fm})

def imageupload(request):
    if request.method == 'POST':
        fm= imageupload(request.POST)
        # fields=['title','image','linkto']
        if fm.is_valid():
            tit =fm.cleaned_data['title']
            filee=fm.cleaned_data['file']
            link=fm.cleaned_data['linkto']
            fm.save()
    else:
        fm=Uploadpdf()
    return render(request, 'core/uploadimage.html',{'form':fm})

def dfoletter(request):
    heading="वनमंडल के पत्र"
    data=pdffile.objects.filter(linkto="DfoLetter")
    return render(request,'core/letterTemplate.html',{'heading':heading,'data':data})

def ccfletter(request):
    heading="मुख्‍य वनसंरक्षक के पत्र"
    data=pdffile.objects.filter(linkto="CcfLetter")
    return render(request,'core/letterTemplate.html',{'heading':heading,'data':data})

def pccfletter(request):
    heading="प्रधान मुख्‍य वनसंरक्षक के पत्र"
    data=pdffile.objects.filter(linkto="PccfLetter")
    return render(request,'core/letterTemplate.html',{'heading':heading,'data':data})

def hardasanghletter(request):
    heading="वन कर्मचारी संघ हरदा के पत्र"
    data=pdffile.objects.filter(linkto="HardaSanghLetter")
    return render(request,'core/letterTemplate.html',{'heading':heading,'data':data})

def bhopalsanghletter(request):
    heading="वन कर्मचारी संघ भोपाल के पत्र"
    data=pdffile.objects.filter(linkto="BhopalSanghLetter")
    return render(request,'core/letterTemplate.html',{'heading':heading,'data':data})

def prapatra(request):
    return render(request,'core/prapatra.html')

def rajpatra(request):
    return render(request,'core/rajpatra.html')