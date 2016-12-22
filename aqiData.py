#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import re
import csv

city='南京'
fname='aqidata'+city.decode('utf-8').encode('gb2312')+'.csv'
aqidata=file(fname,'wb')

writer=csv.writer(aqidata,delimiter=',',quoting=csv.QUOTE_ALL)
writer.writerow(['date','aqi','pm2.5','pm10','so2','co','no2','o3'])

months=['201312','201401','201402','201403','201404','201405','201406','201407','201408','201409','201410','201411','201412','201501','201502','201503','201504','201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611']

spring=['201403','201404','201405','201503','201504','201505','201603','201604','201605']
summers=['201406','201407','201408','201506','201507','201508','201606','201607','201608']
autumn=['201409','201410','201411','201509','201510','201511','201609','201610','201611']
winters=['201312','201401','201402','201412','201501','201502','201512','201601','201602','201612']

for month in months:
    url='http://www.aqistudy.cn/historydata/daydata.php?city='+city+'&month='+str(month)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('</tr>.*?<tr>.*?<td align="center">(.*?)</td>.*?<td align="center">(.*?) </td>.*?<td align="center" class="hidden-xs hidden-sm">.*?</td>.*?<td align="center">.*?<div style=.*?</div>.*?</td>.*?<td align="center">(.*?) </td>.*?<td align="center">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?<td align="center" class="hidden-xs">(.*?) </td>.*?',re.S)
    items = re.findall(pattern,content)
    for item in items:
        date=str(item[0])
        aqi=str(item[1])
        pm25=str(item[2])
        pm10=str(item[3])
        so2=str(item[4])
        co=str(item[5])
        no2=str(item[6])
        o3=str(item[7])
        data=[(date,aqi,pm25,pm10,so2,co,no2,o3)]
        writer.writerows(data)
    print(month)

aqidata.close()

print('Finished!')
