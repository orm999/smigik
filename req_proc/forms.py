# -*- coding: utf -*-
from django import forms

from dev_info.models import OutputDev

class ImgMarkedForm( forms.Form ):
    img = forms.ImageField( label='Изображение' )

class CertCreatedForm( forms.Form ):
    model = forms.ModelChoiceField( queryset=OutputDev.objects.values_list( 'model', flat=True ),
                                    label='Модель' )
    cartridge_id = forms.ModelChoiceField( queryset=OutputDev.objects.values_list( 'cartridge_id', flat=True ),
                                           label='Номер катриджа' )
    print_mode = forms.ModelChoiceField( queryset=OutputDev.objects.values_list( 'print_mode', flat=True ),
                                         label='Режим печати' )
    cert = forms.FileField( label='Сертификат' )
