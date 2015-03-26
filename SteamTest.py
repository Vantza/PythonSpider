# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time
import json

#----------加载处理Steam市场--------------
class Spider_Model:
    



    def __init__(self):
        self.enable = False
        self.myUrl = "http://steamcommunity.com/market/recent?country=CN&language=schinese&currency=1"
        self.data = {"country":"CN",
                     "language":"schinese",
                     "currency":"1"}

    def getLastOn(self,page):

        #print(page)
        #page = page.decode("utf-8")
        #找出所有的class="market_listing_item_name_link"的a
        #找出所有的class="market_listing_game_name"的span
        #找出所有的class="market_listing_price market_listing_price_with_fee"的span
        Commodity_names = re.findall('<a class="market_listing_item_name_link".*?>(.*?)</a>',page,re.S)
        Commodity_games = re.findall('<span.*?class="market_listing_game_name">(.*?)</span>',page,re.S)
        Commodity_prices = re.findall('<span.*?class="market_listing_price market_listing_price_with_fee">(.*?)</span>',page,re.S)

        #曾用来统计获取到的数据数量
        #print len(Commodity_names)
        #print len(Commodity_games)
        #print len(Commodity_prices)
        

        items = []
        for i in range(0,10):
            
            Commodity_prices[i] = Commodity_prices[i].replace("&#36;","$")
            #print[Commodity_prices[i]]
            
            item = [Commodity_names[i],Commodity_games[i],Commodity_prices[i]]
            items.append(item)
            print items[i][0]+"\n"+items[i][1]+items[i][2]+"\n"

        return items
    

    #访问地址后返回的是Json文件
    def request_ajax_data(self):
        req = urllib2.Request(self.myUrl)
        #伪装成浏览器访问
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('X-Requested-With','XMLHttpRequest')
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
 
        params = urllib.urlencode(self.data)
        #print(params)
        response = urllib2.urlopen(req, params)
        jsonText = response.read()
        #使原编码改为utf-8编码（中文太恶心了）
        unicodePage = jsonText.decode("utf-8")
        return unicodePage

    #解析Json文件
    def parseJson(self,jsonText):
        j = json.loads(jsonText)
        page = j["results_html"]
        #print(page)
        return page

    def start(self):
        self.enable = True
        while self.enable:
            
            self.getLastOn(self.parseJson(self.request_ajax_data()))
            print('========================^_^============================')

            myInput = raw_input()
            if myInput == 'q':
                self.enable = False
                break
        


#------------程序入口处---------------
print u'''
---------------------------------------
    程序：steam市场
    
语言：Pythom 2.7
    
版本：1.0
    
作者：Cy
    
操作：输入‘q’退出，按下回车获取最新上架资讯
    
功能：获取steam市场上最新上架的信息
---------------------------------------
'''

print u'~~~~'
print u'请按下回车浏览即时steam最新上架：'  
myInput = raw_input(' ')
myModel = Spider_Model()
#print(myModel.GetLastOn(myUrl))
#myModel.request_ajax_data(myUrl,)
#print(myModel.request_ajax_data())

#f = open('steam.json','w+')
#f.write(myModel.request_ajax_data())
#f.close()

#tt = myModel.request_ajax_data()
#page = myModel.parseJson(tt)
#myModel.getLastOn(page)
myModel.start()

print u'谢谢使用！'


#market.js/line:948&992
