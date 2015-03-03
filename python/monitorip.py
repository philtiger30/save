#! /usr/bin/python
#coding=utf-8
#file: monitorip
#author: lin bi

from __future__ import division
import sys
import os
import time
import signal

netcmd = 'ifconfig eth0|grep bytes'
#print netcmd

def getnetio(line):
    s1=line.find('RX bytes:')+9
    e1=line.find(' ',s1)
    print "s1 is %s"%s1
    print "e1 is %s"%e1
    neti=line[s1:e1]
    s2=line.find('TX bytes:')+9
    e2=line.find(' ',s2)
    neto=line[s2:e2]
    return (int(neti),int(neto))

def int_handler(signum, frame):
    print ""
    sys.exit()

signal.signal(signal.SIGINT, int_handler)

line=os.popen(netcmd)
netio=getnetio(line)
print 'The 1st netio is next line:'
print netio
neti_start=netio[0]
neto_start=netio[1]
time_start=time.time()
count=60

