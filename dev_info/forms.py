# -*- coding: utf -*-
from django import forms

class InputDevEditForm( forms.Form ):
    model = forms.CharField( max_length=255, label='Модель' )
    expl_start_date = forms.DateField( label='Дата начала эксплуатации' )
    scan_mode = forms.CharField( max_length=255, label='Режим сканирования' )

class OutputDevEditForm( forms.Form ):
    model = forms.CharField( max_length=255, label='Модель' )
    expl_start_date = forms.DateField( label='Дата начала эксплуатации' )
    cartridge_id = forms.IntegerField( label='Номер картриджа' )
    print_mode = forms.CharField( max_length=255, label='Режим печати' )

