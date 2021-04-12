from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import pdffile
from .models import pdffile, imagefile
from core import models

class Uploadpdf(forms.ModelForm):
    class Meta:
        model = pdffile
        fields=['title','javak','date','linkto','file']
        labels={'title':'विषय','javak':"जावक क्रमांक",'date':'पत्र दिनांक','linkto':'किसके साथ लिंक करना है'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}),
                'javak':forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}),
                'date':forms.DateInput(attrs={'class':'form-control','id':'datepicker', 'autocomplete':"off"}),
                'linkto':forms.Select(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    password1= forms.CharField(label='पासवर्ड', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='पासवर्ड पुष्टि', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'username':'युजर का नाम','first_name':'प्रथम नाम','last_name':'उपनाम','email':'ईमेल'},
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}),
                'last_name':forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}),
                'email':forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}),                
                }
       
class uploadimage(forms.ModelForm):
    class Meta:
        model = imagefile
        fields=['title','linkto','file']
        

