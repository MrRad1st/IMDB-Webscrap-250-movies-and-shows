# import re
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import requests
# import time
from bs4 import BeautifulSoup

# driver = webdriver.Firefox()
# driver.minimize_window()
animeVar = 0
animeVarMax = 1000


# soup = BeautifulSoup(a, 'html.parser')
# tr_elements = soup.find_all('tr', class_='ranking-list')
# 
# for tr in tr_elements:
    # a_element = tr.find('a', class_='hoverinfo_trigger')
    # if a_element:
        # href = a_element.get('href')
        # print(href)


AnimeLinksStr = ""


while animeVar < animeVarMax:
    animes = requests.get("https://myanimelist.net/topanime.php?limit="+str(animeVar)).text

    soup = BeautifulSoup(animes, 'html.parser')
    tr_elements = soup.find_all('tr', class_='ranking-list')

    for tr in tr_elements:
        a_element = tr.find('a', class_='hoverinfo_trigger')
        if a_element:
            href = a_element.get('href')
            href = str(href.encode("utf-8"))
            AnimeLinksStr = AnimeLinksStr + href[2:-1] + "\n"
            print(href)

    animeVar+=50

f = open("animeLinks.txt","w")
# AnimeLinksStr = AnimeLinksStr.encode('utf-8')
f.write(str(AnimeLinksStr))
f.close()






# soup = BeautifulSoup(driver.page_source,'html.parser')
# links = soup.find_all(name='a')
# #links = links[:75] # the last link in the demographics category
# f = open("genreLinks.txt", "w")
# index = 0
# for i in links:
#     if "genre-name-link" in str(i) and index<76:
#         # print(i)
#         x = re.split('"', str(i))
#         text = str(x[3])
#         pattern = r'([^/]+)$'

#         match = re.search(pattern, text)

#         if match:
#             action = match.group(1)
#         f.write(action + ",https://myanimelist.net" +str(x[3])+'\n')
#         index+=1
    
# driver.close()
# f.close()