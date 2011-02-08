# -*- coding: utf-8 -*-

import os
import urllib

from settings import MEDIA_ROOT

from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

from req_proc.models import ImgMarked, CertCreated
from req_proc.forms import ImgMarkedForm, CertCreatedForm

def index( request ):
    file_list = []
    path = os.path.join( __file__, os.pardir, MEDIA_ROOT, 'smigik/users' )
    for root, dirs, files in os.walk( path ):
        if os.path.basename( root ) == 'requests':
            req_nums = [os.path.splitext( req )[0] for req in files]
            file_list.append( req_nums )
    flat_file_list = sum( file_list, [] )

    form = CertCreatedForm( request.POST )

    if form.is_valid():
        cd = form.cleaned_data
        print( cd )

    return render_to_response( 'req_proc/base_index.html', {'req_list': flat_file_list, 'form': form} )

def upload_img( request ):
    print( request.method )
    if request.method == 'POST':
        url = request.POST.get( 'form', '' )
        unq_url = urllib.unquote( str( url ) )
        query = QueryDict( unq_url )
        print( query )
        form = ImgMarkedForm( query )

        if form.is_valid():
            cd = form.cleaned_data
            print( cd )

            img = ImgMarked()
            img.save()

#        notice = 'Изображение {0} загружено'.format( img )
        response = '<textarea>' + simplejson.dumps( {'success': 'True', 'notice': 'hi', 'html': 'hi', 'error': 'errors'} ) \
            + '</textarea>'
    else:
        form = ImgMarkedForm()
        html = render_to_string( '_form.html', {'id': 'upload_img', 'form': form,
            'submit_val': 'Изображение промаркировано', 'legend': 'Загрузить изображение'} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        print( response )
        return HttpResponse( response, content_type='application/javascript' )
    else:
        assert False

def upload_cert( request ):
    if request.method == 'POST':
        response = simplejson.dumps( {'success': 'True', 'html': 'hi'} )
    else:
        form = CertCreatedForm()
        html = render_to_string( '_form.html', {'id': 'upload_cert', 'form': form,
            'submit_val': 'Сертификат сформирован'} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        return HttpResponse( response, content_type='application/javascript' )
