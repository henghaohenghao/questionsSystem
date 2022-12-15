

import socket
from urllib import request
import requests
from lxml import etree
from get_character_array import get_character
import os
import codecs
import json

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
      }
timeout = 10

def get_json(character_arr):
    data = {}
    for i in set(character_arr):
        print(i)
        url = r'https://baike.baidu.com/item/'+i
        socket.setdefaulttimeout(timeout)
        req = requests.get(url=url,headers=header,allow_redirects=True)
        req.encoding = 'utf-8'
        try:
            html = req.text
            response = etree.HTML(html)
            #获取人物图片
            pic_name = str(i) + '.jpg'
            img_src = response.xpath('//div[@class="summary-pic"]//img/@src')[0]
            request.urlretrieve(img_src,pic_name)
        except:
            print("找不到图片")
        res_key = response.xpath('//dt[@class="basicInfo-item name"]')
        res_val = response.xpath('//dd[@class="basicInfo-item value"]')
        key=[ik.text.strip().replace("\n","、") for ik in res_key]
        value = [iv.text.strip().replace("\n", "、") for iv in res_val]
        item = dict(zip(key,value))
        data[str(i)]=item
    f = codecs.open('../json/SG_data.json','w','utf-8')
    f.write(json.dumps(data,  ensure_ascii=False))
        

if __name__ == "__main__":
    character_arr=get_character()
    os.chdir(os.path.join(os.getcwd(), './images'))
    get_json(character_arr)