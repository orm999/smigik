# -*- coding: utf -*-
from django import forms

class ImgSubjForm( forms.Form ):
    subject = forms.CharField( max_length=255, required=False, label='Тематика' )
