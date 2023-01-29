from django.shortcuts import render, redirect, get_object_or_404  
from io import BytesIO
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
from document.models import Politika, Prosedur, Talimat, Form, Tablo, Liste
from document.forms import PolitikaForm ,ProsedurForm, TalimatForm, FormForm, TabloForm, ListeForm


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict).encode('utf-8')
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def politika_pdf(request, id):
    politika = Politika.objects.get(id=id) 
    pdf = render_to_pdf('show_politika.html', {'politika': politika, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Politika_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def prosedur_pdf(request, id):
    prosedur = Prosedur.objects.get(id=id) 
    pdf = render_to_pdf('show_prosedur.html', {'prosedur': prosedur, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Prosedur_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def talimat_pdf(request, id):
    talimat = Talimat.objects.get(id=id) 
    pdf = render_to_pdf('show_talimat.html', {'talimat': talimat, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Talimat_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def form_pdf(request, id):
    form = Form.objects.get(id=id) 
    pdf = render_to_pdf('show_form.html', {'form': form, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Form_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def tablo_pdf(request, id):
    tablo = Tablo.objects.get(id=id) 
    pdf = render_to_pdf('show_tablo.html', {'tablo': tablo, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Tablo_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

def liste_pdf(request, id):
    liste = Liste.objects.get(id=id) 
    pdf = render_to_pdf('show_liste.html', {'liste': liste, 'download': 'true'}  )
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Liste_%s.pdf" %(id)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response


def politika(request):  
    if request.method == "POST":  
        form = PolitikaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = PolitikaForm()  
    return render(request,'politika.html',{'form':form})  


def prosedur(request):  
    if request.method == "POST":  
        form2 = ProsedurForm(request.POST)  
        if form2.is_valid():  
            try:  
                form2.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form2 = ProsedurForm()  
    return render(request,'prosedur.html',{'form2':form2})  

def talimat(request):  
    if request.method == "POST":  
        form3 = TalimatForm(request.POST)  
        if form3.is_valid():  
            try:  
                form3.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form3 = TalimatForm()  
    return render(request,'talimat.html',{'form3':form3})  

def form(request):  
    if request.method == "POST":  
        form4 = FormForm(request.POST)  
        if form4.is_valid():  
            try:  
                form4.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form4 = FormForm()  
    return render(request,'form.html',{'form4':form4})  

def tablo(request):  
    if request.method == "POST":  
        form5 = TabloForm(request.POST)  
        if form5.is_valid():  
            try:  
                form5.save() 
               
                return redirect('/')  
            except:  
                pass  
    else:  
        form5 = TabloForm()  
    return render(request,'tablo.html',{'form5':form5})  

def liste(request):  
    if request.method == "POST":  
        form6 = ListeForm(request.POST)  
        if form6.is_valid():  
            try:  
                form6.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form6 = ListeForm()  
    return render(request,'liste.html',{'form6':form6})  



def show(request): 
    prosedur = Prosedur.objects.all() 
    politika = Politika.objects.all()  
    talimat = Talimat.objects.all()
    tablo = Tablo.objects.all()
    liste = Liste.objects.all()
    form = Form.objects.all()
    
    return render(request,"show.html",{'politika':politika, 'prosedur':prosedur, 'talimat':talimat, 'tablo':tablo, 'liste':liste, 'form':form}) 


#def edit(request, id):  
    #employee = Employee.objects.get(id=id)  
   # return render(request,'edit.html', {'employee':employee})  

 

def destroy_form(request, id):  
    
    destroy_form = Form.objects.get(id=id) 
 
    destroy_form.delete()  
     
    return redirect("/show")

def destroy_politika(request, id): 

    destroy_politika = Politika.objects.get(id=id) 

    destroy_politika.delete()  
     
    return redirect("/show")

def destroy_prosedur(request, id):  
 
    destroy_prosedur= Prosedur.objects.get(id=id) 
   

    destroy_prosedur.delete()  
    
    return redirect("/show")

def destroy_talimat(request, id):  
  
    destroy_talimat= Talimat.objects.get(id=id) 

   
    destroy_talimat.delete()  
    return redirect("/show")

def destroy_liste(request, id):  

    destroy_liste= Liste.objects.get(id=id) 

    destroy_liste.delete()   

    return redirect("/show")

def destroy_tablo(request, id):  
  
    destroy_tablo= Tablo.objects.get(id=id) 
  

    destroy_tablo.delete() 
   
    return redirect("/show")


def show_politika(request, id):
    politika = Politika.objects.get(id=id) 
    return render(request,'show_politika.html',{'politika':politika,})

def show_prosedur(request, id):
    prosedur = Prosedur.objects.get(id=id) 
    return render(request,'show_prosedur.html',{'prosedur':prosedur})

def show_talimat(request, id):
    talimat = Talimat.objects.get(id=id) 
    return render(request,'show_talimat.html',{'talimat':talimat})

def show_form(request, id):
    form = Form.objects.get(id=id) 
    return render(request,'show_form.html',{'form':form})

def show_liste(request, id):
    liste = Liste.objects.get(id=id) 
    return render(request,'show_liste.html',{'liste':liste})

def show_tablo(request, id):
    tablo = Tablo.objects.get(id=id) 
    return render(request,'show_tablo.html',{'tablo':tablo})


def update_politika(request, id):
   document = get_object_or_404(Politika, pk=id)
   if request.method == 'POST':
        form = PolitikaForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
   else:
        form = PolitikaForm(instance=document)
   return render(request, 'update.html', {'form': form,'edit': 'true'})

def update_prosedur(request, id):
   document = get_object_or_404(Prosedur, pk=id)
   if request.method == 'POST':
        form = ProsedurForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
            
           
   else:
        form = ProsedurForm(instance=document)
   return render(request, 'update.html', {'form': form})

def update_liste(request, id):
   document = get_object_or_404(Liste, pk=id)
   if request.method == 'POST':
        form = ListeForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
   else:
        form = ListeForm(instance=document)
   return render(request, 'update.html', {'form': form})

def update_form(request, id):
     document = get_object_or_404(Form, pk=id)
     if request.method == 'POST':
        form = FormForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
     else:
        form = FormForm(instance=document)
     return render(request, 'update.html', {'form': form})

def update_tablo(request, id):
   document = get_object_or_404(Tablo, pk=id)
   if request.method == 'POST':
        form = TabloForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
   else:
        form = TabloForm(instance=document)
   return render(request, 'update.html', {'form': form})

def update_talimat(request, id):
   document = get_object_or_404(Talimat, pk=id)
   if request.method == 'POST':
        form = TalimatForm(request.POST, instance=document)
        if form.is_valid():
            
            document.revision_date = timezone.now()
            document.revision_number += 1
            form.save()
            return redirect('show')
   else:
        form = TalimatForm(instance=document)
   return render(request, 'update.html', {'form': form})

def index(request):
    return render(request,'index.html')

def my_view(request):
   data = Model.objects.all()
   context = {'politika': data}
   return render(request, 'template.html', context)


