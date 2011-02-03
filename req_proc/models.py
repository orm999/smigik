from django.db import models

class ImgMarked( models.Model ):
    img_id = models.AutoField( primary_key=True )
    img = models.ImageField( upload_to='img' )

class CertCreated( models.Model ):
    cert_id = models.AutoField( primary_key=True )
    model = models.ForeignKey( 'dev_info.OutputDev',
        related_name='%(app_label)s_%(class)s_model' )
    cartridge_id = models.ForeignKey( 'dev_info.OutputDev',
        related_name='%(app_label)s_%(class)s_cartridge_id' )
    print_mode = models.ForeignKey( 'dev_info.OutputDev',
        related_name='%(app_label)s_%(class)s_print_mode' )
    cert = models.FileField( upload_to='cert' )
