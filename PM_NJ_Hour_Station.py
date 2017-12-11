#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import re
import time as T
import csv

aqidata=file('PM_NJ_Hour_Station.txt','a')

writer=csv.writer(aqidata,delimiter=',',quoting=csv.QUOTE_ALL)
writer.writerow(['time','site','aqi','pm2.5','pm10'])

interval = 3600

while True:

    url='http://www.86pm25.com/city/nanjing.html'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern1 = re.compile('<td>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?',re.S)
    pattern2 = re.compile('<div class="remark">(.*?)</div>.*?',re.S)
    items = re.findall(pattern1,content)
    b = re.findall(pattern2,content)

    for item in items:
        
        time = b[0].encode('utf-8')
        site = item[0].encode('utf-8')
        aqi = item[1]
        pm25 = item[2].encode('utf-8')
        pm10 = item[3].encode('utf-8')
        data=[(time,site,aqi,pm25,pm10)]
        writer.writerows(data)
    print T.asctime( T.localtime(T.time()) )
    T.sleep(interval)  # Check interval, herein 10s

aqidata.close()




