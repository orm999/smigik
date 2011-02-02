from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

import os

def index( request ):
    file_list = []
    print( __file__ )
    print( os.path.join( os.path.dirname( __file__ ), '../media/files/users' ) )
    print( os.path.exists( os.path.join( os.path.dirname( __file__ ), '../media/files/users' ) ) )
    for root, dirs, files in os.walk( os.path.join( os.path.dirname( __file__ ), '../media/files/users' ) ):
        print( root )
        print( dirs )
        print( files )
        file_list.append( files )
    return render_to_response( 'req_proc/base_index.html', {'req_list': file_list} )
