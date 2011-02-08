# -*- coding: utf-8 -*-

from django import forms


class PhForms(forms.Form):
	fam = forms.CharField(max_length=50, label='Фамилия')
        imja = forms.CharField(max_length=50, label='Имя')
        otch = forms.CharField(max_length=40, label='Отчество')
        datroj = forms.DateField(label='Дата рождения')
        pser = forms.IntegerField(max_value=9999, label='Паспорт: серия')
        pnom = forms.IntegerField(max_value=999999, label='Паспорт: номер')
        vidan = forms.CharField(max_length=100, label='Кем выдан')
        dvidan = forms.DateField(label='Дата выдачи')
        adres = forms.CharField(max_length=200, label='Адрес')
        nazvim = forms.CharField(max_length=40, label='Название изображения')
        tip_foto = forms.ChoiceField(widget = forms.Select(), 
              choices = ([('Пейзаж','Пейзаж'), ('Портрет','Портрет'),('Другое','Другое'), ]), initial='', label='Тип изображения', required = True,) 
     	im = forms.ImageField(label='Изображение')
      
class ValForm(forms.Form):
	txt = forms.CharField(max_length=50, label='Фамилия')
        

class VvForm(forms.Form):
	nazvim = forms.CharField(max_length=40, label='Название изображения')
        tip_foto = forms.ChoiceField(widget = forms.Select(), 
              choices = ([('Пейзаж','Пейзаж'), ('Портрет','Портрет'),('Другое','Другое'), ]), initial='', label='Тип изображения', required = True,) 
     	im = forms.ImageField(label='Изображение')
