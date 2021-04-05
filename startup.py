#!/usr/bin/python3

from subprocess import run
import sys

#parameters = sys.argv[1]

run(['service','cron','start'])

run(['nginx'])
