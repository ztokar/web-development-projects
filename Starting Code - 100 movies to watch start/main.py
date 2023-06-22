import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

movie_list=requests.get(URL)
movie_list_txt=movie_list.text

soup=BeautifulSoup(movie_list_txt,"html.parser")
titles=soup.select(selector=".title")
top100=titles[::-1][0:100]

# str ='<h3 class="title">'
with open("top100.txt", "w") as file:
        for movie in top100:
            file.write(movie.getText())
# cleaned_list=[movie.replace(str,"") for movie in top100]
