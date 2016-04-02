#!/usr/bin/env python3

from distutils.core import setup

def readme():
    with open('README.txt') as f:
        return f.read()

setup(name='playlistexport',
	version='0.3.1',
	description='Export playlists while maintaining directory hierarchy',
	long_description=readme(),
	author='Pierce Putz',
	author_email='putzpie@gmail.com',
	maintainer='Pierce Putz',
	maintainer_email='putzpie@gmail.com',
	url='tobemade',
	license='GPLv3',
	keywords=['playlist','copy','transfer'],
	classifiers=['Development Status :: 3 - Alpha',
				'Environment :: Console',
				'Intended Audience :: End Users/Desktop',
				('License :: OSI Approved :: GNU General Public' + 
				' License v3 (GPLv3)'),
				'Natural Language :: English',
				'Operating System :: OS Independent',
				'Programming Language :: Python :: 3',
				'Topic :: System :: Archiving :: Backup'],
	packages=['playlistexport'])
				
	
