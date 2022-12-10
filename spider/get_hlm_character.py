#!/usr/bin/env python
# coding:utf8

from urllib import request
from urllib.parse import quote
import  string
import time
import json
from bs4 import BeautifulSoup
import codecs
from get_character_array import get_character
import os
if not os.path.exists("./spider/images"):
		os.mkdir("./spider/images")

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def get_json(character_arr):
	data={}
    #用于获取每个人物的百科网页详情
	for i in set(character_arr):
		print(i)
		url=r'https://baike.baidu.com/item/'+i
        #urllib.parse中的quote方法能够将汉字转换成unicode编码的格式,适用于单个参数
		url = quote(url, safe = string.printable)
		req = request.Request(url, headers=headers)
		response = request.urlopen(req, timeout=20)
		
		try:
			html = response.read().decode('utf-8')
			soup = BeautifulSoup(html, 'html.parser', )
			res = soup.find(class_="summary-pic")
			pic_name = str(i) + '.jpg'
			img_src = res.find('img').get('src')
			request.urlretrieve(img_src,pic_name)
		except :
			print("找不到图片")
		res_key=soup.find_all(class_ ="basicInfo-item name")
		res_val=soup.find_all(class_ ="basicInfo-item value")
		key=[ik.get_text().strip().replace("\n","、") for ik in res_key]
		value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]
		item=dict(zip(key,value))
		data[str(i)]=item
	if not os.path.exists("../json"):
		os.mkdir("../json")
	f = codecs.open('../json/data.json','w','utf-8')
	f.write(json.dumps(data,  ensure_ascii=False))
if __name__ == "__main__":
	character_arr=get_character()
    #os.chdir()方法用于改变当前工作目录到指定的路径
    #os.path.join()函数用于路径拼接文件路径,可以传入多个路径
        #从后往前看,会从第一个以"/"开头的参数开始拼接,之前的参数全部丢弃
        #以上一种情况为先.在上一种情况确保情况下,若出现"./"开头的参数,会从"./"开头的参数的前面参数全部保留
    #os.getcwd()的功能是获得当前文件的路径
	os.chdir(os.path.join(os.getcwd(), './spider/images'))
	get_json(character_arr)
