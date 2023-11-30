import re
from bs4 import BeautifulSoup
import requests
from functions import clear_spaces_before_string
from functions import clear_after_comma_spaces
from functions import make_info_ready
from functions import remove_excess_newlines
from functions import remove_newline_at_the_end
from functions import remove_space_at_the_end
from functions import cut_string_in_half
import openpyxl


f = open('animeLinks.txt', 'r')
allAnimeDB = []
animelists = []
for i in f:
    animelists.append(i)
f.close()

k = 2
for i in animelists[151:201]:
    print('##########################################')
    anime = requests.get(i).text
    soup = BeautifulSoup(anime, 'html.parser')
    hmm = soup.find('div', class_='leftside').text

    aTitles = hmm[hmm.find('Alternative Titles'):hmm.find('More titles')].replace('  ',' ')


    print(remove_excess_newlines(aTitles))

    # chatgpt created this code
    # edited the hell out of it! :D
    input_text = str(hmm)  # Replace this with your actual input text

    # Define regular expressions for extracting information
    alternative_titles_pattern = r"Alternative Titles\n(.*?)\n\n"
    alternative_titles_pattern = r"Alternative Titles\n(.*?)\n"
    type_pattern = r"Type:\n(.*?)\n"
    episodes_pattern = r"Episodes:\n(.*?)\n"
    status_pattern = r"Status:(.*?)\n"
    aired_pattern = r"Aired:\n(.*?)\n"
    premiered_pattern = r"Premiered:\n(.*?)\n"
    broadcast_pattern = r"Broadcast:\n(.*?)\n"
    producers_pattern = r"Producers:\n(.*?)\n"
    licensors_pattern = r"Licensors:\n(.*?)\n"
    studios_pattern = r"Studios:\n(.*?)\n"
    source_pattern = r"Source:\n(.*?)\n"
    genres_pattern = r"Genres:\n(.*?)\n"
    theme_pattern = r"Themes?:\n(.*?)\n"
    duration_pattern = r"Duration?:\n(.*?)\n"
    demographic_pattern = r"Demographic:\n(.*?)\n"
    rating_pattern = r"Rating:\n(.*?)\n"

    # Extract information using regular expressions and handle NoneType
    def extract_info(pattern, text):
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return "Not found"

    # Print or use the extracted information
    # print("Alternative Titles")
    # print(extract_info(alternative_titles_pattern, input_text))
    # doesnt work!!!!

    print("\nType:")
    aType = make_info_ready(extract_info(type_pattern, input_text))
    print(aType)

    print("\nEpisodes:")
    aEpisodes = make_info_ready(extract_info(episodes_pattern, input_text))
    print(aEpisodes)

    # print("\nStatus:")
    # aStatus = make_info_ready(extract_info(status_pattern, input_text))
    # print(extract_info(status_pattern, input_text))
    # doesnt work for some reason... Bruh!

    index = input_text.find('Status')
    index += 10
    aStatus = input_text[index:]
    aStatus = aStatus[aStatus.find('Status'):aStatus.find('Aired')]
    aStatus = remove_excess_newlines(clear_spaces_before_string(aStatus))
    print('\n'+aStatus)


    print("\nAired:")
    aAired = make_info_ready(extract_info(aired_pattern, input_text))
    print(aAired)

    print("\nPremiered:")
    aPremiered = make_info_ready(extract_info(premiered_pattern, input_text))
    print(aPremiered)

    print("\nBroadcast:")
    aBroadcast = make_info_ready(extract_info(broadcast_pattern, input_text))
    print(aBroadcast)

    print("\nProducers:")
    aProducers = make_info_ready(extract_info(producers_pattern, input_text))
    print(aProducers)

    print("\nLicensors:")
    aLicensors = make_info_ready(extract_info(licensors_pattern, input_text))
    print(aLicensors)

    print("\nStudios:")
    aStudios = make_info_ready(extract_info(studios_pattern, input_text))
    print(aStudios)

    print("\nSource:")
    aSource = make_info_ready(extract_info(source_pattern, input_text))
    print(aSource)

    print("\nGenres:")
    aGenres = make_info_ready(extract_info(genres_pattern, input_text))
    print(aGenres)

    print("\nTheme(s):")
    aTheme = make_info_ready(extract_info(theme_pattern, input_text))
    print(aTheme)

    print("\nDemographic:")
    aDemog = make_info_ready(extract_info(demographic_pattern, input_text))
    print(aDemog)

    print("\nDuration:")
    aDuration = make_info_ready(extract_info(duration_pattern, input_text))
    print(aDuration)

    print("\nRating:")
    Rating = make_info_ready(extract_info(rating_pattern, input_text))
    print(Rating)

    s = remove_excess_newlines(aTitles)+'\n'
    s += "\nType:\n"+ aType+'\n'
    s += "\nEpisodes:\n"+ aEpisodes + '\n'
    s += "\nStatus:\n"+ aStatus + '\n'
    s += "\nAired:\n"+ aAired + '\n'
    s += "\nPremiered:\n"+ aPremiered + '\n'
    s += "\nBroadcast:\n"+ aBroadcast + '\n'
    s += "\nProducers:\n"+ aProducers + '\n'
    s += "\nLicensors:\n"+ aLicensors + '\n'
    s += "\nStudios:\n"+ aStudios + '\n'
    s += "\nSource:\n"+ aSource + '\n'
    # tempa = aGenres.split(',')
    # for i in range(len(tempa)):
    #     tempa[i] = tempa[i][:len(tempa)+1]
    s += "\nGenres:\n"+ aGenres + '\n'

    # tempa = aTheme.split(',')
    # for i in range(len(tempa)):
    #     tempa[i] = tempa[i][:len(tempa)+1]
    s += "\nTheme(s):\n"+ aTheme + '\n'
    
    # tempa = aDemog.split(',')
    # for i in range(len(tempa)):
    #     tempa[i] = tempa[i][:len(tempa)+1]
    s += "\nDemographic:\n"+ aDemog + '\n'
    s += "\nDuration:\n"+ aDuration + '\n'
    s += "\nRating:\n"+ Rating + '\n'
    # s += "\nRating:\n"+ Rating + '\n'
    a = s.split('\n\n')
    print(a[0][a[0].find('\n')+1:])

    for i in range(len(a)):
        a[i] = a[i][a[i].find('\n')+1:]
        if(a[i][:7]=='Status:'):
            a[i] = a[i][8:]

    print()


    
    for i in range(len(a)):
        # print("(("+a[i]+"))")
        a[i] = remove_space_at_the_end(remove_newline_at_the_end(a[i]))
        print("(("+a[i]+"))")



    # Genres cleaning
    b = a[11].split(',')
    temps = ""
    for i in range(len(b)):
        if b[i]!= "Not found":
            temps = temps + cut_string_in_half(b[i]) + ','
        else:
            temps = temps + b[i] + ','
    temps = temps[:-1]
    print(temps)
    a[11] = temps


    # Themes Cleaning
    b = a[12].split(',')
    temps = ""
    for i in range(len(b)):
        if b[i]!= "Not found":
            temps = temps + cut_string_in_half(b[i]) + ','
        else:
            temps = temps + b[i] + ','
    temps = temps[:-1]
    print(temps)
    a[12] = temps


    # Demographic cleaning
    b = a[13].split(',')
    temps = ""
    for i in range(len(b)):
        if b[i]!= "Not found":
            temps = temps + cut_string_in_half(b[i]) + ','
        else:
            temps = temps + b[i] + ','
    temps = temps[:-1]
    print(temps)
    a[13] = temps


    allAnimeDB.append(a)





workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = 'Titles'
sheet['B1'] = 'Type'
sheet['C1'] = 'Episodes'
sheet['D1'] = 'Status'
sheet['E1'] = 'Aired'
sheet['F1'] = 'Premiered'
sheet['G1'] = 'Broadcast'
sheet['H1'] = 'Producers'
sheet['I1'] = 'Licensors'
sheet['J1'] = 'Studios'
sheet['K1'] = 'Source'
sheet['L1'] = 'Genres'
sheet['M1'] = 'Themes'
sheet['N1'] = 'Duration'
sheet['O1'] = 'Demographic'
sheet['P1'] = 'Rating'

k=2
for a in allAnimeDB:
    for index, value in enumerate(a, start=2):
        sheet.cell(row=k, column=index-1, value= value)
    k+=1

    

    

workbook.save('animeDB4.xlsx')