# By Martin v1.0.0
# Automatic crawling to obtain data
# Main(Target_Url,Xpath,log echo)
# return value (Stat_Code,Web_Source_Code,Server_respon_message,content)

import requests,random,sys
from lxml import etree as CS_etree


class Crawling_Spider_Collection():
    def __init__(self):
        self.__User_Agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1'
        ]


    def draw(self,url,myxpath,log=True):
        self.url = url
        try:
            respon = requests.get(self.url,headers={'User-Agent':random.choice(self.__User_Agents)},timeout=5)
        except:
            if log:
                print('Network error, unable to reach the server!')
            return (None,None,None,None)
        else:
            if respon.status_code == 200:
                tree = CS_etree.HTML(respon.text)
                content = tree.xpath(myxpath+'/text()')
                if not content:
                    if log:
                        print('Content is empty!')
                    return (None,None,None,None)
                else:
                    return (respon.status_code,respon.text,respon.headers,content[0].strip())
            else:
                if log:
                    print("the server cannot be accessed!")
                return (None,None,None,None)