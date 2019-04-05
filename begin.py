# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:18:45 2018

@author: admin
"""
#网站1 url需要加原网址
from urllib import request,parse
from bs4 import BeautifulSoup
import re
import pandas as pd 
import datetime
import requests
import xlwt
import random

name_sz = []
page_wd = []
date_rq = []
text_url = []

#深圳市经信委
url = 'http://www.szjmxxw.gov.cn/xxgk/xxgkml/qt/tzgg/'
#url_1 = 'http://www.szjmxxw.gov.cn/xxgk/xxgkml/qt/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szjmxxw.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text = response.read().decode('utf8')

pattern = re.compile('<li><span>(.*?)</span><.*?\.(.*?)\" target.*?>(.*?)</a></li>',re.S)
results = re.findall(pattern,text)
text_url_1 = []
for i in results:
    #page_wd.append(i[2])
    date_rq.append(i[0])
    text_url.append('http://www.szjmxxw.gov.cn/xxgk/xxgkml/qt/tzgg'+i[1])
    text_url_1.append('http://www.szjmxxw.gov.cn/xxgk/xxgkml/qt/tzgg'+i[1])
    name_sz.append('深圳市经信委')
    
for i in text_url_1:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.find(class_ = 'tit').h1.string)
    
#for ul in soup.find_all(name='ul'):  #时间
#    for li in ul.find_all(name='li'):
#        for span in li.find_all(name='span'):
#            print(span.string)

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_1 = response_1.read().decode('utf8')

#深圳市发改委
#网站2 url需要加原网址
url = 'http://www.szpb.gov.cn/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szpb.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_2 = response.read().decode('gb2312')


pattern = re.compile('<li>.*?\.(.*?)\".*?</i>(.*?)</span>.*?>(.*?)</span>.*?</li>',re.S)
results = re.findall(pattern,text_2)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szpb.gov.cn/xxgk/qt/tzgg'+i[0])
    name_sz.append('深圳市发改委')

    

#网站3 url需要加原网址 深圳市科创委
url = 'http://www.szsti.gov.cn/xxgk/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szsti.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_3 = response.read().decode('utf8')

#soup = BeautifulSoup(text_3,'lxml')
#soup = soup.find_all(class_ = 'list-body')
#soup = str(soup)

pattern = re.compile('<p><a href=\"\.(.*?)" target=\"_blank\" title=\"(.*?)\">.*?</a><span class="t">(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,text_3)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.szsti.gov.cn/xxgk/tzgg'+i[0])
    name_sz.append('深圳市科创委')


#网站4 url需要加原网址深圳市财委
url = 'http://www.szfb.gov.cn/xwzx/tzgg/'
#url_1 = 'http://www.szfb.gov.cn/xwzx/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szfb.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_4 = response.read().decode('gb2312')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_4_1 = response_1.read().decode('gb2312')

pattern = re.compile('<li>.*?class=\"tit\".*?\.(.*?)\" target="_blank.*?title=\"(.*?)</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,text_4)
text_url_4 = []
for i in results:
    #page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szfb.gov.cn/xwzx/tzgg'+i[0])
    text_url_4.append('http://www.szfb.gov.cn/xwzx/tzgg'+i[0])
    name_sz.append('深圳市财委')
     
for i in text_url_4:
    #req = request.Request(url=i,headers=headers)
    response = requests.get(url=i,headers=headers)
    html=response.content
    html=html[0:5900]
    html_doc=str(html,'gb2312')
    print(i)
    soup = BeautifulSoup(html_doc,'lxml')
    page_wd.append(soup.find(class_ = 'tit').h1.string)        

    
#网站5 1页15条解析是需注意 深圳市人力资源和社保局
url = 'http://www.szhrss.gov.cn/tzgg/'
#url_1 = 'http://www.szhrss.gov.cn/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szhrss.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_5 = response.read().decode('gb2312')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_5_1 = response_1.read().decode('gb2312')

pattern = re.compile('<li>.*?\.(.*?)\" target="_blank" title="(.*?)\">.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,text_5)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szhrss.gov.cn/tzgg'+i[0])
    name_sz.append('深圳市人力资源和社保局')


#网站6 1页15条解析是需注意 url有点怪  深圳市税务局
url = 'http://www.sztax.gov.cn/sztax/xxgk_tzgg/xxgk_list.shtml'
#url_1 = 'http://www.sztax.gov.cn/sztax/xxgk_tzgg/xxgk_list_2.shtml'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.sztax.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_6 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_6_1 = response_1.read().decode('utf8')

pattern = re.compile('<li>.*?<span class="fl">.*?\.\.\/\.\.(.*?)\" target=\"_blank\" title=\\\'(.*?)\\\'.*?<span class="fr">(.*?) .*?</span>.*?</li>',re.S)
results = re.findall(pattern,text_6)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.sztax.gov.cn'+i[0])
    name_sz.append('深圳市税务局')


#网站7 1页15条解析是需注意 url有点怪 深圳市住建局
url = 'http://www.szjs.gov.cn/csml/bgs/xxgk/tzgg_1/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szjs.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_7 = response.read().decode('utf8')

soup = BeautifulSoup(text_7,'lxml')
soup = soup.find(class_ = 'ftdt-list')
soup = str(soup)

pattern = re.compile('<a.*?\.(.*?)\" title=\"(.*?)\".*?</a><span>(.*?)</span></li>',re.S)
results = re.findall(pattern,soup)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append('20'+i[2])
    text_url.append('http://www.szjs.gov.cn/csml/bgs/xxgk/tzgg_1'+i[0])
    name_sz.append('深圳市住建局')


#网站8 南山区科技创新局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qkcj/xxgk/qt/tzgg/'
#url_1 = 'http://www.szns.gov.cn/xxgk/bmxxgk/qkcj/xxgk/qt/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_8 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_8_1 = response_1.read().decode('utf8')
soup = BeautifulSoup(text_8,'lxml')
soup = soup.find(class_ = "lb")
soup=str(soup)

pattern = re.compile('<a.*?\.(.*?)\".*?</div>(.*?)</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_8=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qkcj/xxgk/qt/tzgg'+i[0])
    text_url_8.append('http://www.szns.gov.cn/xxgk/bmxxgk/qkcj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区科技创新局')

for i in text_url_8:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.find(class_ = 'mainContentBot1').h2.string)


##网站9 1页超过了20 深圳市中小企业服务署
#url = 'http://www.szsmb.gov.cn/category/7.html'
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
#    'Host':'www.szsmb.gov.cn'
#         }
#req = request.Request(url=url,headers=headers)
#response = request.urlopen(req)
#text_9 = response.read().decode('utf8')
#
#pattern = re.compile('<div class="rightdate">(.*?)</div>.*?\"(.*?)\" target',re.S)
#results = re.findall(pattern,text_9)
#
#text_url_9=[]
#for i in results[0:10]:
#    #page_wd.append(i[2])
#    date_rq.append(i[0])
#    text_url.append('http://www.szsmb.gov.cn'+i[1])
#    text_url_9.append('http://www.szsmb.gov.cn'+i[1])
#    name_sz.append('深圳市中小企业服务署')
#
#for i in text_url_9:
#    req = request.Request(url=i,headers=headers)
#    response = request.urlopen(req)
#    text = response.read().decode('utf8')
#    soup = BeautifulSoup(text,'lxml')
#    wd = str(soup.find(class_ = 't'))
#    pattern = re.compile('<div class="t">(.*?)</div>',re.S)
#    page_wd.append(''.join((re.findall(pattern,wd))).replace('<br/>',''))
    

#网站10 1页超过了20 广东省科技厅
url = 'http://www.gdstc.gov.cn/zwgk/tzgg/index@1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gdstc.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_10 = response.read().decode('utf8')

soup = BeautifulSoup(text_10,'lxml')
soup = soup.find(class_ = 'p12_l22')
soup = str(soup)

pattern = re.compile('<tr>.*?<img.*?</td>.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a>.*?\">(.*?)</td></tr>',re.S)
results = re.findall(pattern,soup)

text_url_10=[]
for i in results[0:10]:
    #page_wd.append(i[2])
    date_rq.append(i[2])
    text_url.append('http://www.gdstc.gov.cn'+i[0])
    text_url_10.append('http://www.gdstc.gov.cn'+i[0])
    name_sz.append('广东省科技厅')

for i in text_url_10:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.find(class_ = 'p20').strong.string.strip())    


#网站11 广东省人力资源社会保障厅
url = 'http://www.gdhrss.gov.cn/gsgg/index.jhtml'
url_1 = 'http://www.gdhrss.gov.cn/gsgg/index_2.jhtml'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gdhrss.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_11 = response.read().decode('utf8')

req_1 =req = request.Request(url=url_1,headers=headers)
response_1 = request.urlopen(req_1)
text_11_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_11,'lxml')
soup = soup.find(class_ = 'list leftlist')
soup = str(soup)

pattern = re.compile('<a href=\"(.*?)\" target=\"_blank\".*?=\"(.*?)\">.*?<i>(.*?)</i>',re.S)
results = re.findall(pattern,soup)

for i in results[0:9]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append(i[0])
    name_sz.append('广东省人力资源社会保障厅')

soup = BeautifulSoup(text_11_1,'lxml')
soup = soup.find(class_ = 'list leftlist')
soup = str(soup)
pattern = re.compile('<a href=\"(.*?)\" target=\"_blank\".*?=\"(.*?)\">.*?<i>(.*?)</i>',re.S)
results = re.findall(pattern,soup)   
for i in results[0:1]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append(i[0])
    name_sz.append('广东省人力资源社会保障厅')


#网站12 深圳市市场和质量监督管理委员会
url = 'http://www.szmqs.gov.cn/xxgk/qt/tzgg/'
#url_1 = 'http://www.szmqs.gov.cn/xxgk/qt/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szmqs.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_12 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_12_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_12,'lxml')
soup = soup.find_all(class_ = 'phonelist')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)\" title=\"(.*?)\"><em>.*?<span>(.*?)</span></em></a>',re.S)
results = re.findall(pattern,soup)   
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szmqs.gov.cn/xxgk/qt/tzgg'+i[0])
    name_sz.append('深圳市市场和质量监督管理委员会')


#网站13 深圳市安监局
url = 'http://www.szsafety.gov.cn/ajdt/tztg/'
#url_1 = 'http://www.szsafety.gov.cn/ajdt/tztg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szsafety.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_13 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_13_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_13,'lxml')
soup = soup.find_all(class_ = 'con_right')
soup = str(soup)

pattern = re.compile('<li><a href=\"\.(.*?)\" target=\"_blank\".*?/>(.*?)</a>.*?\">(.*?)</span>',re.S)
results = re.findall(pattern,soup) 
text_url_13 = [] 
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.szsafety.gov.cn/ajdt/tztg'+i[0])
    text_url_13.append('http://www.szsafety.gov.cn/ajdt/tztg'+i[0])
    name_sz.append('深圳市安监局')
    
for i in text_url_13:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#网站14 深圳市科学技术协会
url = 'http://www.szsta.org/zxzx_89860/tzgg/'
#url_1 = 'http://www.szsta.org/zxzx_89860/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szsta.org'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_14 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_14_1 = response_1.read().decode('utf8')
#
soup = BeautifulSoup(text_14,'lxml')
soup = soup.find(class_ = 'listBox-temp2')
soup = str(soup)

pattern = re.compile('<li>.*?=\"\.(.*?)\"><i></i>.*?<span>(.*?)</span>\n</a>',re.S)
results = re.findall(pattern,soup) 
text_url_14 = [] 
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szsta.org/zxzx_89860/tzgg'+i[0])
    text_url_14.append('http://www.szsta.org/zxzx_89860/tzgg'+i[0])
    name_sz.append('深圳市科学技术协会')

for i in text_url_14:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.find(class_ = 'fn18 mb20').string) 


#网站15 宝安区发展和改革局
url = 'http://www.baoan.gov.cn/fgj/ywgz/tzgg/'
#url_1 = 'http://www.baoan.gov.cn/fgj/ywgz/tzgg/index_1.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.baoan.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_15 = response.read().decode('utf8')

#req_1 =req = request.Request(url=url_1,headers=headers)
#response_1 = request.urlopen(req_1)
#text_15_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_15,'lxml')
soup = soup.find_all(class_ = 'zx_ml_list')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)\" title=\"(.*?)">.*?</a>.*?<span>(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,soup) 

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.baoan.gov.cn/fgj/ywgz/tzgg'+i[0])
    name_sz.append('宝安区发展和改革局')



#网站16 宝安区科技创新服务中心
url = 'http://kjcx.baoan.gov.cn/zxdt/tzgg/'
url_1 = 'http://kjcx.baoan.gov.cn/zxdt/tzgg/index_1.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'kjcx.baoan.gov.cn'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_16 = response.read().decode('utf8')

req_1 =req = request.Request(url=url_1,headers=headers)
response_1 = request.urlopen(req_1)
text_16_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_16,'lxml')
soup = soup.find_all(class_ = 'news_listR_pic')
soup = str(soup)

pattern = re.compile('<li><span>(.*?)</span>.*?=\"\.(.*?)\" target=\"_blank\">(.*?)</a>',re.S)
results = re.findall(pattern,soup) 

for i in results[0:8]:
    page_wd.append(i[2])
    date_rq.append(i[0])
    text_url.append('http://kjcx.baoan.gov.cn/zxdt/tzgg'+i[1])
    name_sz.append('宝安区科技创新服务中心')

    
soup = BeautifulSoup(text_16_1,'lxml')
soup = soup.find_all(class_ = 'news_listR_pic')
soup = str(soup)    
        
pattern = re.compile('<li><span>(.*?)</span>.*?=\"\.(.*?)\" target=\"_blank\">(.*?)</a>',re.S)
results = re.findall(pattern,soup) 

for i in results[0:2]:
    page_wd.append(i[2])
    date_rq.append(i[0])
    text_url.append('http://kjcx.baoan.gov.cn/zxdt/tzgg'+i[1])
    name_sz.append('宝安区科技创新服务中心')


#网站17 高新企业咨询服务网
url = 'http://www.gaoxinbutie.com/tonggao/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gaoxinbutie.com'
         }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_17 = response.read().decode('utf8')

soup = BeautifulSoup(text_17,'lxml')
soup = soup.find_all(class_ = 'NewsContentList')
soup = str(soup)

pattern = re.compile('<li><span.*?>(.*?)</span><a href=\"(.*?)\">(.*?)</a></li>',re.S)
results = re.findall(pattern,soup) 

for i in results[0:10]:
    page_wd.append(i[2])
    date_rq.append('2018-'+i[0])
    text_url.append(i[1])
    name_sz.append('高新企业咨询服务网')

#网站18
#url = 'http://www.ssia.org.cn/userlist/admin/news-7478.html'
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
#    'Host':'www.ssia.org.cn'
#         }
#req = request.Request(url=url,headers=headers)
#response = request.urlopen(req)
#text_18 = response.read().decode('utf8')


#19 中国科学技术部
url = 'http://www.most.gov.cn/kjjh/xmsb/sbzj/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36'
         }
#req = request.Request(url=url,headers=headers)
#response = request.urlopen(req)
#text_19 = response.read().decode('gb2312')

r = requests.get('http://www.most.gov.cn/kjjh/xmsb/sbzj/',headers=headers)
html=r.content
#text_19 =str(html,'gb2312')
soup = BeautifulSoup(html,'lxml')
#soup = BeautifulSoup(text_19,'lxml')
soup = soup.find_all(class_ = 'STYLE30')
soup = str(soup)

pattern = re.compile('<a class="STYLE30" href=.*?\"(.*?)" target=\"_blank\">(.*?)\((.*?)\)',re.S)
results = re.findall(pattern,soup)
for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    if i[0][0:8] =='../../..':
        text_url.append('http://www.most.gov.cn'+i[0].replace('../../..',''))
    elif i[0][0] =='.':
        text_url.append('http://www.most.gov.cn/kjjh/xmsb/sbzj'+i[0][1:])
    else:
        text_url.append(i[0])
    name_sz.append('中国科学技术部')

    
#20  中国工业和信息化部
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'xxgk.miit.gov.cn'
         }
r = requests.get('http://www.miit.gov.cn/n1146295/n1652858/n1653100/index.html',headers=headers)
html=r.content
text_20 =str(html,'utf-8')

soup = BeautifulSoup(text_20,'lxml')
soup = soup.find_all(class_ = 'clist_con')
soup = str(soup)

pattern = re.compile('<li>.*?=\".*?\" target=\"_blank\">(.*?)</a>.*?=\"\.\.\/\.\.\/\.\.(.*?)\" target=\"_blank\">(.*?)</a></span>',re.S)
results = re.findall(pattern,soup)
for i in results[0:10]:
    page_wd.append(i[0])
    date_rq.append(i[2])
    text_url.append('http://www.miit.gov.cn'+i[1])
    name_sz.append('中国工业和信息化部')


#21 中国商务部
url = 'http://www.mofcom.gov.cn/article/b/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.mofcom.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_21= response.read().decode('utf8')

soup = BeautifulSoup(text_21,'lxml')
soup = soup.find_all(class_ = 'complink')
soup = str(soup)

pattern = re.compile('<a class="complink" href=\"(.*?)\" target=\"_blank\" title=\"(.*?)">.*?</a>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    #date_rq.append(i[2])
    text_url.append('http://www.mofcom.gov.cn'+i[0])
    name_sz.append('中国商务部')
    
soup = BeautifulSoup(text_21,'lxml')
soup = soup.find_all(class_ = 'comptime')
soup = str(soup)

pattern = re.compile('<span class=\"comptime\">(.*?)</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i)
    #text_url.append('http://www.mofcom.gov.cn'+i[0])
    #name_sz.append('中国工业和信息化部')

    
#22 中国财政部
url = 'http://kjs.mof.gov.cn/zhengwuxinxi/zhengcefabu/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'kjs.mof.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_22= response.read().decode('gb2312')

soup = BeautifulSoup(text_22,'lxml')
soup = soup.find(class_ = 'ZIT')
soup = str(soup)

pattern = re.compile('<td class="ZITI">.*?src=.*?\".*?=\"\.(.*?)\" target=\"_blank\">.*?\（(.*?)\）.*?</td>',re.S)
results = re.findall(pattern,soup)

text_url_22 = []
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    if i[0][0]=='.':
        text_url.append('http://kjs.mof.gov.cn/zhengwuxinxi'+i[0][1:])
        text_url_22.append('http://kjs.mof.gov.cn/zhengwuxinxi'+i[0][1:])
    else:
        text_url.append('http://kjs.mof.gov.cn/zhengwuxinxi/zhengcefabu'+i[0])
        text_url_22.append('http://kjs.mof.gov.cn/zhengwuxinxi/zhengcefabu'+i[0])
    name_sz.append('中国财政部')

for i in text_url_22:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('gb2312')
    soup = BeautifulSoup(text,'lxml')
    pattern = re.compile('<td.*?>(.*?)</td>',re.S)
    change = str(soup.find(class_ = 'font_biao1'))
    results = ''.join(re.findall(pattern,change))
    page_wd.append(results.replace('<br/>','').strip())

    
#23 中国发展和改革委员会

#my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
#"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
#"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
#"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
#"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]  
#
#
#url = 'http://www.ndrc.gov.cn/zcfb/zcfbtz/'
#headers = {
#    'User-Agent':random.choice(my_headers),
#    'Host':'www.ndrc.gov.cn',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
#    }
#proxy = '111.155.116.220:8123'
#proxies = {
#           'http':'http://'+proxy
#           }    
#           
###req = request.Request(url=url,headers=headers)
###response = request.urlopen(req)
###text_23= response.read().decode('utf8')
#
#r = requests.get('http://www.ndrc.gov.cn/zcfb/zcfbtz/',headers=headers,proxies=proxies)
#html=r.content
#text_23 =str(html,'utf-8')
###r = session.get('http://www.ndrc.gov.cn/zcfb/zcfbtz/',headers=headers)
#
###soup = BeautifulSoup(text_23,'lxml')
###soup = soup.find(class_ = 'list_02 clearfix')
###soup = str(soup)
#
#pattern = re.compile('<font.*?\">(.*?)/(.*?)/(.*?)</font><a href=\"\.(.*?)\" target=\"_blank\">(.*?)</a>',re.S)
###pattern = re.compile('<li class=\"li\"><font class=\"date\">(.*?)/(.*?)/(.*?)</font><a href=\"\.(.*?)\" target=\"_blank\">(.*?)</a><span class=\"new\"></span></li>',re.S)
#results = re.findall(pattern,text_23)
#
#for i in results[0:10]:
#    page_wd.append(i[4])
#    date_rq.append(i[0]+'-'+i[1]+'-'+i[2])
#    text_url.append('http://www.ndrc.gov.cn/zcfb/zcfbtz'+i[3])
#    name_sz.append('中国发展和改革委员会')




#headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
#opener= request.build_opener()
#opener.addheaders=[headers]
##安装为全局
#request.install_opener(opener)
#data=request.urlopen("http://www.thebigproxylist.com/members/proxy-api.php?output=all&user=list&pass=8a544b2637e7a45d1536e34680e11adf").read().decode('utf8')
#ippool=data.split('\n')
#
#for ip in ippool:
#    ip=ip.split(',')[0]
#    try:
#        print("当前代理IP "+ip)
#        proxy=request.ProxyHandler({"http":ip})
#        opener=request.build_opener(proxy,request.HTTPHandler)
#        request.install_opener(opener)
#        url="http://www.baidu.com"
#        data=request.urlopen(url).read().decode('utf-8','ignore')
#        print("通过")            
#        my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
#        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
#        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]                          
#        url = 'http://www.ndrc.gov.cn/zcfb/zcfbtz/'
#        headers = {
#                'User-Agent':random.choice(my_headers),
#                'Host':'www.ndrc.gov.cn',
#                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
#                }
#        proxy = str(ip)
#        proxies = {
#                  'http':'http://'+proxy
#                  }                           
#            ##req = request.Request(url=url,headers=headers)
#            ##response = request.urlopen(req)
#            ##text_23= response.read().decode('utf8')            
#        r = requests.get('http://www.ndrc.gov.cn/zcfb/zcfbtz/',headers=headers,proxies=proxies)
#        html=r.content
#        text_23 =str(html,'utf-8')
#            ##r = session.get('http://www.ndrc.gov.cn/zcfb/zcfbtz/',headers=headers)
#            
#            ##soup = BeautifulSoup(text_23,'lxml')
#            ##soup = soup.find(class_ = 'list_02 clearfix')
#            ##soup = str(soup)            
#        pattern = re.compile('<font.*?\">(.*?)/(.*?)/(.*?)</font><a href=\"\.(.*?)\" target=\"_blank\">(.*?)</a>',re.S)
#            ##pattern = re.compile('<li class=\"li\"><font class=\"date\">(.*?)/(.*?)/(.*?)</font><a href=\"\.(.*?)\" target=\"_blank\">(.*?)</a><span class=\"new\"></span></li>',re.S)
#        results = re.findall(pattern,text_23)
#        for i in results[0:10]:
#            page_wd.append(i[4])
#            date_rq.append(i[0]+'-'+i[1]+'-'+i[2])
#            text_url.append('http://www.ndrc.gov.cn/zcfb/zcfbtz'+i[3])
#            name_sz.append('中国发展和改革委员会')                        
#        print("-----------------------------")
#        break
#    except Exception as err:
#        print('err')
#        print("-----------------------------")

        
#24 广东省财政厅
url = 'http://www.gdczt.gov.cn/zwgk/zcfg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gdczt.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_24= response.read().decode('utf8')

soup = BeautifulSoup(text_24,'lxml')
soup = soup.find(class_ = 'lists_ty')
soup = str(soup)

pattern = re.compile('<li><a href=\"\.(.*?)\" target=\"_blank\" title=\"(.*?)\">.*?</a><span>(.*?)</span></li>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.gdczt.gov.cn/zwgk/zcfg'+i[0])
    name_sz.append('广东省财政厅')


#25 广东省经济和信息化委员会
url = 'http://www.gdei.gov.cn/zwgk/tzgg/index.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gdei.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_25= response.read().decode('gb2312')

soup = BeautifulSoup(text_25,'lxml')
soup = soup.find(class_ = 'NewsList')
soup = str(soup)

pattern = re.compile('<li><span>(.*?)</span><a href=\".*?\.(.*?)\" target=\"_blank\" title=\"(.*?)\">.*?</a></li>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[2])
    date_rq.append(i[0])
    if i[1][0:4] == './..':
        text_url.append('http://www.gdei.gov.cn'+i[1].replace('./..',''))
    else:
        text_url.append('http://www.gdei.gov.cn/zwgk/tzgg'+i[1])
    name_sz.append('广东省经济和信息化委员会')


#26 广东省发展和改革委员会
url = 'http://www.gddrc.gov.cn/zwgk/ywtz/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.gddrc.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_26= response.read().decode('utf8')

soup = BeautifulSoup(text_26,'lxml')
soup = soup.find_all(class_ = 'gl-cont2 f-r')
soup = str(soup)

pattern = re.compile('<li>.*?\[(.*?)\]</span>.*?=\"\.(.*?)" target=\"_blank\" title=\"(.*?)">.*?</a>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[2])
    date_rq.append(i[0])
    text_url.append('http://www.gddrc.gov.cn/zwgk/ywtz'+i[1])
    name_sz.append('广东省发展和改革委员会')

    
#27 东莞市科技局
url = 'http://www.dgstb.gov.cn/dgstb/zwgktzgg/yjj_list_2.shtml'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.dgstb.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_27= response.read().decode('utf8')

soup = BeautifulSoup(text_27,'lxml')
soup = soup.find_all(class_ = 'padd lb')
soup = str(soup)

pattern = re.compile('<li>.*?href=\"(.*?)\" target=\"_blank\" title=\"(.*?)\">.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.dgstb.gov.cn'+i[0])
    name_sz.append('东莞市科技局')


#28 东莞市发改局 有两页
url = 'http://dgdp.dg.gov.cn/007330029/0801/list2.shtml'
url_1 = 'http://dgdp.dg.gov.cn/007330029/0801/list2_2.shtml'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'dgdp.dg.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_28= response.read().decode('utf8')

req_1 =req = request.Request(url=url_1,headers=headers)
response_1 = request.urlopen(req_1)
text_28_1 = response_1.read().decode('utf8')

soup = BeautifulSoup(text_28,'lxml')
soup = soup.find_all(class_ = 'con-right fr')
soup = str(soup)

pattern = re.compile('<div.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a>.*?<tr>.*?发布时间\：(.*?)</td>.*?</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:7]:
    page_wd.append(i[1])
    date_rq.append(i[2].strip())
    text_url.append('http://dgdp.dg.gov.cn'+i[0])
    name_sz.append('东莞市发改局')

soup = BeautifulSoup(text_28_1,'lxml')
soup = soup.find_all(class_ = 'con-right fr')
soup = str(soup)

pattern = re.compile('<div.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a>.*?<tr>.*?发布时间\：(.*?)</td>.*?</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:3]:
    page_wd.append(i[1])
    date_rq.append(i[2].strip())
    text_url.append('http://www.dgstb.gov.cn'+i[0])
    name_sz.append('东莞市发改局')


#29 东莞财政网
url = 'http://czj.dg.gov.cn/business/htmlfiles/dgcz/s23511/list.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'czj.dg.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_29= response.read().decode('utf8')

soup = BeautifulSoup(text_29,'lxml')
soup = soup.find(class_ = 'list_right_nr')
soup = str(soup)

pattern = re.compile('<Title>(.*?)</Title>.*?<SubTitle />.*?<ExpStr1 />.*?<PublishedTime>(.*?)</PublishedTime>.*?<Source />.*?<ParentCateId>通知公告</ParentCateId>.*?<InfoURL>(.*?)</InfoURL>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[0])
    date_rq.append(i[1])
    text_url.append('http://czj.dg.gov.cn/publicfiles/business/htmlfiles/'+i[2])
    name_sz.append('东莞财政网')

    
#30 东莞市科协 9.20停用
#url = 'http://www.dgkx.gov.cn/info/list-5.html'
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
#    'Host':'www.dgkx.gov.cn' 
#     }
#req = request.Request(url=url,headers=headers)
#response = request.urlopen(req)
#text_30 = response.read().decode('utf8')
#
#soup = BeautifulSoup(text_30,'lxml')
#soup = soup.find(class_ = 'col-md-10')
#soup = str(soup)
#
#pattern = re.compile('<li style=.*?href\=\"(.*?)\" style=.*?\">(.*?)</a>.*?\">(.*?)</span></li>',re.S)
#results = re.findall(pattern,soup)
#
#for i in results[0:10]:
#    page_wd.append(i[1])
#    date_rq.append(i[2])
#    text_url.append(i[0])
#    name_sz.append('东莞市科协')


#31 松山湖官网 9.20停用
#url = 'http://www.ssl.gov.cn/dgssl/ppdgssltzgg/index.htm'
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
#    'Host':'www.ssl.gov.cn' 
#     }
#req = request.Request(url=url,headers=headers)
#response = request.urlopen(req)
#text_31 = response.read().decode('utf8')
#
#soup = BeautifulSoup(text_31,'lxml')
#soup = soup.find(class_ = 'index_2014_list_con_x_r')
#soup = str(soup)
#
#pattern = re.compile('<Title>(.*?)</Title>.*?<PublishedTime>(.*?)</PublishedTime>.*?<InfoURL>(.*?)</InfoURL>',re.S)
#results = re.findall(pattern,soup)
#
#for i in results[0:10]:
#    page_wd.append(i[0].replace('&#xD;&#xD;',''))
#    date_rq.append(i[1])
#    text_url.append('http://www.ssl.gov.cn/'+i[2])
#    name_sz.append('松山湖官网')

    
#32 国家自然科学基金委员会
url = 'http://www.nsfc.gov.cn/publish/portal0/tab434/module1146/more.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.nsfc.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_32 = response.read().decode('utf8')

soup = BeautifulSoup(text_32,'lxml')
soup = soup.find(class_ = 'C_InfoList')
soup = str(soup)

pattern = re.compile('<a href=\"(.*?)\" id.*?target=\"_blank\" title=\"(.*?)\">.*?</a></span><span class="fr">(.*?)</span></li>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2])
    text_url.append('http://www.nsfc.gov.cn'+i[0])
    name_sz.append('国家自然科学基金委员会')

    
#33 南山区住房和建设局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qzjj/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_33 = response.read().decode('utf8')

soup = BeautifulSoup(text_33,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_33=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qzjj/xxgk/qt/tzgg'+i[0])
    text_url_33.append('http://www.szns.gov.cn/xxgk/bmxxgk/qzjj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区住房和建设局')

for i in text_url_33:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#34 南山区安全生产监督管理局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qajj/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_34 = response.read().decode('utf8')

soup = BeautifulSoup(text_34,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_34=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qajj/xxgk/qt/tzgg'+i[0])
    text_url_34.append('http://www.szns.gov.cn/xxgk/bmxxgk/qajj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区安全生产监督管理局')

for i in text_url_34:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#35 南山区人力资源局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qrzj/xxgk/qt/tzgg/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_35 = response.read().decode('utf8')

soup = BeautifulSoup(text_35,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_35=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qrzj/xxgk/qt/tzgg/tzgg'+i[0])
    text_url_35.append('http://www.szns.gov.cn/xxgk/bmxxgk/qrzj/xxgk/qt/tzgg/tzgg'+i[0])
    name_sz.append('南山区人力资源局')

for i in text_url_35:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#36 南山区经济促进局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qjjcjj/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_36 = response.read().decode('utf8')

soup = BeautifulSoup(text_36,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_36=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qjjcjj/xxgk/qt/tzgg'+i[0])
    text_url_36.append('http://www.szns.gov.cn/xxgk/bmxxgk/qjjcjj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区经济促进局')

for i in text_url_36:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#37 南山区发展和改革局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qfgj/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_37 = response.read().decode('utf8')

soup = BeautifulSoup(text_37,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_37=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qfgj/xxgk/qt/tzgg'+i[0])
    text_url_37.append('http://www.szns.gov.cn/xxgk/bmxxgk/qfgj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区发展和改革局')

for i in text_url_37:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#38 南山区财政局
url = 'http://www.szns.gov.cn/xxgk/bmxxgk/qczj/xxgk/qt/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szns.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_38 = response.read().decode('utf8')

soup = BeautifulSoup(text_38,'lxml')
soup = soup.find(class_ = 'lb')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)">.*?</div>.*?</a>.*?<span>(.*?)</span>',re.S)
results = re.findall(pattern,soup)

text_url_38=[]
for i in results[0:10]:
    #page_wd.append(i[1])
    date_rq.append(i[1])
    text_url.append('http://www.szns.gov.cn/xxgk/bmxxgk/qczj/xxgk/qt/tzgg'+i[0])
    text_url_38.append('http://www.szns.gov.cn/xxgk/bmxxgk/qczj/xxgk/qt/tzgg'+i[0])
    name_sz.append('南山区财政局')

for i in text_url_38:
    req = request.Request(url=i,headers=headers)
    response = request.urlopen(req)
    text = response.read().decode('utf8')
    soup = BeautifulSoup(text,'lxml')
    page_wd.append(soup.h2.string) 


#39 宝安区经济促进局
url = 'http://www.baoan.gov.cn/jjcj/jywgz/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.baoan.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_39 = response.read().decode('utf8')

soup = BeautifulSoup(text_39,'lxml')
soup = soup.find(class_ = 'zx_ml_list')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)" title=\"(.*?)\">.*?</a>.*?<span>(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.baoan.gov.cn/jjcj/jywgz/tzgg'+i[0])
    name_sz.append('宝安区经济促进局')


#40 宝安区财政局
url = 'http://www.baoan.gov.cn/czj/ywgz/tzgg_129356/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.baoan.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_40 = response.read().decode('utf8')

soup = BeautifulSoup(text_40,'lxml')
soup = soup.find(class_ = 'zx_ml_list')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)" title=\"(.*?)\">.*?</a>.*?<span>(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.baoan.gov.cn/czj/ywgz/tzgg_129356'+i[0])
    name_sz.append('宝安区财政局')


#41 宝安区住房和建设局
url = 'http://www.baoan.gov.cn/jshej/ywgz_136247/tzgg/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.baoan.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_41 = response.read().decode('utf8')

soup = BeautifulSoup(text_41,'lxml')
soup = soup.find(class_ = 'zx_ml_list')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)" title=\"(.*?)\">.*?</a>.*?<span>(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.baoan.gov.cn/jshej/ywgz_136247/tzgg'+i[0])
    name_sz.append('宝安区住房和建设局')

    
#42 宝安区人力资源局
url = 'http://www.baoan.gov.cn/rlzyj/ywgz_136244/tzgg_129356/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.baoan.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_42 = response.read().decode('utf8')

soup = BeautifulSoup(text_42,'lxml')
soup = soup.find(class_ = 'zx_ml_list')
soup = str(soup)

pattern = re.compile('<a href=\"\.(.*?)" title=\"(.*?)\">.*?</a>.*?<span>(.*?)年(.*?)月(.*?)日</span>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[1])
    date_rq.append(i[2]+'-'+i[3]+'-'+i[4])
    text_url.append('http://www.baoan.gov.cn/rlzyj/ywgz_136244/tzgg_129356'+i[0])
    name_sz.append('宝安区人力资源局')

    
#43 深圳市中小企业服务-通知公告
url = 'http://www.szsmb.gov.cn/category/7.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szsmb.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_43 = response.read().decode('utf8')

soup = BeautifulSoup(text_43,'lxml')
soup = soup.tbody
soup = str(soup)

pattern = re.compile('<tr><td height=\"25\"><div class=\"rightdate\">(.*?)</div>.*?href=\"(.*?)\" target=\"_blank\" title=\"(.*?)\">.*?</a></td></tr>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[2].replace('&lt;BR&gt;',''))
    date_rq.append(i[0])
    text_url.append('http://www.szsmb.gov.cn'+i[1])
    name_sz.append('深圳市中小企业服务-通知公告')


#44 深圳市中小企业服务-专项资金
url = 'http://www.szsmb.gov.cn/category/768.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'Host':'www.szsmb.gov.cn' 
     }
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
text_44 = response.read().decode('utf8')

soup = BeautifulSoup(text_44,'lxml')
soup = soup.tbody
soup = str(soup)

pattern = re.compile('<tr><td height=\"25\"><div class=\"rightdate\">(.*?)</div>.*?href=\"(.*?)\" target=\"_blank\" title=\"(.*?)\">.*?</a></td></tr>',re.S)
results = re.findall(pattern,soup)

for i in results[0:10]:
    page_wd.append(i[2].replace('&lt;BR&gt;',''))
    date_rq.append(i[0])
    text_url.append('http://www.szsmb.gov.cn'+i[1])
    name_sz.append('深圳市中小企业服务-专项资金')


    
time_stamp = datetime.datetime.now()
mon = str(time_stamp.month)
da = str(time_stamp.day)
now = mon+da    
    
    
df_1 = pd.DataFrame(name_sz,columns=['网站名称'])
df_2 = pd.DataFrame(page_wd,columns=['内容'])
df_3 = pd.DataFrame(date_rq,columns=['日期'])
df_4 = pd.DataFrame(text_url,columns=['网址'])
df_5 = pd.concat([df_1, df_2,df_3,df_4],axis=1)
df_6 = pd.read_excel('/usr/local/spyder/%s.xls' %now)
df_5 = pd.concat([df_5, df_6])



#df_5.to_excel('/usr/local/spyder/%s.xlsx' %now,index=None)
#df_5.to_excel('C:\\Users\\admin\\Desktop\\%s.xlsx' %now,index=None)

file = xlwt.Workbook()
table = file.add_sheet('sheet1',cell_overwrite_ok=True)
table.col(0).width=256*30
table.col(1).width=256*120
table.col(2).width=256*20
table.col(3).width=256*120

for i,gen in enumerate(df_5['网站名称']):
    print(i,gen)
    table.write(0,0,'网站名称')
    table.write(i+1,0,'%s' % gen )    
         
for i,gen in enumerate(df_5['内容']):
    print(i,gen)
    table.write(0,1,'内容')
    table.write(i+1,1,'%s' % gen ) 
        
for i,gen in enumerate(df_5['日期']):
    print(i,gen)
    table.write(0,2,'日期')
    table.write(i+1,2,'%s' % gen )   

for i,gen in enumerate(df_5['网址']):
    print(i,gen)
    table.write(0,3,'网址')
    table.write(i+1,3,'%s' % gen )       

file.save('/usr/local/spyder/%s.xls' %now)     


