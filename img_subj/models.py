from django.db import models

class ImgSubj( models.Model ):
    subj_id = models.AutoField( primary_key=True )
    subject = models.CharField( max_length=255, unique=True )
