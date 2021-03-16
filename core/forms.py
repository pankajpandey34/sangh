from django.core import validators
from django import forms
from django.db.models import fields
from .models import pdffile, imagefile
from core import models

class Uploadpdf(forms.ModelForm):
    class Meta:
        model = pdffile
        fields=['title','javak','date','linkto','file']
        labels={'title':'विषय','javak':"जावक क्रमांक",'date':'पत्र दिनांक','linkto':'किसके साथ लिंक करना है'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                'javak':forms.TextInput(attrs={'class':'form-control'}),
                'date':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
                'linkto':forms.Select(attrs={'class':'form-control'}),
        }

class uploadimage(forms.ModelForm):
    class Meta:
        model = imagefile
        fields=['title','linkto','file']
