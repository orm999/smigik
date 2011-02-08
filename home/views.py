from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

def index( request ):
    if request.is_ajax():
        if request.method == 'POST':
            who = request.POST.get( 'who' )
            print( who )
            if who == 'user':
                html = render_to_string( 'home/_user.html' )
            if who == 'operator':
                html = render_to_string( 'home/_operator.html' )
            if who == 'admin':
                html = render_to_string( 'home/_admin.html' )
            response = simplejson.dumps( {'success': 'True', 'html': html} )
            return HttpResponse( response )
    return render_to_response( 'home/base_index.html' )
