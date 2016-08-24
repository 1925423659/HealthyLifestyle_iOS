# -*- coding:utf-8 -*-

import urllib
import urllib.request
import sys
import re





class Acupoint:
    listURL = 'http://www.a-hospital.com/w/'
    detailURL = 'http://www.a-hospital.com/w/%E9%92%88%E7%81%B8%E5%AD%A6/'
    removeTags = re.compile('<.*?>|</.*?>')
    removeSpaces = re.compile('\s')
    
#    def __init__(self):

    def getListURL(self, meridian):
        return self.listURL + urllib.parse.quote(meridian)
    
    def getDetailURL(self, acupoint):
        return self.detailURL + urllib.parse.quote(acupoint)
    
    #获取页面
    def getPage(self, url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')

    #获取穴位列表
    def getAcupointList(self, page):
        reg = r'<table class="wikitable">(.*?)</table>'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, page)
        
        newitems = []
        reg = r'<tr>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n</tr>'
        pattern = re.compile(reg, re.S)
        for item in items:
            list = re.findall(pattern, item)
            for a in list:
                newitem = []
                for i in a:
                    i = re.sub(self.removeTags, "", i)
                    i = re.sub(self.removeSpaces, "", i)
                    newitem.append(i.strip())
                newitems.append(newitem)
        return newitems

    #获取穴位详情
    def getAcupointDetail(self, page):
        reg = r'</table>\n<p>(.*)?</p>*\n<table id="toc" class="toc">'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, page)
        detail = ''
        for item in items:
            item = re.sub(self.removeTags, "", item)
            item = re.sub(self.removeSpaces, "", item)
            detail += item.strip()
        return detail

    #获取主治
    def getIndication(self, detail):
        reg = r'［主治］([^［]*)'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, detail)
        detail = ''
        for item in items:
            item = re.sub(self.removeTags, "", item)
            item = re.sub(self.removeSpaces, "", item)
            detail += item.strip();
        return detail

    #获取针灸法
    def getAcupuncture(self, detail):
        reg = r'［刺灸法］([^［]*)'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, detail)
        detail = ''
        for item in items:
            item = re.sub(self.removeTags, "", item)
            item = re.sub(self.removeSpaces, "", item)
            detail += item.strip();
        return detail

    #获取配伍
    def getCooperation(self, detail):
        reg = r'［配伍］([^［]*)'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, detail)
        detail = ''
        for item in items:
            item = re.sub(self.removeTags, "", item)
            item = re.sub(self.removeSpaces, "", item)
            detail += item.strip();
        return detail


#acupoint = Acupoint()
#page = acupoint.getPage(acupoint.listurl + "手太阳小肠经穴")
#items = acupoint.getAcupointList(page)
#for item in items:
#    print(item)
#page = acupoint.getPage(acupoint.getDetailURL("少商穴"))
#detail = acupoint.getAcupointDetail(page)
#print(detail)
#indication = acupoint.getIndication(detail)
#print(indication)
#acupuncture = acupoint.getAcupuncture(detail)
#print(acupuncture)
#cooperation = acupoint.getCooperation(detail)
#print(cooperation)


