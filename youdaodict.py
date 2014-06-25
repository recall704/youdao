#!/usr/bin/env python2
# -*- coding:utf-8 -*-


import urllib2
import urllib
import sys
import json

URL = 'http://fanyi.youdao.com/openapi.do?keyfrom=cctv10&key=1365682047&type=data&doctype=json&version=1.1&q='


def get_result(word):
    url = URL + urllib.quote(word.decode(sys.stdin.encoding).encode('utf-8'))
    html = urllib2.urlopen(url).readlines()
    try:
        json_data = json.loads(html[0])
        errorCode = json_data.get('errorCode',-1)
        if errorCode != 0:
            print u'查询出错'
        else:
            # 基本含义
            print u'基本含义'.center(40,'*')
            #print json_data.get('query','') #查询的词
            tran =  json_data.get('translation',None) #翻译结果
            if tran:
                for item in tran:
                    print '\t',item
            
            print u'网络含义'.center(40,'*')
            web = json_data.get('web',None)
            if web:
                for item in web:
                    print item.get('key',None),"=>"
                    for v in item.get('value',''):
                        print '\t\t',v
        #print json_data
    except:
        print u'无法解析json数据'
    
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print u'无效的参数个数'
    else:
        get_result(sys.argv[1])
