# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from img_subj.models import ImgSubj
from img_subj.forms import ImgSubjForm


def index( request ):
    if request.is_ajax():
        if request.method == 'POST':
            subj_id = request.POST.get( 'subj_id' )
            subject = request.POST.get( 'subject' )
            print( subj_id, subject )
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
        form = ImgSubjForm()
        subj_img_list = ImgSubj.objects.all()
        return render_to_response( 'img_subj/base_img_subj.html',
            {'form': form, 'subj_img_list': subj_img_list}
        )

def genOption( id, subject ):
    return '<option id="{0}">{1}</option>'.format( id, subject )
