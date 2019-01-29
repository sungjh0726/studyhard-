from bs4 import BeautifulSoup


html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>
        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

col_names = {'국적': 'nation', '활동장르': 'genre', '데뷔': 'debut', '수상이력':'award'}

soup = BeautifulSoup(html, 'html.parser')
dl = soup.select_one('dl')
dts = []
dds = []
for i,d in enumerate(dl):
    if not d.name: continue

    if d.name == 'dt':
        print(d.name)
        dts.append(col_names[d.text])
    else:
        span = d.select_one('span')
        if span != None:
            slcs = span.text.split('|')
            if len(slcs) <= 1: 
                slc =span.next.strip()
                dds.append(slc)
                continue
            
            else:
                slc = slcs[0].strip() + '|' + slcs[1].strip()
                dds.append(slc)
        else:
            dds.append(d.text)

sql = "insert into Singer(" + ", ".join(col_names.values()) + ") values('" + "', '".join(dds) + "')"
print(sql)
