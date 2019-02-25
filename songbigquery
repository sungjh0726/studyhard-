import pymysql
import bigquery
import sys


def get_conn(db):
    return pymysql.connect(
        host='35.243.112.23',
        user='root',
        password='eileen',
        port=3306,
        db=db,
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

conn = get_conn('melondb')


with conn:
    cur = conn.cursor()

    # Song table 데이터 가져오기
    song_sql = "select s.song_no, s.title, s.genre, a.album_id from MS_Song s inner join Album a on s.album_id = a.album_id "
    cur.execute(song_sql)
    songs = cur.fetchall()

    print ("Song data collected")

    # Ablum table 데이터 가져오기
    album_sql = '''select album_id, album_title, album_genre, 
                cast(rating as char(30)) as rating,
                cast(releasedt as char(30)) as releasedt,
                album_comp, entertainment,
                cast(crawldt as char(30)) as crawldt from Album'''
    cur.execute(album_sql)
    albums = cur.fetchall()

    print ("Album data collected")

    # albumid 가져오기
    albumids = []
    for i in albums:
        albumid = i['album_id']
        albumids.append(albumid)

    # songs에 albumdetail이라는 key를 만들고 value값으로 album 데이터 집어넣기
    albumdetail = {}
    for i in range(len(albumids)):
        albumdetail[albumids[i]] = albums[i]

    for song in songs:
        song['albumdetail'] = albumdetail[song['album_id']]
    

# # ---------------------bigquery--------------------------------


client = bigquery.get_client(json_key_file='../../bigquery.json', readonly = False)
print("identification success")

DATABASE='bqdb'
TABLE='Songs'

if not client.check_table(DATABASE, TABLE):
    print("Create table {}.{}".format(DATABASE, TABLE, file = sys.stderr))

    client.create_table(DATABASE, TABLE, [
        {'name': 'song_no', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'genre', 'type': 'string', 'description': 'song genre'},
        {'name': 'album_id', 'type':'string', 'description': 'album id'},
        {'name': 'albumdetail', 'type': 'record', 'description': 'album detail',
          'fields': [{'name': 'album_id', 'type': 'string'},
                     {'name': 'album_title', 'type': 'string'},
                     {'name': 'album_genre', 'type': 'string'},
                     {'name': 'rating', 'type': 'float', 'description': 'album rating'},
                     {'name': 'releasedt', 'type':'date'},
                     {'name': 'album_comp', 'type':'string'},
                     {'name': 'entertainment', 'type':'string'},
                     {'name': 'crawldt', 'type':'timestamp'}

                    ]}])

pushResult = client.push_rows(DATABASE, TABLE, songs, insert_id_key='song_no')
print("Pushed Result is", pushResult)
