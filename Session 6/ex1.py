from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame
from youtube_dl import YoutubeDL
import requests
# import pyexcel

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)

url = 'https://www.apple.com/itunes/charts/songs/'

# 1 . Download web page
data = requests.get(url)
html_content = data.content.decode()

# 2 . Extract ROI ( Region of interest )
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section",{"class":"section chart-grid"})

# 3 . Extract info
list_of_song = []
li_list = section.find_all("li")

for li in li_list:
    h3 = li.h3
    h4 = li.h4
  
    dictionary = {} 
    dictionary["Name"] = h3.string
    dictionary["Artist"] = h4.string
    list_of_song.append(dictionary)

    # download = h3.string + " " + h4.string
    # dl.download([download])


# pyexcel.save_as(records=list_of_song, dest_file_name="itunes_top100.xlsx")


df = DataFrame(list_of_song, columns = ['Name','Artist'])
df.to_excel('top_itunes.xlsx',index=False)