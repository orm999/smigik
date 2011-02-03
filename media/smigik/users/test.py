#! /usr/bin/python
import random
import os

def files(dir):
	for root, dirs, files in os.walk(dir):
		for d in dirs:
			if d == 'requests':
				filename = str(random.randint(1, 10000)) + '.odt'
				path = root + '/' + d + '/' + filename
				with open(path, 'w') as f:
					f.write(filename)
files('.')
