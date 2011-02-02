# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template.loader import render_to_string
from PIL import Image

import os
import re
import StringIO

from help_info.models import Ph, pu

from help_info.forms import PhForms


kiril = ( 'А', 'а', 'Б' , 'б', 'В', 'в', 'Г', 'г', 'Д', 'д' , 'Е', 'е', 	'Ё', 'ё',
         'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м',
         'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у',
         'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ',
         'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я' )

path = ''
def albumentry( request ):
 form = PhForms()
 c = csrf( request )
 if request.method == 'POST':
     type = request.POST.get( 'type', 'input' )
     ph_id = request.POST.get( 'ph_id' )
     if type == 'input':
         form = PhForms( request.POST, request.FILES )
     if form.is_valid():
         cd = form.cleaned_data
         ph_id = Ph.objects.values( 'ph_id' )

       #  p = Ph(fam=cd['fam'], ija=cd['ija'], otch=cd['otch'], pser=cd['pser'],
              #  pnom=cd['pnom'], vidan=cd['vidan'], dvidan=cd['dvidan'],
              #  tip_foto=cd['tip_foto'],im=cd['im'])
         #p.save()

         v = cd['fam']
         path = "files/user/" + v
         os.mkdir( path )
         os.chdir( path )
         put( puth )

         p = Ph( fam=cd['fam'], ija=cd['ija'], otch=cd['otch'], pser=cd['pser'],
                pnom=cd['pnom'], vidan=cd['vidan'], dvidan=cd['dvidan'],
                tip_foto=cd['tip_foto'], im=cd['im'] )
         p.save()

         filename = v + ".txt"
         f1 = open( filename, 'w' )
         v = cd['fam']
         v = v.encode( "utf-8" )
         if re.match( u"^[A-Za-z]+$", v ):
             f1.write( v + '\n' )

         v = cd['ija']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )

         v = cd['otch']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )

         v = cd['pser']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )

         v = cd['pnom']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )


         v = cd['vidan']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )


         v = cd['dvidan']
         f1.write( str( v ) + '\n' )

         v = cd['tip_foto']
         v = v.encode( "utf-8" )
         f1.write( v + '\n' )
         f1.write( u'&' + '\n' )
         f1.close()

         v = cd['im']
         #im = im.encode('utf-8')
         #filename = self.get_source_filename()
        ## image = Image.open(z)

         #image.thumbnail(size, Image.ANTIALIAS)
         #image.save(os.path.join('1.bmp'))
         #imagef = Image.open(im)
         #photo.save(1.jpg, imagef)
        # f1.close()
        # ph = Ph.objects.get(ph_id=ph_id)
        # ph.publication_date = form.cleaned_data['publication_date'] #phf.publication_date #cd['publication_date']
        # ph.title = cd['title']
        # ph.im = cd['im']

         #v = cd['title']
         #for sv in v:
             #if re.match(u"^[A-Za-z]+$", u'sv'):
                #print sv       
        # filename = "1.txt"
         #os.mkdir(v)
         #createPath(“C:\Dir”)
         #if v not in kiril:
         #file = open(filename, 'w')
         #file.write(v)
         #file.close()

         #ph.save()
     #else:
         #print(form.errors.as_ul())
 c.update( {'form': form} )
 return render_to_response( 'albumentry.html', c )


   #if request.method =='POST':
   #  type = request.POST.get('type', 'input')
   #  ph_id = request.POST.get('ph_id')
   #  if type =='input':
   #      form = PhForms(request.POST)
   #  if form.is_valid():
   #      cd = form.cleaned_data
   #      if type == 'input':
   #          dev = Ph.objects.get(ph_id=ph_id)
   #          dev.publication_date = cd['publication_date']
   #          dev.title = cd['title']
   #          dev.im = cd ['im']
   #          return HttpResponseRedirect('/showalbumentry/%s' % albumEntry.key())
   #      dev.save()
   #  else:
   #      return render_to_response('albumentry.html', locals())


 #      albumentry = form.save()
 #  return HttpResponseRedirect('/showalbumentry/%s' % albumEntry.key())
 # else:
 #  return render_to_response('albumentry.html', locals())
 #else:
 #form = PhForms()
 #return render_to_response('albumentry.html', locals())



#def upload_photo(request):
 #   filename = request.FILES['image_file']['filename']
  #  content = request.FILES['image_file']['content']
   # return render_to_response('1.html')


#def search_form(request):
 #   return render_to_response('search_form.html')

#def search(request):
 #   if 'q' in request.GET:
  #      message = 'You searched for: %r' % request.GET['q']
   # else:
    #    message = 'You submitted an empty form.'
   # return HttpResponse(message)


