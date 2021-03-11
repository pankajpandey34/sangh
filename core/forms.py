from django.core import validators
from django import forms
from django.db.models import fields
from .models import pdffile
from core import models

class Uploadpdf(forms.ModelForm):
    class Meta:
        model = pdffile
        fields=['title','file','linkto']