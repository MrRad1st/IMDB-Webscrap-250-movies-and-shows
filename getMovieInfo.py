from bs4 import BeautifulSoup
from selenium import webdriver
import time
from functions import space_between_words
import openpyxl
import requests


movies_file = open("movies_links.txt", 'r')
movies_links_list = []
for link in movies_file:
    movies_links_list.append(link)
movies_file.close()

all_movie_db = []

for movie_link in movies_links_list:
    # initialize web driver and go to the link
    driver = webdriver.Edge()
    driver.get(movie_link)
    driver.minimize_window()
    time.sleep(2) #in case the page elements don't fully load at first

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # get the page source from the driver
    movies_page = driver.page_source
    # close the web driver
    driver.quit()

    soup = BeautifulSoup(movies_page, 'html.parser')
    title = soup.find('span', class_="hero__primary-text").text
    info = soup.find_all('a', class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color")

    print(title)
    info = info[-2:]
    for i in range(len(info)):
        print(info[i].text)
        info[i] = info[i].text

    year = info[0]
    age_rating = info[1]

    rating = soup.find('span', class_="sc-bde20123-1 cMEQkK").text
    genres = soup.find_all('span', class_="ipc-chip__text")
    genres = genres[:-1]
    for i in range(len(genres)):
        genres[i] = genres[i].text

    genres_out = ""
    for genre in genres:
        genres_out = genres_out + genre + ','
    genres_out = genres_out[:-1]

    summary = soup.find('span', class_="sc-466bb6c-1 dWufeH").text

    image = soup.find('img').find_next('img')
    str_img = str(image)
    str_img = str_img[str_img.find("https")+5:]
    str_img = str_img[str_img.find("https")+5:]
    str_img = str_img[str_img.find("https")+5:]

    str_img = str_img[str_img.find("https"):]
    str_img = str_img[:str_img.find(".jpg")+4]
    
    print()
    print()
    print()
    print()
    print()
    print()
    print(str_img)
    print()
    print()
    print()
    print()
    print()


    movie_info = soup.find_all('li', class_="ipc-metadata-list__item")
    for i in range(len(movie_info)):
        movie_info[i] = movie_info[i].text

    director = movie_info[0][movie_info[0].find("Director")+len("Director"):]
    writers = movie_info[1][movie_info[1].find("Writers")+len("writers"):]
    stars = movie_info[2][movie_info[2].find("Stars")+len("stars"):]

    Language = "Not Found"
    country_of_origin = "Not Found"
    runtime = "Not Found"
    budget = "Not Found"
    gross_worldwide = "Not Found"

    for item in movie_info:
        if item.find("Language") == 0:
            Language = item[item.find("Language")+len("Language"):]
        if item.find("Country of origin") == 0:
            country_of_origin = item[item.find("Country of origin")+len("Country of origin"):]
        if item.find("Runtime") == 0:
            runtime = item[item.find("Runtime")+len("Runtime"):]
        if item.find("Budget") == 0:
            budget = item[item.find("Budget")+len("Budget"):]
        if item.find("Gross worldwide") == 0:
            gross_worldwide = item[item.find("Gross worldwide")+len("Gross worldwide"):]

    a = []
    a.append(title)
    a.append(year)
    a.append(age_rating)
    a.append(rating)
    a.append(genres_out)
    a.append(summary)
    a.append(space_between_words(director))
    a.append(space_between_words(writers))
    a.append(space_between_words(stars))
    a.append(Language)
    a.append(runtime)
    a.append(budget)
    a.append(gross_worldwide)
    a.append(str_img)
    
    response = requests.get(a[-1])
    # Check if the request is successful
    if response.status_code == 200:
        # Open the file in write mode, write the image into the file, and then close it
        file = open('images/'+title+'_'+year+'.jpg', 'wb')
        file.write(response.content)
        file.close()

    all_movie_db.append(a)


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = 'Title'
sheet['B1'] = 'Year of release'
sheet['C1'] = 'Age Rating'
sheet['D1'] = 'Popularity Rating'
sheet['E1'] = 'Genres'
sheet['F1'] = 'Summary'
sheet['G1'] = 'Director'
sheet['H1'] = 'Writers'
sheet['I1'] = 'Stars'
sheet['J1'] = 'Language'
sheet['K1'] = 'Runtime'
sheet['L1'] = 'Budget'
sheet['M1'] = 'Gross Worldwide'
sheet['N1'] = 'Banner'

i=2
for movie in all_movie_db:
    for index, value in enumerate(movie, start=2):
        sheet.cell(row=i, column=index-1, value= value)
    i+=1
    
workbook.save("movies_db.xlsx")