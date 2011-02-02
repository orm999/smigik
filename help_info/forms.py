# -*- coding: utf-8 -*-
from django import forms
#from django.forms import ModelForm
#from prog.views import Ph 


class PhForms(forms.Form):
	#title = forms.CharField(max_length=100, label='Описание')
	fam = forms.CharField(max_length=50, label='Фамилия')
        ija = forms.CharField(max_length=50, label='Имя')
        otch = forms.CharField(max_length=40, label='Отчество')
        pser = forms.CharField(max_length=4, label='Паспорт: серия')
        pnom = forms.CharField(max_length=6, label='Паспорт: номер')
        vidan = forms.CharField(max_length=100, label='Кем выдан')
        dvidan = forms.DateField(label='Дата выдачи')
        tip_foto = forms.ChoiceField(widget = forms.Select(), 
              choices = ([('Пейзаж','Пейзаж'), ('Портрет','Портрет'),('Другое','Другое'), ]), initial='', label='Тип изображения', required = True,) 
     	im = forms.FileField(label='Изображение')
      
        #class Meta:
         #   model = Ph 

#  Tip_Foto = forms.ChoiceField(widget = forms.Select(), 
#              choices = ([('1','1'), ('2','2'),('3','3'), ]), initial='', required = True,) 
 
