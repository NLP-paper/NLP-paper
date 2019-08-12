#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
__file__

    Crawler_Name_py3.py
    
__description__

    This file is for cralwering first and last name from Oxford Name Dictionary 
    
"""


import re
import random
from urllib import request
import time

########################
###Class for Crawler####
########################

## This class is only based on Urllib
## In order to decrease the duplicated codes, I use a customized class and functions
## But all hard core functions are from urllib, so it is still equal to using third party package(urllib), not my own functions
class Crawler_Name:
    
    def __init__(self,
                 page_number,
                 user_agent_list,
                 proxy_list):
        
        self.page_number=page_number
        self.user_agent_list=user_agent_list
        self.proxy_list=proxy_list
        self.default_user_agent=self.user_agent_list[0]
    
    def user_agent(self):
        return random.choice(user_agent_list)
    
    def user_proxy(self):
        return random.choice(proxy_list)
    
    ## The fast download function uses fixed User-Agent and fixed Ip address
    ## It may occur failure of Crawler task for high frequency sending request to server
    ## However, here I put some commands(functions) between each time of request in the loop of
    ## for i in range(1,cwl_first_name.page_number+1):
    ## Thus, this request is not high frequency. So you can use this simple one 
    def fast_download_html(self,url): 
        headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent':self.default_user_agent,
               'Connection': 'keep-alive',
                   }
        response=request.Request(url,headers=headers)
        html=request.urlopen(response).read().decode('utf-8')
        return html 
    
    
    ## The download function uses random proxy IP address and user_agent, so it is much safe
    ## But I have to maintain the proxy_list in which many IP address may out of date in the future
    ## The four Ip address in proxy_list are available when I run the crawler
    def download_html(self,url):
        proxy={'http':self.user_proxy()}
        proxy_support =request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        request.install_opener(opener)
        user_agent=self.user_agent()
        headers = {'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'User-Agent':user_agent ,
                   'Connection': 'keep-alive',
                   }
        response=request.Request(url,headers=headers)
        html=request.urlopen(response).read().decode('utf-8')
        return html
    
    ## search the all names from one page
    def scrap_name(self,html):   
        pattern='result=[0-9]*">[a-z]+'
        all_name=re.findall(pattern,html,re.I)
        all_name=list(map(lambda x: re.search('[A-Z][a-z]*',x).group(),all_name))
        return all_name

    
##########
##Main####
##########
if __name__=="__main__":
    user_agent_list = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
    proxy_list = ['138.219.229.239:80',
                 '77.242.105.88:80',
                 '171.97.103.31:80',
                 '89.40.115.70:80']
    
    ###############
    ###First_Name##
    ###############
    
    First_Name_URL='http://www.oxfordreference.com/view/10.1093/acref/9780198610601.001.0001/acref-9780198610601?btog=chap&hide=true&page=1&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780198610601.001.0001%2Facref-9780198610601'
    URL_former=re.search('^.*page=',First_Name_URL).group() # cur off the URL and combine with page number i later
    URL_latter=re.search('&pageSize.*$',First_Name_URL).group()
    First_Name_page=389 # total pages
    
    cwl_first_name=Crawler_Name(First_Name_page,user_agent_list,proxy_list)
    
    First_Name_List=[]
    
    start_time = time.time()
    ## Add name list from each page together
    for i in range(1,cwl_first_name.page_number+1):
        URL=URL_former+str(i)+URL_latter # cur off the URL and combine with page number i to create each page URL
        html=cwl_first_name.fast_download_html(URL)
        name=cwl_first_name.scrap_name(html)#Scrap name
        First_Name_List+=name
    print("Time for running this crawler is %d sec" %(time.time() - start_time))
    First_Name_List=list(filter(lambda x: len(x)>1,First_Name_List))
    print(First_Name_List)
    
    
    ########################
    ###Last_Name_American###
    ########################
    Last_Name_American_URL='http://www.oxfordreference.com/view/10.1093/acref/9780195081374.001.0001/acref-9780195081374?btog=chap&hide=true&page=4&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780195081374.001.0001%2Facref-9780195081374'
    URL_former=re.search('^.*page=',Last_Name_American_URL).group()
    URL_latter=re.search('&pageSize.*$',Last_Name_American_URL).group()
    Last_Name_American_page=3516

    cwl_Last_Name_American=Crawler_Name(Last_Name_American_page,user_agent_list,proxy_list)

    Last_Name_American_List=[]

    start_time = time.time()
    for i in range(1,cwl_Last_Name_American.page_number+1):
        URL=URL_former+str(i)+URL_latter
        html=cwl_Last_Name_American.fast_download_html(URL)
        name=cwl_Last_Name_American.scrap_name(html)#Scrap name
        Last_Name_American_List+=name
    print("Time for running this crawler is %d sec" %(time.time() - start_time))
    Last_Name_American_List=list(filter(lambda x: len(x)>1,Last_Name_American_List))
    print(Last_Name_American_List)
    
    
    ###################
    ####Counrty_Name###
    ###################
    Counrty_Name_URL='https://en.wikipedia.org/wiki/Lists_of_cities_by_country'
    Country_Name_page=1
    
    cwl_country_name=Crawler_Name(Country_Name_page,user_agent_list,proxy_list)
   
    Country_Name_List=[]
    
    start_time = time.time()
    ## Add name list from each page together
    for i in range(1,cwl_country_name.page_number+1):
        URL=Counrty_Name_URL
        html=cwl_country_name.fast_download_html(URL)
        tp=re.findall('<li><span class="flagicon"><a href="/wiki/[a-z]*"',html,re.I)
        tp=list(map(lambda x: re.search('/[A-Z][a-z]*',x).group(),tp ))
        tp=list(map(lambda x: re.search('[A-Z][a-z]*',x).group(),tp ))
        Country_Name_List+=tp
    print("Time for running this crawler is %d sec" %(time.time() - start_time))
    print(Country_Name_List)
    
    
    ##################
    #####City_Name####
    ##################
    City_Name_URL='https://en.wikipedia.org/wiki/Lists_of_cities_by_country'
    City_Name_page=169
    
    cwl_city_name=Crawler_Name(City_Name_page,user_agent_list,proxy_list)
    
    html=cwl_city_name.fast_download_html(City_Name_URL)
    URL_city_list=re.findall('</span>.*href="/wiki/List_of_cities_[\w]+',html)
    URL_city_list=list(map(lambda x: re.search('/wiki/List_of_cities_[\w]+',x).group() ,URL_city_list))
    URL_city_list=list(map(lambda x: 'https://en.wikipedia.org'+x ,URL_city_list))
    
    City_Name_List=[]
    
    start_time = time.time()
    for pos, url in enumerate(URL_city_list):
        try:
            City_Name_List.append(re.search('(?=_[A-Z])[\w]+',url).group())
            html=cwl_city_name.fast_download_html(url)
            #time.sleep(0.5)
            tp0=re.findall('<td.*><a href="/wiki/[\w\s]*" title="[\w\s]*">',html,re.I)
            tp1=list(map(lambda x:re.search('"[\w\s]*">$',x).group(),tp0))
            tp2=list(map(lambda x:re.search('[\w\s]+',x).group(),tp1))
            City_Name_List+=tp2
        except:
            print(pos)
    print("Time for running this crawler is %d sec" %(time.time() - start_time))
    print(City_Name_List)
    
    
    print("***************************Done************************************")

