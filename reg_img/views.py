# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template.loader import render_to_string
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist

import os
import re
import random

from settings import MEDIA_ROOT

from reg_img.models import Ph

from reg_img.forms import PhForms, ValForm, VvForm


def fwork1(cd, z):
         put = MEDIA_ROOT
         tz = cd['fam']
         path = put+'/'+tz
       
         if not os.path.isdir(path):
             os.mkdir(path)
             os.chdir(path)
             
         imname = str(z)+".bmp"
         w = cd['im']

         image = Image.open(w)
         image.save(imname)

         
         v = cd['fam']       
         filename = str(z)+".txt"
         f1 = open(filename, 'w')
         
         v = cd['fam']+' '+cd['imja']+' '+cd['otch']
         v = v.encode("utf-8")
         if not re.match(u"^[A-Za-z]+$", v):
             f1.write(v+'\n')

         v = cd['datroj']
         f1.write('Дата рождения: '+str(v)+'\n')

         v1 = cd['vidan']
         v1 = v1.encode("utf-8")
         v = str(cd['pser'])+' '+'№'+str(cd['pnom'])+' '+v1+' '+str(cd['dvidan'])
         f1.write(v+'\n')

         v = cd['adres']
         v = v.encode("utf-8")
         f1.write(v+'\n')

         v = cd['fam']
         v = v.encode("utf-8")
         ph = Ph.objects.filter(fam=v).latest('ph_id')   
         tv = ph.publication_date
         f1.write('Дата подачи заявки: '+str(tv)+'\n')
         
         v = cd['nazvim']
         v = v.encode("utf-8")
         f1.write('Название изображения: '+v+'\n')

         f1.write('Номер сертификата: '+str(z)+'\n')
         
         f1.write(u'&'+'\n')
         f1.close()
         os.chdir(put)
         return 'h'

        
def ph_add(request):
 put = MEDIA_ROOT   
 form = VvForm()
 c = csrf(request)
 if request.method == 'POST':
     type = request.POST.get('type', 'input')
     ph_id = request.POST.get('ph_id')
     if type =='input':
         form = VvForm(request.POST, request.FILES)
     if form.is_valid():
         cd = form.cleaned_data
         tf = glob
         ph = Ph.objects.get(fam=tf)
         path = put+'/'+glob
       
         if  os.path.isdir(path):
             os.chdir(path)

         ph.nsert = ph.nsert+1
         z = ph.im
         ph.im = cd['nazvim']+'.bmp'

         z = ph.nsert
             
         imname = str(z)+".bmp"
         w = cd['im']

         image = Image.open(w)
         image.save(imname)

         filename = str(z)+".txt"
         f1 = open(filename, 'w')

         z = ph.nazvim
         ph.nazvim = cd['nazvim']
         z = ph.tip_foto
         ph.tip_foto = cd['tip_foto']


         v = ph.fam+' '+ph.imja+' '+ph.otch 
         v = v.encode("utf-8")
         if not re.match(u"^[A-Za-z]+$", v):
             f1.write(v+'\n')

         v = ph.datroj
         f1.write('Дата рождения: '+str(v)+'\n')

         v1 = ph.vidan
         v1 = v1.encode("utf-8")
         v = str(ph.pser)+' '+'№'+str(ph.pnom)+' '+v1+' '+str(ph.dvidan)
         f1.write(v+'\n')

         v = ph.adres
         v = v.encode("utf-8")
         f1.write(v+'\n')

         #v = cd['fam']
         #v = v.encode("utf-8")
         #ph = Ph.objects.filter(fam=v).latest('ph_id')   
         tv = ph.publication_date
         f1.write('Дата подачи заявки: '+str(tv)+'\n')
         
         v = ph.nazvim
         v = v.encode("utf-8")
         f1.write('Название изображения: '+v+'\n')

         z = ph.nsert
         f1.write('Номер сертификата: '+str(z)+'\n')
         
         f1.write(u'&'+'\n')
         f1.close()
         
         ph.save()

         os.chdir(put)
         message = 'Ваша заявка была принята'
         return HttpResponse(message)
 c.update( {'form': form} )
 return render_to_response('reg_img/ph_add_inf.html', c)


def valid(request):
 global glob
 form = ValForm()
 c = csrf(request)
 if request.method == 'POST':
     type = request.POST.get('type', 'input')
     ph_id = request.POST.get('ph_id')
     if type =='input':
         form = ValForm(request.POST)
     if form.is_valid():
         cd = form.cleaned_data
         tf = cd['txt']
         if Ph.objects.filter(fam=tf):
             glob = tf
             return HttpResponseRedirect( '/reg_img/ph_add_inf/' )             
         else:
             return HttpResponseRedirect( '/reg_img/add_inf/' )
 c.update( {'form': form} )
 return render_to_response('reg_img/first.html', c)


def albumentry(request):
 form = PhForms()
 c = csrf(request)
 if request.method == 'POST':
     type = request.POST.get('type', 'input')
     ph_id = request.POST.get('ph_id')
   
     if type =='input':
         form = PhForms(request.POST, request.FILES)
     if form.is_valid():
         cd = form.cleaned_data
         
         try:
             v = cd['fam']
             v = v.encode("utf-8")
             ph = Ph.objects.latest('ph_id')
             z = ph.nsert+1
         except ObjectDoesNotExist:
             z = 1
                          
         p = Ph(fam=cd['fam'], imja=cd['imja'], otch=cd['otch'], datroj=cd['datroj'],
                pser=cd['pser'], pnom=cd['pnom'], vidan=cd['vidan'], dvidan=cd['dvidan'],
                adres=cd['adres'], nsert=z, nazvim=cd['nazvim'],
                tip_foto=cd['tip_foto'],im=cd['nazvim']+'.bmp')
         p.save()

         fwork1(cd, z)
         
         #return HttpResponseRedirect( '/index/' )
         message = 'Ваша заявка была принята'
         return HttpResponse(message)
        
 c.update( {'form': form} )
 return render_to_response('reg_img/add_inf.html', c)

