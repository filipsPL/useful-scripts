#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string
import numpy as np
import time

today = str(time.strftime("%Y-%m-%d"))
todayURL = str(time.strftime("%d-%m-%Y"))

# --------------- dump -------------------- #

import os
# URL of your localization here. To get from: http://sojp.wios.warszawa.pl/index.php?page=raport-godzinowy
url = "http://sojp.wios.warszawa.pl/?page=raport-godzinowy&data=%s&site_id=13&csq_id=1414&dane=w1" % todayURL
cmd = os.popen("lynx -dump '%s'" % url)
raw = cmd.read()
cmd.close()

#print url

# ----------- processing ------------------- #

for line in raw.split('\n'):
#    print line
    line = re.sub(' +',' ',line.strip())
    if re.search('^Data, godzina', line) :
        head=string.split(line, " ")
    if re.search(today, line) :
        values_tmp=string.split(line, " ")
        if len(values_tmp) > 2:
           values = values_tmp

'''
['Data,', 'godzina', 'PM10', 'SO2', 'NO2', 'O3', 'PM25']
['2014-12-16', '09:00', '35.5', '7.6', '32.2', '4.2', '32.3']
'''

binsPM10=np.array([0, 50, 100, 150, 200])
x = np.array([float(values[2])])
binPM10 = int(np.digitize(x, binsPM10))

binsPM25=np.array([0, 25, 50, 75, 100])
x = np.array([float(values[6])])
binPM25 = int(np.digitize(x, binsPM25))

#print values[0:2]
print "PM10:  ", values[2], binPM10
print "PM2.5: ", values[6], binPM25
