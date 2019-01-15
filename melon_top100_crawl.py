import requests
from bs4 import BeautifulSoup
 
if __name__ == "__main__":
    RANK = 100
 
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    url = requests.get('https://www.melon.com/chart/index.htm', headers = header)
    lurl = "https://www.melon.com/commonlike/getSongLike.json"
    html = url.text
    parse = BeautifulSoup(html, 'html.parser')
 
    titles = parse.find_all("div", {"class": "ellipsis rank01"})
    songs = parse.find_all("div", {"class": "ellipsis rank02"})
 
    title = []
    song = []
 
    for t in titles:
        title.append(t.find('a').text)
 
    for s in songs:
        song.append(s.find('span', {"class": "checkEllipsis"}).text)
 
    for i in range(RANK):
        print('%3d위: %s - %s'%(i+1, title[i], song[i]))

html = requests.get(url).text

jsonData = json.loads(html)

params = {
	"contsIds": ",".join(list(dic.keys()))
}

jsonRes = requests.get(lurl, headers = headers, params=params)
print(jsonRes.url)
jsonData = json.loads(jsonRes.text)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for j in jsonData['contsLike']:
	contsid = j['CONTSID']
	likecnt = j['SUMMCNT']
	print(contsid, likecnt)
	dic[str(contsid)]['likecnt'] = likecnt


pprint.pprint(dic)





      
            
