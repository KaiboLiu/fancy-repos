# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
    #target = 'https://qingbuyaohaixiu.com/post/18097/'
    target = 'http://qingbuyaohaixiu.com/post/17932/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    print(req.text)

