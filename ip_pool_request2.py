import requests
import re
import random
import time

class download():
    def __init__(self):

        self.ip_list=[]
        html = requests.get('http://haoip.cc/tiqu.htm')
        all_ip = re.findall(r'r/>(.*?)<b', html.text, re.S)
        for i in all_ip:
            ip = re.sub('\n', '', i)
            self.ip_list.append(i.strip())
            #print(ip.strip())
        self.user_agent_list=[
            'mozilla/4.0 (compatible; msie 7.0; aol 8.0; windows nt 5.1; gtb5; .net clr 1.1.4322; .net clr 2.0.50727)',
            'mozilla/4.0 (compatible; msie 7.0; aol 8.0; windows nt 5.1; .net clr 2.0.50727)',
    'mozilla/4.0 (compatible; msie 7.0; aol 8.0; windows nt 5.1; .net clr 1.1.4322; .net clr 2.0.50727; infopath.1; .net clr 3.0.04506.30) ',
'mozilla/4.0 (compatible; msie 7.0; aol 8.0; windows nt 5.1; .net clr 1.1.4322; .net clr 2.0.50727) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; ycomp 5.0.0.0; .net clr 1.0.3705) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; sv1; .net clr 1.1.4322) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; sv1; (r1 1.3); .net clr 1.1.4322)',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; sv1) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; q312461)',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; funwebproducts; sv1; .net clr 1.0.3705) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; funwebproducts; sv1) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; funwebproducts) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; .net clr 1.1.4322)',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; .net clr 1.0.3705) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1; (r1 1.3)) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.1) ',
'mozilla/4.0 (compatible; msie 6.0; aol 8.0; windows nt 5.0)',
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",

        ]
    def get(self,url,timeout,proxy=None,num_retries=6):
        ran_agent=random.choice(self.user_agent_list)
        headers={'User-Agent':ran_agent}
        if proxy ==None:
            try:

                return requests.get(url, headers=headers, timeout=timeout).text

            except:
                if int(num_retries)>0:

                    time.sleep(8)
                    print(u'获取网页出错，8S后将获取倒数第：', num_retries, u'次')
                    return self.get(url,timeout,int(num_retries)-1)
                else:
                    print(u'开始使用代理')
                    time.sleep(8)
                    ip=''.join(str(random.choice(self.ip_list)).strip())
                    proxy={'http':ip}
                    return self.get(url,timeout,proxy=proxy)
        else:

            try:

                return requests.get(url,headers=headers,proxies=proxy,timeout=timeout).text
            except:
                if num_retries>0:
                    time.sleep(10)
                    ip=''.join(str(random.choice(self.ip_list)).strip())
                    proxy = {'http': ip}
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.get(url, timeout, proxy, int(num_retries)-1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.get(url, 3)


download_request=download()