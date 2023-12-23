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