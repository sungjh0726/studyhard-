from bs4 import BeautifulSoup
import requests
import re
import pprint
import pymysql
import time
import json
import melondb_func as mf

soup = mf.request_soup()
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

def get_album_data():
   
  
   albums = soup.select('div.ellipsis.rank03 > a')

   # print(albums)

   album_no_lst = []
   album_name_lst = []

   dic = {}

   for album in albums:
      
      
      album_no = album.get("href")
      sn = re.compile('goAlbumDetail\(\'(.*)\'.*')
      album_no2 = re.findall(sn, album_no)[0]
      #  print(album_no2)
      
      
      # print(album_no2)
      album_no_lst.append(album_no2)

      album_name = album.text
      # print(album_name)
      album_name_lst.append(album_name)

      dic[album_no2] = {'album_name': album_name}


   for i in album_no_lst:
      
   
      html = requests.get('http://vlg.berryservice.net:8099/melon/detail?albumId={}'.format(i), headers = headers)
      soup2 = BeautifulSoup(html.text, 'html.parser')

      # print(soup)
      
      publisher = soup2.select('#conts > div.section_info > div > div.entry > div.meta > dl > dt, dd')

      #  print(publisher)
      

      for j, element in enumerate(publisher):

         
         if publisher[j].text == "발매사":


            # print(publisher[j+1].text)
            # publisher_name_lst.append(publisher[j+1].text)

            dic[i]['publisher'] = publisher[j+1].text


   for i in album_no_lst:

      likeUrl = "http://vlg.berryservice.net:8099/melon/albumlikejson?albumId={}".format(i)
      rateUrl = " http://vlg.berryservice.net:8099/melon/albumratejson?albumId={}".format(i)
      
      likeParams = {
      "contsIds": "i"
      }
      rateParams = {
      "albumId" : "i"
      }

      resLikecnt = requests.get(likeUrl, headers=headers, params=likeParams)
      resRating = requests.get(rateUrl, headers=headers, params=rateParams) 
      # print(resLikecnt.url)
      jsonData1 = json.loads(resLikecnt.text)
      jsonData2 = json.loads(resRating.text)
      # pprint(jsonData)
      dic[i]['likecnt'] = jsonData1['contsLike'][0]['SUMMCNT']
      dic[i]['rating'] = round(float(jsonData2["infoGrade"]['TOTAVRGSCORE']))


   
   album_insert_lst = []

   for i in album_no_lst:
      album_insert_lst.append([i, dic[i]['album_name'], dic[i]['publisher'], dic[i]['likecnt'], dic[i]['rating']])

   return album_insert_lst
