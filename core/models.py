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
	('RtiAct','सूचना का अधिकार'),
	('PccfLetter','प्रधान मुख्‍य वनसंरक्षक के पत्र'),
	('CcfLetter','मुख्‍य वन संरक्षक के पत्र'),
	('DfoLetter','वनमंडल के पत्र'),)

image_choice=(
    ('drRangerSenerity','पदक्रम उपवनक्षेत्रपाल'),
	('पदक्रम वनपाल','पदक्रम वनपाल'),	
	('मुख्‍य वन संरक्षक के पत्र','मुख्‍य वन संरक्षक के पत्र'),
	('वनमंडल के पत्र','वनमंडल के पत्र'),)

# Create your models here.
class division(models.Model):
    name =models.CharField(max_length=50)
    def __str__(self):
        return self.name
 
class subdivision(models.Model):
    name = models.CharField(max_length= 50)
    division = models.ForeignKey(to=division, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   
class range(models.Model):
    name = models.CharField(max_length=50)
    subdivision = models.ForeignKey(to=subdivision, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name
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
    division=models.ForeignKey(to=division, on_delete=CASCADE)
    range=models.ForeignKey(to=range, on_delete=CASCADE)
    
    
