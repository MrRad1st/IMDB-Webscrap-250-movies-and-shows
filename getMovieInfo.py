from bs4 import BeautifulSoup
from selenium import webdriver
import time
from functions import extract_info
from functions import space_between_words

movies_file = open("movies_links.txt", 'r')
movies_links_list = []
for link in movies_file:
    movies_links_list.append(link)
movies_file.close()


for movie_link in movies_links_list:
    # initialize web driver and go to the link
    driver = webdriver.Edge()
    driver.get(movie_link)
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

    # year = soup.find('a', class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color").text

    print(title)
    info = info[-2:]
    for i in range(len(info)):
        print(info[i].text)
        info[i] = info[i].text

    year = info[0]
    age_rating = info[1]

    rating = soup.find('span', class_="sc-bde20123-1 cMEQkK").text
    # print(rating)
    genres = soup.find_all('span', class_="ipc-chip__text")
    genres = genres[:-1]
    # print(genres)
    for i in range(len(genres)):
        genres[i] = genres[i].text

    genres_out = ""
    for genre in genres:
        genres_out = genres_out + genre + ','
    genres_out = genres_out[:-1]
    # print(genres_out)

    summary = soup.find('span', class_="sc-466bb6c-1 dWufeH").text
    # print(summary)

    image = soup.find('img').find_next('img')
    # print(image)
    str_img = str(image)
    str_img = str_img[str_img.find("https")+5:]
    str_img = str_img[str_img.find("https")+5:]
    str_img = str_img[str_img.find("https")+5:]

    str_img = str_img[str_img.find("https"):]
    str_img = str_img[:str_img.find(".jpg")+4]

    # print(str_img) okay shod

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

    f = open('moviesDB/'+title+'_'+year+'.txt','w')
    f.write("Title: "+title + '\n')
    f.write("Year of release: " + year + '\n')
    f.write("Age Rating: " + age_rating + '\n')
    f.write("Popularity Rating: " + rating + '\n')
    f.write("Genres: " + genres_out + '\n')
    f.write("Summary: " + summary + '\n')
    f.write("Director: " + space_between_words(director) + '\n')
    f.write("Writers: " + space_between_words(writers) + '\n')
    f.write("Stars: " + space_between_words(stars) + '\n')
    f.write("Language: " + Language + '\n')
    f.write("Runtime: " + runtime + '\n')
    f.write("Budget: " + budget + '\n')
    f.write("Gross Worldwide: " + gross_worldwide)

    f.close()
    # print(space_between_words(director))
    # print(space_between_words(writers))
    # print(space_between_words(stars))
    # print(Language)
    # print(country_of_origin)
    # print(runtime)
    # print(budget)
    # print(gross_worldwide)

