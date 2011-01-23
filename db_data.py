from dev_info.models import *

def fill_input_db():
	for i in range( 10 ):
		dev = InputDev( model='model {0}'.format( i ), expl_start_date='2001-1-1', scan_mode='{0}'.format( i ) )
		dev.save()

def fill_output_db():
	for i in range( 10 ):
		dev = OutputDev( model='model {0}'.format( i ), expl_start_date='2001-1-1', cartridge_id='{0}'.format( i ), print_mode='colored' )
		dev.save()
