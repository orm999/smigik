# -*- coding: utf-8 -*-
import urllib

from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template.loader import render_to_string
from django.utils import simplejson

from dev_info.models import InputDev, OutputDev
from dev_info.forms import InputDevForm, OutputDevForm

def index( request ):
    if request.is_ajax():
        input_dev_list = InputDev.objects.all()
        output_dev_list = OutputDev.objects.all()
        type = request.GET.get( 'type', 'input' )
        html = render_to_string( 'dev_info/_list.html',
            {'type': type, 'input_dev_list': input_dev_list,
             'output_dev_list': output_dev_list}
        )
        response = simplejson.dumps( {'success': 'True', 'html': html} )
        return HttpResponse( response, content_type='application/javascript' )
    else:
        c = csrf( request )
        return render_to_response( 'dev_info/base_index.html', c )

def add( request ):
    if request.method == 'POST':
        type = request.POST.get( 'type', 'input' )
        url = request.POST.get( 'form', '' )
        unq_url = urllib.unquote( str( url ) )
        query = QueryDict( unq_url )
        if type == 'input':
            form = InputDevForm( query )
        elif type == 'output':
            form = OutputDevForm( query )

        if form.is_valid():
            cd = form.cleaned_data
            if type == 'input':
                dev = InputDev( model=cd['model'],
                               expl_start_date=cd['expl_start_date'],
                               scan_mode=cd['scan_mode'] )
            elif type == 'output':
                dev = OutputDev( model=cd['model'],
                                expl_start_date=cd['expl_start_date'],
                                cartridge_id=cd['cartridge_id'],
                                print_mode=cd['print_mode'] )
            dev.save()
            if type == 'input':
                row = getInputRow( dev )
            elif type == 'output':
                row = getOutputRow( dev )
            notice = 'Устройство №{0} было добавлено'.format( dev.dev_id )
            response = simplejson.dumps( {'success': 'True', 'notice': notice, 'row': row} )
        else:
            errors = form.errors.as_ul()
            response = simplejson.dumps( {'success': 'False', 'errors': errors} )
    else:
        type = request.GET.get( 'type', 'input' )
        if type == 'input':
            form = InputDevForm()
        elif type == 'output':
            form = OutputDevForm()
        html = render_to_string( '_form.html', {'id': 'add_dev', 'form': form,
            'submit_val': 'Добавить', 'legend': 'Добавить устройство ' + dev_type( type )} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        return HttpResponse( response, content_type='application/javascript' )

def edit( request ):
    if request.method == 'POST':
        type = request.POST.get( 'type', 'input' )
        dev_id = request.POST.get( 'dev_id' )
        url = request.POST.get( 'form', '' )
        unq_url = urllib.unquote( str( url ) )
        query = QueryDict( unq_url )
        if type == 'input':
            form = InputDevForm( query )
        elif type == 'output':
            form = OutputDevForm( query )

        if form.is_valid():
            cd = form.cleaned_data
            if type == 'input':
                dev = InputDev.objects.get( dev_id=dev_id )
                dev.model = cd['model']
                dev.expl_start_date = cd['expl_start_date']
                dev.scan_mode = cd['scan_mode']
            elif type == 'output':
                dev = OutputDev.objects.get( dev_id=dev_id )
                dev.model = cd['model']
                dev.expl_start_date = cd['expl_start_date']
                dev.cartridge_id = cd['cartridge_id']
                dev.print_mode = cd['print_mode']
            dev.save()
            if type == 'input':
                row = getInputRow( dev )
            elif type == 'output':
                row = getOutputRow( dev )
            notice = 'Данные об устройство №{0} были изменены'.format( dev.dev_id )
            response = simplejson.dumps( {'success': 'True', 'notice': notice, 'row': row} )
        else:
            errors = form.errors.as_ul()
            response = simplejson.dumps( {'success': 'False', 'errors': errors} )
    else:
        type = request.GET.get( 'type', 'input' )
        dev_id = request.GET.get( 'dev_id' )
        if dev_id:
            if type == 'input':
                dev = InputDev.objects.get( dev_id=dev_id )
                form = InputDevForm( 
                    initial={'model': dev.model, 'expl_start_date': dev.expl_start_date,
                             'scan_mode': dev.scan_mode}
                )
            elif type == 'output':
                dev = OutputDev.objects.get( dev_id=dev_id )
                form = OutputDevForm( 
                    initial={'model': dev.model, 'expl_start_date': dev.expl_start_date,
                             'cartridge_id': dev.cartridge_id, 'print_mode': dev.print_mode}
                )
        else:
            return HttpResponseRedirect( '/dev_info/' )
        html = render_to_string( '_form.html', {'id': 'edit_dev', 'form': form,
            'submit_val': 'Обновить', 'legend': 'Редактировать устройство ' + dev_type( type )} )
        response = simplejson.dumps( {'success': 'True', 'html': html} )

    if request.is_ajax():
        return HttpResponse( response, content_type='application/javascript' )

def delete( request ):
    if request.method == 'POST':
        type = request.POST.get( 'type' )
        dev_id = request.POST.get( 'dev_id' )
        if dev_id:
            if type == 'input':
                try:
                    InputDev.objects.get( dev_id=dev_id ).delete()
                    response = 'Устройство ввода №{0} удалено'.format( dev_id )
                except Exception as e:
                    print( e )
                    response = 'Не удалось удалить устройство ввода №{0}'.format( dev_id )
            elif type == 'output':
                try:
                    OutputDev.objects.get( dev_id=dev_id ).delete()
                    response = 'Устройство вывода №{0} удалено'.format( dev_id )
                except Exception as e:
                    print( e )
                    response = 'Не удалось удалить устройство вывода №{0}'.format( dev_id )

    if request.is_ajax():
        return HttpResponse( response )

def getInputRow( dev ):
    row = u'''<tr id="{0}">
                 <td><input id="{0}" class="input" type="checkbox"></input></td>
                 <td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
                 <td><a href="" id="{0}" class="input edit">Редактировать</a>
                 <a href="" id="{0}" class="input delete">Удалить</a></td>
             </tr>'''.format( dev.dev_id, dev.model, dev.expl_start_date, dev.scan_mode )
    return row

def getOutputRow( dev ):
    row = u'''<tr id="{0}">
                 <td><input id="{0}" class="output" type="checkbox"></input></td>
                 <td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
                 <td>{4}</td>
                 <td><a href="" id="{0}" class="output edit">Редактировать</a>
                 <a href="" id="{0}" class="output delete">Удалить</a></td>
             </tr>'''.format( dev.dev_id, dev.model, dev.expl_start_date,
                              dev.cartridge_id, dev.print_mode )
    return row

def dev_type( type ):
    if type == 'input':
        return 'ввода'
    elif type == 'output':
        return 'вывода'
