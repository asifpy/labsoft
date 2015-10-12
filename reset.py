#!/usr/bin/env python

import os
import sys

# setup the environment
SETTINGS = 'labsoft.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = SETTINGS

def cmd(txt):
    os.system(txt)

def actions(cmds):
    for c in cmds:
        cmd(c)

def start():
    actions([
        #'dropdb labsoft',
        'rm labsoft/labsoft.db',
        'sleep 1',
        #'createdb labsoft',
        './manage.py makemigrations',
        './manage.py migrate',
        './manage.py createsuperuser --username=sa --email=sa@me.org',
    ])

# def run_sample_data():
#     cmd('python sample_data.py')

def main():
    start()
    #run_sample_data()

if __name__ == '__main__': main()

