#-*- coding: utf-8 -*-
#---------------------------------
#用于下载网页
#---------------------------------

import string,urllib2

def downloadPage(url,name):
    sName = name+'.json'
    print 'Loading page...'
    f = open(sName,'w+')
    content = urllib2.urlopen(str('http://')+url).read()
    f.write(content)
    f.close()

#------------输入参数--------------
url = str(raw_input(u'请输入网址：'))
name = str(raw_input(u'请输入保存的文件名：'))
#---------------------------------

#调用
downloadPage(url,name)
print u'Done!'
