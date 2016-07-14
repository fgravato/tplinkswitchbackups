#!/usr/bin/env python
# Quick Switch Backup for TP or Switches that don't work in Rancid
# Created by Frank Gravato - Continuous Networks

import sys,pexpect
import getpass
import time
import datetime
import fnmatch
import os
import shutil

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)

HOST = '172.1.205.7'
user = 'admin'
password = '****'
TFTPSERVER = '172.1.202.107'

child = pexpect.spawn ('telnet '+HOST) #start telnet session in switch
child.timeout = 30
child.logfile = sys.stdout #display progress of script on screm

time.sleep(5)

child.expect ('User:') #wait user

child.sendline (user+'\r') #send user

child.expect('Password:') #wait password

child.sendline (password+'\r') #send password

child.expect(' admin on vty0 ')

child.sendline ('\r')
time.sleep(2)

child.sendline  ('\r')
time.sleep(5)


child.sendline (' enable\n'+'\r') #change mode to enable mode

child.expect('#') #wait # enable mode

child.sendline ('copy startup-config tftp ip-address '+TFTPSERVER+' filename '+timestamp+'-bksw-'+HOST+ '\r') #send command to upload startup-config to TFTP server
time.sleep(5)

child.sendline ('logout \r') #exit switch console