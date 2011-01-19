from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from dev_info.models import InputDev
from dev_info.models import OutputDev

from dev_info.forms import InputDevInfoForm
from dev_info.forms import OutputDevInfoForm

def add( request ):
    type = 'input'
    if request.method == 'POST':
        if type == 'input':
            form = InputDevInfoForm( request.POST )
        elif type == 'output':
            form = OutputDevInfoForm( request.POST )

        if form.is_valid():
            cd = form.cleaned_data
            if type == 'input':
                dev = InputDev( model=cd['model'],
                               expl_start_date=cd['expl_start_date'],
                               scan_mode=cd['scan_mode'] )
                print( dev.dev_id )
            elif type == 'output':
                dev = OutputDev( model=cd['model'],
                                expl_start_date=cd['expl_start_date'],
                                cartridge_id=cd['cartridge_id'],
                                print_mode=cd['print_mode'] )
            dev.save()
            print( dev.dev_id )
            return HttpResponseRedirect( '/dev_info/' )
    else:
        if type == 'input':
            form = InputDevInfoForm()
        elif type == 'output':
            form = OutputDevInfoForm()

    c = {'form': form}
    c.update( csrf( request ) )
    return render_to_response( 'dev_info/base_dev_info_add.html', c )

def edit( request, type, dev_id ):
    if request.method == 'POST':
        if type == 'input':
            form = InputDevInfoForm( request.POST )
        elif type == 'output':
            form = OutputDevInfoForm( request.POST )

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
            return HttpResponseRedirect( '/dev_info/{0}/{1}/updated/'.format( type, dev_id ) )
    else:
        if type == 'input':
            try:
                dev = InputDev.objects.get( dev_id=dev_id )
                form = InputDevInfoForm( 
                    initial={'model': dev.model, 'expl_start_date': dev.expl_start_date, 'scan_mode': dev.scan_mode}
                )
            except InputDev.DoesNotExist:
                return HttpResponseRedirect( '/dev_info/' )
        elif type == 'output':
            try:
                dev = OutputDev.objects.get( dev_id=dev_id )
                form = OutputDevInfoForm( 
                    initial={'model': dev.model, 'expl_start_date': dev.expl_start_date, 'cartridge_id': dev.cartridge_id, 'print_mode': dev.print_mode}
                )
            except OutputDev.DoesNotExist:
                return HttpResponseRedirect( '/dev_info/' )

    c = {'form': form}
    c.update( csrf( request ) )
    return render_to_response( 'dev_info/base_dev_info_edit.html', c )

def updated( request, type, dev_id ):
    if type == 'input':
        dev = InputDev.objects.get( dev_id=dev_id )
    elif type == 'output':
        dev = OutputDev.objects.get( dev_id=dev_id )
    return render_to_response( 'dev_info/base_dev_info_updated.html', {'type': type, 'dev': dev} )
