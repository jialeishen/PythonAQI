#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import re

aqi=open('aqidata.txt','w')

months=['201312','201401','201402','201403','201404','201405','201406','201407','201408','201409','201410','201411','201412','201501','201502','201503','201504','201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611']

for month in months:
    print(month)
    city='南京'
    url='http://www.aqistudy.cn/historydata/daydata.php?city='+city+'&month='+str(month)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('</tr>.*?<tr>.*?<td align="center">(.*?)</td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?',re.S)
    items = re.findall(pattern,content)
    for item in items:
        date=str(item[0])
        ozone=str(item[4])
        aqi.write(date+' '+ozone+'\n')

aqi.close()

print('Finished!')

