import requests

a = requests.get("https://www.imdb.com/title/tt0111161/?ref_=chttp_i_1").text
print(a)