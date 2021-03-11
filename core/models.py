from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.lookups import Range

pdf_choice=(
    ('DrRangerSenerity','पदक्रम उपवनक्षेत्रपाल'),
	('ForesterSenerity','पदक्रम वनपाल'),
	('FgSenerity','पदक्रम वनरक्षक'),
	('HardaSanghLetter','हरदा संघ के पत्र'),
	('BhopalSanghLetter','भोपाल संघ के पत्र'),
	('Gajat','राजपत्र'),
	('Parpatra','प्रपत्र'),
	('Niyam','नियम'),
	('Act','अधिनियम'),
    ('empRule','सेवा भीर्ती नियम'),
	('RtiAct','सूचना का अधिकार'),
	('PccfLetter','प्रधान मुख्‍य वनसंरक्षक के पत्र'),
	('CcfLetter','मुख्‍य वन संरक्षक के पत्र'),
	('DfoLetter','वनमंडल के पत्र'),)

image_choice=(
    ('slide','स्‍लाईड'),
	('logo','लोगो'),	
	('newspaper','सामाचार पत्र'),)

division_choice=(
    ('hardaT','सामान्‍य वनमंडल हरदा'),
    ('hardaP','उत्‍पादन वनमंडल हरदा'),
)

subdivision_choice=(
    ('sdoST','उपवनमंडल दक्षिण हरदा सामान्‍य'),
    ('sdoNT','उपवनमंडल उत्‍तर हरदा सामान्‍य'),
    ('sdoSP','उपवनमंडल दक्षिण हरदा उत्‍पादन'),
    ('sdoNP','उपवनमंडल उत्‍तर हरदा उत्‍पादन'),
)

range_choice=(
    ('makraiT','मकड़ाई सामान्‍य'),
    ('magardhaT','मगरधा सामान्‍य'),
    ('borpaniT','बोरपानी सामान्‍य'),
    ('handiaT','हंडिया सामान्‍य'),
    ('temagoanT','टेमागांव सामान्‍य'),
    ('rahatgoanT','रहटगांव सामान्‍य'),
    ('makraiP','मकड़ाई उत्‍पादन'),
    ('magardhaP','मगरधा उत्‍पादन'),
    ('borpaniP','बोरपानी उत्‍पादन'),
    ('handiaP','हंडिया उत्‍पादन'),
    ('temagoanP','टेमागांव उत्‍पादन'),
    ('rahatgoanP','रहटगांव उत्‍पादन'),
)
# Create your models here.
# class division(models.Model):
#     name =models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
 
# class subdivision(models.Model):
#     name = models.CharField(max_length= 50)
#     division = models.ForeignKey(to=division, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
   
# class range(models.Model):
#     name = models.CharField(max_length=50)
#     subdivision = models.ForeignKey(to=subdivision, on_delete=models.CASCADE) 
#     def __str__(self):
#         return self.name
################################# Start Upload PDF File ##########################################
class pdffile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdf')
    linkto =models.CharField(choices=pdf_choice,max_length=100)

################################# End Upload PDF File ##########################################

################################# Start Upload Image File ##########################################
class imagefile(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='img')
    linkto =models.CharField(choices=pdf_choice,max_length=100)
    # def __str__(self):
    #     return self.linkto
################################# End Upload Image File ##########################################
class vetan5680(models.Model):
    name=models.CharField(max_length=100)
    dob=models.CharField(max_length=25, blank=True)
    empyear=models.CharField(max_length=4)
    division=models.CharField(choices=division_choice, max_length=100)
    range=models.CharField(choices=range_choice, max_length=100)
    
    
