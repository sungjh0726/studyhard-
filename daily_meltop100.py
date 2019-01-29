from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep
from pprint import pprint
import json
import melondb_func as mf

soup = mf.request_soup()

def get_songsing_data():

    trs = soup.select('div#tb_list table tbody tr[data-song-no]')
    Song = {}

    for tr in trs:
        song_no = tr.attrs['data-song-no']                     ## 곡 번호
        # title = tr.select_one('div.ellipsis.rank01 a').text    ## 곡 제목
        
        singers = tr.select('div.ellipsis.rank02 span a')
        # singer_group = ",".join([a.text for a in singers])    ## 가수 묶음
        
        for singer in singers:
            
            singer_no_lst = []
            singer_name_lst = []
            
            singer_no = singer.get("href")
            sn = re.compile('goArtistDetail\(\'(.*)\'.*')
            singer_no2 = re.findall(sn, singer_no)[0]          ## 가수 번호(여러명 리스트에 추가)
            singer_no_lst.append(singer_no2)
            
            # singer_name = singer.text                          ## 가수 이름(여러명 리스트에 추가)
            # singer_name_lst.append(singer_name)
            
            
        
        Song[song_no] = {'singer_group': singer_no_lst}

    pprint(Song)


    songsing_insert_lst = []



    for k in Song.keys():
        for i in range(len(Song[k]['singer_group'])):
            songsing_insert_lst.append([k, Song[k]['singer_group'][i]])

    return songsing_insert_lst
