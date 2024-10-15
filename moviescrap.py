import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data ,"html.parser")
tag = soup.find_all("h3", class_="title")
with open("projects/web/movie.txt","w", encoding="utf-8") as data:
    for i in tag[::-1]:
        tag1 = i.getText()
        data.write(f"{tag1} \n")