#!/bin/python3
#Caleb Roberts
#7/11/2023
from geoip import geolite2 as gl
import datetime as dt
import os
import re


filename = 'example.log'
log = open(filename,'r')
log2 = open(filename,'r')
lines = log.readlines()
logTxt = log2.read()
ipList = []

#Creating a list of IPs from failed login attempts
for i in lines:
 if(i.find('Failed password for')>0):
  temp = i[:len(i)-17]
  L = temp.split()
  ip = L[len(L)-1]
  if(ipList.count(ip)<=0):
   ipList.append(ip)


#Starting Interface
os.system('clear')
print("\033[32m\033[1m\tAttacker Report\033[0m - "+str(dt.date.today()))
print("\033[31mCOUNT\tADDRESS\t\tCOUNTRY\033[0m")

for i in ipList:
 loc = gl.lookup(i)
 if loc is not None:
  x = re.findall(i,logTxt)
  if(len(x)>=10):
   print(str(len(x))+'\t'+str(i)+'\t'+loc.country)

