import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# data = requests.get("https://www.facebook.com/pg/modernwomenintheworld/videos/") 
driver = webdriver.Chrome()
x = driver.get("https://www.facebook.com/pg/modernwomenintheworld/videos/?ref=page_internal")

data = requests.get("https://www.facebook.com/pg/modernwomenintheworld/videos/") 

html = data.content.decode()


soup = bs4.BeautifulSoup(html, "html.parser")

ds_bai_viet = soup.find_all('div', {'class': '_2t3c'})
print(ds_bai_viet)
exit()
ket_qua = [] 
for v in ds_bai_viet:
    bai_viet = {} 
    bai_viet['link'] = v.span.attrs["href"] 
    
    ket_qua.append(bai_viet) 

print(ket_qua)
                      


# driver = webdriver.Chrome()

driver.close()
