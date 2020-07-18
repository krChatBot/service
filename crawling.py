from urllib.request import urlopen
from bs4 import BeautifulSoup

mood = input('기분: (우울, 기쁨)  ')

mood_dict = {'우울': '6161', '기쁨': '5729'}

html = urlopen("https://music.bugs.co.kr/musicpd?tag_id=" + mood_dict[mood])
bsObject = BeautifulSoup(html, "html.parser")

# tag_link = 'https://music.bugs.co.kr/musicpd?tag_id=' 
# album_link = 'https://music.bugs.co.kr/musicpd/albumview/' 
# crawl_album_list = []
# crawl_song_list = []

res = bsObject.find_all(attrs={'target':'_self'})
temp = []
links = []
for x in res:
    x = str(x).split(' ')
    for y in x:
        if 'href' in y:
            temp.append(str(y).replace('href=', '').replace('"',''))
for link in temp:
    if not ('pdlistdetail' in link or 'list_mab_03' in link):
        links.append(link)
        
for link in links:
    print(link)