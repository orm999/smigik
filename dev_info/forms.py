# -*- coding: utf -*-
from django import forms

class InputDevForm( forms.Form ):
    model = forms.CharField( max_length=255, label='Модель' )
    expl_start_date = forms.DateField( label='Дата начала эксплуатации (гггг-мм-дд)' )
    scan_mode = forms.CharField( max_length=255, label='Режим сканирования' )

class OutputDevForm( forms.Form ):
    model = forms.CharField( max_length=255, label='Модель' )
    expl_start_date = forms.DateField( label='Дата начала эксплуатации (гггг-мм-дд)' )
    cartridge_id = forms.IntegerField( label='Номер картриджа' )
    print_mode = forms.CharField( max_length=255, label='Режим печати' )
