#!/usr/bin/python

import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('exe', choices=['adb', 'fastboot'], help='Executable to use.')
parser.add_argument('args', nargs='*', help='Arguments for adb or fastboot.')

args = parser.parse_args()

devices = []
for line in subprocess.check_output('%s devices' % (args.exe), shell=True).split('\n'):
  line = line.strip()
  if len(line) > 0 and line[0].isdigit():
    devices.append(line.split()[0])

print '============================================'
print 'Devices detected: \n%s' % ('\n'.join(devices))
print '============================================'

for d in devices:
  subprocess.check_call('%s -s %s %s' % (args.exe, d, ' '.join(args.args)), shell=True)
