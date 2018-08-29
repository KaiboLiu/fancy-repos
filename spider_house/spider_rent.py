import requests 
import time 
import re 
from lxml import etree 
import pinyin
import sys

city = 'sh'
n_cut = 2 if city == 'bj' else 0
base_url = 'https://{}.lianjia.com'.format(city) 
# 获取某市区域的所有链接 
def get_areas(url): 
    print('start grabing areas') 
    t0 = time.time()        # 08/27/2018 by kaibo
    headers = { 
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'} 
    resposne = requests.get(url, headers=headers) 
    content = etree.HTML(resposne.text) 
    areas = content.xpath("//dd[@data-index = '0']//div[@class='option-list']/a/text()") 
    print(areas)            # 08/27/2018 by kaibo
    areas_link = content.xpath("//dd[@data-index = '0']//div[@class='option-list']/a/@href") 
    for i in range(1,len(areas)-n_cut):      # kaibo: last of beijing 2 are '燕郊', '香河', which belongs to different domain (lf.lianjia.com instead of bj.lianjia.com 
    #for i in range(13,len(areas)-2):     # kaibo: last 2 are '燕郊', '香河', which belongs to different domain (lf.lianjia.com instead of bj.lianjia.com 
        t1 = time.time()
        area = areas[i] 
        area_link = areas_link[i] 
        link = base_url + area_link 
        print("开始抓取页面#{}-{}".format(i, area)) 
        get_pages(area, link) 
        print('{} area time: {:.5} s, total time: {:.5} s'.format('='*10, time.time()-t1, time.time()-t0))   # 08/27/2018 by kaibo
 
#通过获取某一区域的页数，来拼接某一页的链接 
def get_pages(area,area_link): 
    headers = { 
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'} 
    resposne = requests.get(area_link, headers=headers) 
    page_data = re.findall("page-data=\'{\"totalPage\":(\d+),\"curPage\"", resposne.text)    # 08/27/2018 by kaibo
    pages =  0 if not page_data else int(page_data[0])        # 08/27/2018 by kaibo
    print("这个区域有" + str(pages) + "页") 
    for page in range(1,pages+1): 
        t11 = time.time()
        url = '{}/zufang/{}/pg{}'.format(base_url, pinyin.get(area, format="strip"),str(page))     # 08/27/2018 by kaibo
        print("开始抓取[{}][page{}/{}]的信息".format(area, page, pages))    # 08/27/2018 by kaibo
        get_house_info(area,page,url) 
        print('{} page time: {:.5} s'.format('-'*10, time.time()-t11))  # 08/27/2018 by kaibo

#获取某一区域某一页的详细房租信息 
def get_house_info(area, page, url): 
    headers = { 
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'} 
    time.sleep(2) 
    try: 
        resposne = requests.get(url, headers=headers) 
        content = etree.HTML(resposne.text) 
        titles = content.xpath("//div[@class='where']/a/span/text()")   # 08/27/2018 by kaibo
        info=[] 
        #for i in range(30): 
        for i, title in enumerate(titles):                              # 08/27/2018 by kaibo
            #title = content.xpath("//div[@class='where']/a/span/text()")[i] 
            room_type = content.xpath("//div[@class='where']/span[1]/span/text()")[i] 
            square = re.findall("(\d+)",content.xpath("//div[@class='where']/span[2]/text()")[i])[0] 
            position = content.xpath("//div[@class='where']/span[3]/text()")[i].replace(" ", "") 
            try: 
                detail_place = re.findall("([\u4E00-\u9FA5]+)租房", content.xpath("//div[@class='other']/div/a/text()")[i])[0] 
            except Exception as e: 
                detail_place = "" 
            floor =re.findall("([\u4E00-\u9FA5]+)\(", content.xpath("//div[@class='other']/div/text()[1]")[i])[0] 
            total_floor = re.findall("(\d+)",content.xpath("//div[@class='other']/div/text()[1]")[i])[0] 
            try: 
                house_year = re.findall("(\d+)",content.xpath("//div[@class='other']/div/text()[2]")[i])[0] 
            except Exception as e: 
                house_year = "" 
            price = content.xpath("//div[@class='col-3']/div/span/text()")[i] 
            with open('rent_lianjia_{}.txt'.format(city),'a',encoding='utf-8') as f: 
                #f.write(area + ',' + title + ',' + room_type + ',' + square + ',' +position+ ','+ detail_place+','+floor+','+total_floor+','+price+','+house_year+'\n') 
                f.write('{},{},{},{},{},{},{},{},{},{}, {:.2f}\n'.format(area, title, room_type, square,position, detail_place,floor,total_floor,price,house_year, int(price)/int(square)))
 
            sys.stdout.write('writing work [{}][page{}#{}/{}] has done!continue the next page {}'.format(area,page,i+1,len(titles),'\r'))    # 08/27/2018 by kaibo
            if i < len(titles)-1: sys.stdout.flush()
            else: print('')
 
    except Exception as e: 
        print( 'ooops! connecting error, retrying.....') 
        time.sleep(20) 
        return get_house_info(area, page, url) 
 
 
def main(): 
    print('start!') 
    get_areas(base_url + '/zufang')
 
 
if __name__ == '__main__': 
    main() 
