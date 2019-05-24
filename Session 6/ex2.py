from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from pandas import DataFrame
import requests

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

# 1 . Download web page
data = requests.get(url)
html_content = data.content.decode()




with open('vinamilk.html', 'wt', encoding='utf-8') as f: 
    f.write(html_content)

# 2 . Extract ROI ( Region of interest )
soup = BeautifulSoup(html_content,"html.parser")
table = soup.find("table",id = "tableContent")

# 3 . Extract info
list_needed = []
td_list = table.find_all("td",{"class":"b_r_c"})

for i in range(0,len(td_list),6):
    dictionary = {}

    dictionary["Title"] = td_list[i].string
    dictionary["Quy 4 - 2016"] = td_list[i+1].string
    dictionary["Quy 1 - 2017"] = td_list[i+2].string
    dictionary["Quy 2 - 2017"] = td_list[i+3].string
    dictionary["Quy 3 - 2017"] = td_list[i+4].string
    
    list_needed.append(dictionary)

df = DataFrame(list_needed, columns = ["Title","Quy 4 - 2016","Quy 1 - 2017","Quy 2 - 2017","Quy 3 - 2017"])

df.to_excel('vinamilk.xlsx',index=False)