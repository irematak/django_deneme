from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from datetime import datetime, date



class Politika(models.Model):
    id = models.AutoField(primary_key=True)
    baslik = models.CharField(blank=True,null= True, max_length=100)
    amac =  RichTextField(blank=True, null=True)
    kapsam =   RichTextField(blank=True, null=True)
    tanimlar =   RichTextField(blank=True, null=True)
    referanslar =  RichTextField(blank=True, null=True)
    uygulama =   RichTextField(blank=True, null=True)
    sorumluluk =   RichTextField(blank=True, null=True)
    kontrol =  RichTextField(blank=True, null=True)
    ekler =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)
    


#def __str__(self):
        #return "%s " %(self.baslik)  #titile ile degisitirilecek
    def __str__(self):
        return self.name + " - " + self.upload_date.strftime("%d/%m/%Y %H:%M:%S")
class Meta:
    db_table = "politika"  



class Prosedur(models.Model):
    id = models.AutoField(primary_key=True)
    baslik = models.CharField(blank=True,null= True, max_length=100)
    amac =  RichTextField(blank=True, null=True)
    kapsam =   RichTextField(blank=True, null=True)
    tanimlar =   RichTextField(blank=True, null=True)
    referanslar =  RichTextField(blank=True, null=True)
    uygulama =   RichTextField(blank=True, null=True)
    sorumluluk =   RichTextField(blank=True, null=True)
    kontrol =  RichTextField(blank=True, null=True)
    ekler =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)
   
    def __str__(self):
        return "%s " %(self.baslik)  #titile ile degisitirilecek
class Meta:
    db_table = "prosedur"  





class Talimat(models.Model):
    baslik = models.CharField(blank=True,null= True, max_length=100)
    talimat =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)
    
 
def __str__(self):
        return "%s " %(self.baslik)  #titile ile degisitirilecek
class Meta:
    db_table = "talimat" 



class Form(models.Model):
    baslik = models.CharField(blank=True,null= True, max_length=100)
    form =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)
    
 
def __str__(self):
        return "%s " %(self.baslik) #titile ile degisitirilecek
class Meta:
    db_table = "form" 


class Liste(models.Model):
    baslik = models.CharField(blank=True,null= True, max_length=100)
    liste =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)

 
def __str__(self):
        return "%s " %(self.baslik)  #titile ile degisitirilecek
class Meta:
    db_table = "liste" 


class Tablo(models.Model):
    baslik = models.CharField(blank=True,null= True, max_length=100)
    tablo =  RichTextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    revision_number = models.IntegerField(default=1)
    
    
def __str__(self):
        return  "%s " %(self.baslik) #titile ile degisitirilecek
class Meta:
    db_table = "tablo" 


