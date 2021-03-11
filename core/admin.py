from django.contrib import admin
from core.models import vetan5680,pdffile
# Register your models here.

# class divi(admin.ModelAdmin):
#     list_display=['name']
#     list_filter=['name']
#     search_fields=['name']
# admin.site.register(division,divi)

# class subdiv(admin.ModelAdmin):
#     list_display=['name']
#     list_filter=['name']
#     search_fields=['name']
# admin.site.register(subdivision, subdiv)

# class ran(admin.ModelAdmin):    
#     list_display=['name']
#     list_filter=['name']
#     search_fields=['name']
# admin.site.register(range,ran)

class emp(admin.ModelAdmin):    
    list_display=['name','dob']
    list_filter=['name']
    search_fields=['name']
admin.site.register(vetan5680,emp)


class pdffiler(admin.ModelAdmin):    
    list_display=['title','javak','date','linkto','file']    
admin.site.register(pdffile, pdffiler)