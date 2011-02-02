# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm
import os


class Ph( models.Model ):
    path = ''
    ph_id = models.AutoField( primary_key=True )
    publication_date = models.DateField( auto_now_add=True )
    fam = models.CharField( max_length=50 )
    ija = models.CharField( max_length=50 )
    otch = models.CharField( max_length=40 )
    pser = models.CharField( max_length=4 )
    pnom = models.CharField( max_length=6 )
    vidan = models.CharField( max_length=100 )
    dvidan = models.DateField()
    tip_foto = models.CharField( max_length=40 )
    im = models.ImageField( upload_to='media' )

    class Meta:
	ordering = ['-ph_id']


def pu( path ):
    return path

