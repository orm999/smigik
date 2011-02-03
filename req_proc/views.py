import os

from settings import MEDIA_ROOT

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

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
    if request.method == 'POST':
        response = simplejson.dumps( {'success': 'True', 'html': 'hi'} )
    else:
        form = ImgMarkedForm()
        html = render_to_string( 'req_proc/_upload_img.html', {'form': form} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        return HttpResponse( response, content_type='application/javascript' )

def upload_cert( request ):
    if request.method == 'POST':
        response = simplejson.dumps( {'success': 'True', 'html': 'hi'} )
    else:
        form = CertCreatedForm()
        html = render_to_string( 'req_proc/_upload_cert.html', {'form': form} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        return HttpResponse( response, content_type='application/javascript' )
