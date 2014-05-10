#!/usr/bin/env python2
#coding : utf-8


import urllib2
import sys
import json

URL = 'http://fanyi.youdao.com/openapi.do?keyfrom=cctv10&key=1365682047&type=data&doctype=json&version=1.1&q='

def get_json_str(word='may'):
    return urllib2.urlopen(URL+word).read()


def show_result(json_str):
    jsonDict = json.loads(json_str)
    translation_list = []
    web_list = []
    basic_dict = {}
    for k,v in jsonDict.items():
        #print k,v
        if k == 'translation':
            translation_list = v
        #        print vl
        elif k == 'web':
            web_list = v
        #    for vl in v:
        #        print vl['key'],"".join(vl['value'])
        elif k == 'basic':
            basic_dict = v
        #    for d,c in v.items():
        #        #print d,c
        #        if d == 'phonetic':
        #            print c
        #        if d == 'explains':
        #            for l in c:
        #                print l
    if len(translation_list) != 0:
        print("\n--------------------------translation-----------------------\n")
    for tr in translation_list:
        print tr
    if len(basic_dict) != 0:
        print('\n--------------------------basic-----------------------------\n')
    for k,v in basic_dict.items():
        #print k,v
        if k == 'explains':
            #print v
            for l in v:
                print l
    if len(web_list) != 0:
        print('\n--------------------------web------------------------------\n')
    for wl in web_list:
        msg = '%-18s  => %s'  %(wl['key'],";".join(wl['value']))
        print msg
        #for k,v in wl.items():
        #    print v




def main():
    if len(sys.argv) != 2:
        print("invalid parameter")
    else:
        word = sys.argv[1]
        show_result(get_json_str(word))


if __name__ == "__main__":
    main()
