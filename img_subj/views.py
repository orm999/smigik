# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from img_subj.models import ImgSubj
from img_subj.forms import ImgSubjForm

JS = ''

def index( request ):
    global JS

    if request.is_ajax():
        print( '1' )
        if request.method == 'POST':
            subj_id = request.POST.get( 'subj_id' )
            subject = request.POST.get( 'subject' )
            JS = request.POST.get( 'JS', '' )

            if subject:
                if subj_id:
                    subj = ImgSubj.objects.get( subj_id=subj_id )
                    old_subject = subj.subject
                    subj.subject = subject
                    msg = 'Тематика "{0}" изменена на "{1}"'.format( old_subject, subject )
                else:
                    subj = ImgSubj( subject=subject )
                    subj.save()
                    msg = 'Тематика "{0}" добавлена'.format( subject )
                subj.save()
                option = genOption( subj.subj_id, subj.subject )
            else:
                try:
                    subj = ImgSubj.objects.get( subj_id=subj_id )
                    msg = 'Тематика "{0}" удалена'.format( subj.subject )
                    subj.delete()
                except ImgSubj.DoesNotExist as e:
                    msg = 'Такой тематики нет!'
                option = ''

            response = simplejson.dumps( {'msg': msg, 'option': option} )
            print( msg, option )
            return HttpResponse( response )
    else:
        print( '2' )
        form = ImgSubjForm()
        subj_img_list = ImgSubj.objects.all()
        return render_to_response( 'img_subj/base_index.html',
            {'JS': JS, 'form': form, 'subj_img_list': subj_img_list}
        )

def genOption( id, subject ):
    return '<option id="{0}">{1}</option>'.format( id, subject )
