import bs4
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

request = requests.get(URL)


bs = BeautifulSoup(request.text, "html.parser")
bs.find(name='a' class)