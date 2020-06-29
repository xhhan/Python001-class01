#!/usr/bin/python
#-coding:utf-8--

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

def get_movie_url():
    links = []
    url = "https://maoyan.com/films?showType=3"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)

    bs_info = bs(response.text,'html.parser')
    for tags in bs_info.find_all("div", attrs={"class": "movie-item film-channel"}):
        links.append("https://maoyan.com"+str(tags.find('a',).get('href')))
    return links

def get_movie_info(urls):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header = {'user-agent': user_agent}
    files_info = []
    for i in range(0, 10):
        url = urls[i]
        types = ''
        file_date = ''
        file_info = []
        print("request "+url+" ,ing......")
        response = requests.get(url, headers=header)
        bs_info = bs(response.text, 'html.parser')
        file_name = bs_info.find_all('h1',attrs={'class':'name'})[0].text
        for info in bs_info.find_all('li',attrs={'class': 'ellipsis'}):
            #print(info)
            for atags in info.find_all('a',):
                types = str(atags.text)+'/'+types
            file_date = info.text
        file_info=[file_name, types, file_date]
        files_info.append(file_info)
        sleep(1)
    return files_info

def write_to_csv(data):
    movie = pd.DataFrame(data)
    movie.to_csv(path_or_buf='./movies.csv', header=False, encoding='utf8', index=False)




if __name__ == '__main__':
    #url1 = 'https://maoyan.com/films/1250952'
    #url2 = 'https://maoyan.com/films/1218273'
    #urls = [url1, url2]
    #get_movie_info(urls)
    urls = get_movie_url()
    data = get_movie_info(urls)
    #print(urls)
    write_to_csv(data)


