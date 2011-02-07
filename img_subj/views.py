# -*- coding: utf-8 -*-
#import urllib

from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.utils import simplejson

from img_subj.models import ImgSubj
from img_subj.forms import ImgSubjForm
from pickletools import optimize

def index( request ):
    if request.is_ajax():
        if request.method == 'POST':
            subj_id = request.POST.get( 'subj_id' )
            subject = request.POST.get( 'subject' )

            if subject:
                if subj_id != '0':
                    try:
                        subj = ImgSubj.objects.get( subj_id=subj_id )
                        old_subject = subj.subject
                        subj.subject = subject
                        subj.save()
                        msg = u'Тематика "{0}" изменена на "{1}"'.format( old_subject, subject )
                        option = genOption( subj )
                        action = 'updated'
                    except IndentationError:
                        msg = u'Тематика "{0}" уже добавлена'.format( subject )
                        option = ''
                        action = 'exists'
                else:
                    try:
                        subj = ImgSubj( subject=subject )
                        subj.save()
                        msg = u'Тематика "{0}" добавлена'.format( subject )
                        option = genOption( subj )
                        action = 'added'
                    except IntegrityError:
                        msg = u'Тематика "{0}" уже добавлена'.format( subject )
                        option = ''
                        action = 'exists'
            else:
                try:
                    subj = ImgSubj.objects.get( subj_id=subj_id )
                    msg = u'Тематика "{0}" удалена'.format( subj.subject )
                    subj.delete()
                    action = 'deleted'
                except ImgSubj.DoesNotExist as e:
                    msg = u'Такой тематики нет!'
                    action = 'doesnotexist'
                option = ''

            response = simplejson.dumps( {'action': action, 'msg': msg, 'option': option} )
            print( msg, option )
            return HttpResponse( response )
    else:
        form = ImgSubjForm()
        subj_img_list = ImgSubj.objects.all()
        return render_to_response( 'img_subj/base_index.html',
            {'form': form, 'subj_img_list': subj_img_list, 'legend': 'Тематики изображений'}
        )

def genOption( subj ):
    return u'<option id="{0}">{1}</option>'.format( subj.subj_id, subj.subject )
