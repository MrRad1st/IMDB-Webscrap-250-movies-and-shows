# import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from functions import extract_info

# initialize web driver and go to the link
driver = webdriver.Edge()
driver.get("https://www.imdb.com/chart/top/")
time.sleep(1) #in case the page elements don't fully load at first

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# get the page source from the driver
movies_page = driver.page_source
# close the web driver
driver.quit()

# parse the html code
soup = BeautifulSoup(movies_page, 'html.parser')
# find the link elements for the top 250 movies
movies_elements = soup.find_all('a', class_="ipc-lockup-overlay ipc-focusable")

# use regular expressions to get the links to the top 250 movies
links_of_the_movies = []
link_pattern = r'href="(.*?)"'
for element in movies_elements:
    short_link = extract_info(link_pattern,str(element))
    print(short_link)
    links_of_the_movies.append("https://www.imdb.com"+short_link)
    
    
movies_file = open("movies_links.txt", 'w')
for link in links_of_the_movies:
    movies_file.write(link+'\n')

movies_file.close()




# animeVar = 0
# animeVarMax = 1000
# AnimeLinksStr = ""


# while animeVar < animeVarMax:
#     animes = requests.get("https://myanimelist.net/topanime.php?limit="+str(animeVar)).text

#     soup = BeautifulSoup(animes, 'html.parser')
#     tr_elements = soup.find_all('tr', class_='ranking-list')

#     for tr in tr_elements:
#         a_element = tr.find('a', class_='hoverinfo_trigger')
#         if a_element:
#             href = a_element.get('href')
#             href = str(href.encode("utf-8"))
#             AnimeLinksStr = AnimeLinksStr + href[2:-1] + "\n"
#             print(href)

#     animeVar+=50

# f = open("animeLinks.txt","w")
# # AnimeLinksStr = AnimeLinksStr.encode('utf-8')
# f.write(str(AnimeLinksStr))
# f.close()






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