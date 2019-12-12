import re 
import urllib  
import urllib.request  
import urllib.parse
import requests
import time


def get_data_urllib(url):
    urlop = None
    while urlop is None:
        try:
            urlop = urllib.request.urlopen(url, timeout=2)
        except:
            pass
            #return None
    if 'html' not in urlop.getheader('Content-Type'):
        return None
    try:
        this_data = urlop.read()
    except:
        return None
    try:
        if 'UTF-8' in urlop.getheader('Content-Type') or 'utf-8' in urlop.getheader('Content-Type'):
            data = this_data.decode("UTF-8")
        elif 'GBK' in urlop.getheader('Content-Type') or 'gbk' in urlop.getheader('Content-Type'):
            data = this_data.decode("GBK")
        else:
            data = this_data.decode("UTF-8")
    except:
        return None
    return data


def get_data_requests(url):
    data = requests.get(url)
    # if data.status_code != 200:
    #     print('Error status code: {} for url: {}'.format(data.status_code, url)) 
    #     continue
    while data.status_code != 200:
        data = requests.get(url)
    try:
        data = data.content.decode("utf-8")
    except:
        return None
    return data

 
lego_list = {'wmt': [
                  (10247, 200, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Ferris-Wheel-10247/42104279'),
                  (10257, 200, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Carousel-10257/55126277'),
                  (10261, 380, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Roller-Coaster-10261/508328879'),
                  (10214, 240, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Tower-Bridge-10214-4-295-Pieces/23763794'),
                  (10243, 160, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Parisian-Restaurant-10243/34228382'),
                  (10251, 170, 'https://www.walmart.com/ip/Lego-Creator-Expert-Brick-Bank-10251-2-380-Pieces/47335729'),
                  (10255, 280, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Assembly-Square-10255/55126227'),
                  (10260, 170, 'https://www.walmart.com/ip/LEGO-Creator-Expert-Downtown-Diner-10260/527744244'),
                  (42055, 280, 'https://www.walmart.com/ip/LEGO-Technic-Bucket-Wheel-Excavator-42055-Construction-Toy/51720901'),
                  (42069, 180, 'https://www.walmart.com/ip/LEGO-Technic-Extreme-Adventure-42069/55126273'),
                  (42070, 280, 'https://www.walmart.com/ip/LEGO-Technic-6x6-All-Terrain-Tow-Truck-42070/55126274'),
                  (42078, 180, 'https://www.walmart.com/ip/LEGO-Technic-Mack-Anthem-42078-Building-Set-2-595-Piece/295990632'),
                  (42082, 300, 'https://www.walmart.com/ip/LEGO-Technic-Rough-Terrain-Crane-42082/503907361'),
                  (42083, 350, 'https://www.walmart.com/ip/LEGO-Technic-Bugatti-Chiron-42083/916941084'),
                  (42099, 250, 'https://www.walmart.com/ip/LEGO-Technic-4X4-X-treme-Off-Roader-42099-Toy-Truck-STEM-Toy-958-Pieces/766301697'),
                  (42110, 200, ''),
                   ],
             'amz': [
                  (10247, 200, 'https://www.amazon.com/LEGO-Creator-Expert-Ferris-Construction/dp/B00X6A8VWA'),
                  (10257, 200, 'https://www.amazon.com/LEGO-Creator-Expert-Carousel-Building/dp/B072MHYHXJ'),
                  (10261, 380, 'https://www.amazon.com/LEGO-Creator-Expert-Coaster-Building/dp/B07GXYMCMV'),
                  (10214, 240, 'https://www.amazon.com/LEGO-6038577-Tower-Bridge-10214/dp/B003Q6BQOY'),
                  (10243, 160, 'https://www.amazon.com/LEGO-Creator-10243-Parisian-Restaurant/dp/B00HQIZBE4'),
                  (10251, 170, 'https://www.amazon.com/LEGO-Creator-Expert-Brick-Construction/dp/B01A85FXBC'),
                  (10255, 280, 'https://www.amazon.com/LEGO-Creator-Expert-Assembly-Building/dp/B01NBP28HQ'),
                  (10260, 170, 'https://www.amazon.com/LEGO-Creator-Downtown-Building-Assembly/dp/B0787JFG5Q'),
                  (42055, 280, 'https://www.amazon.com/LEGO-Technic-Bucket-Excavator-Construction/dp/B01CU9X8AC'),
                  (42069, 180, 'https://www.amazon.com/LEGO-Technic-Extreme-Adventure-Building/dp/B0725KD9VD'),
                  (42070, 280, 'https://www.amazon.com/LEGO-Technic-Terrain-Truck-Building/dp/B07146N1MP'),
                  (42078, 180, 'https://www.amazon.com/LEGO-Technic-Building-Engineering-Teenagers/dp/B075SD9MJG'),
                  (42082, 300, 'https://www.amazon.com/LEGO-Technic-Rough-Terrain-Building/dp/B07CFNCSC7'),
                  (42083, 350, 'https://www.amazon.com/LEGO-Technic-Building-Engineering-Collectible/dp/B07C8L9CRJ'),
                  (42099, 250, 'https://www.amazon.com/LEGO-Technic-X-treme-Off-Roader-Building/dp/B07NRT9GYG'),
                  (42110, 200, 'https://www.amazon.com/LEGO-Technic-Defender-Building-Pieces/dp/B07VFDRT8B'),
                    ]
            }

idx_to_name = {
               10247: 'Ferris Wheel',
               10257: 'Carousel',
               10261: 'Roller Coaster',
               10260: 'Downtown Diner',
               10214: 'Tower Bridge',
               10243: 'Parisian Restaurant',
               10251: 'Brick Bank',
               10255: 'Assembly Square',
               42055: 'Bucket Wheel Excavator 斗轮挖掘机',
               42069: 'Extreme Adventure 极限履带越野车',
               42070: '6x6 All Terrain Tow Truck 全地形卡车',
               42078: 'Technic Mack Anthem',
               42082: 'Rough Terrain Crane 复杂地形起重机',
               42083: 'Bugatti Chiron 布加迪奇龙',
               42099: '4x4 X-Treme Off-Roader 遥控越野车',
               42110: 'Land Rover Defender 路虎守卫者',
              }
pattern_p = {'wmt':r'id="price".+?>(\$[\d\.]+?)</span>',
             'amz':r'id="priceblock_ourprice".+?>(\$[\d\.]+?)</span>'
            }

pattern_t = r'link rel="canonical" href="(.+?)"/>'

if __name__ == '__main__':
    print(time.asctime())
    for seller, urls in lego_list.items():
        print(seller)
        #if seller == 'wmt': continue
        for idx, msrp, url in urls:
            if url == '': continue
            #if idx != 10214: continue
            data = get_data_urllib(url)
            if data == None:
                data = get_data_requests(url)
            if data == None:
                print('no data for url: {}'.format(url)) 
                continue
            match = re.findall(pattern_p[seller], data)

            if len(match) == 0:
                pattern = r'id="priceblock_pospromoprice".+?>(\$[\d\.]+?)</span>'
                match = re.findall(pattern, data)
            if len(match) != 0:
                p = float(match[0][1:])
                #print('{}\t${}\t${}\t{}'.format(url.split('/')[-2], p, msrp, '✓' if msrp - p >=1 else ' '))
            else:
                pattern = r'id="availability".+?>(.+?)</span>'
                match = re.findall(pattern, data.replace('\n',''))
                #print(match)
                if len(match) > 0 and 'Available from' in match[0]:
                    p = 'OOS'
                else: 
                    print('no info for url: {}'.format(url)) 
                    continue

            print('{}\t{}\t${}\t{} - {}\t\t\t{}'.format('✓' if (isinstance(p, (int, float)) and msrp - p >= 2) else ' ', p if p=='OOS' else '$'+str(p), msrp, idx, idx_to_name[idx], url))

