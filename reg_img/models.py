# -*- coding: utf-8 -*-

from django.db import models
 
class Ph(models.Model):
    ph_id = models.AutoField(primary_key=True)
    publication_date = models.DateField(auto_now_add=True)
    fam = models.CharField(max_length=50)
    imja = models.CharField(max_length=50)
    otch = models.CharField(max_length=40)
    datroj = models.DateField()
    pser = models.IntegerField()
    pnom = models.IntegerField()
    vidan = models.CharField(max_length=150)
    dvidan = models.DateField()
    adres = models.CharField(max_length=200)
    nsert = models.IntegerField()
    nazvim = models.CharField(max_length=40)
    tip_foto = models.CharField(max_length=40)
    im = models.CharField(max_length=100)

    class Meta:
	ordering = ['-ph_id']

