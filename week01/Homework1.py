#!/usr/bin/python
#-coding:utf-8--

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

def get_movie_url():
    links = []
    url = "https://movie.douban.com/top250?start=0"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)

    bs_info = bs(response.text,'html.parser')
    for tags in bs_info.find_all("div", attrs={"class": "hd"}):
        for atag in tags.find_all("a", ):
            links.append(atag.get("href"))
    return links

def get_movie_info(urls):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header = {'user-agent': user_agent}
    files_info = []
    for url in urls:
        types = ''
        file_date = ''
        file_info = []
        print("request "+url+" ,ing......")
        response = requests.get(url, headers=header)
        bs_info = bs(response.text, 'html.parser')
        file_name = bs_info.find_all('span',attrs={'property':'v:itemreviewed'})[0].text
        for type in bs_info.find_all('span',attrs={'property':'v:genre'}):
            types = types+'/'+str(type.text)
        for f_date in bs_info.find_all('span',attrs={'property':'v:initialReleaseDate'}):
            file_date = file_date+'/'+str(f_date.text)
        file_info=[file_name, types, file_date]
        files_info.append(file_info)
        sleep(1)
    return files_info

def write_to_csv(data):
    movie = pd.DataFrame(data)
    movie.to_csv(path_or_buf='./movies.csv', header=False, encoding='utf8', index=False)




if __name__ == '__main__':
    #url1 = 'https://movie.douban.com/subject/3319755'
    #url2 = 'https://movie.douban.com/subject/6786002'
    #urls = [url1, url2]
    #get_movie_info(urls)
    urls = get_movie_url()
    data = get_movie_info(urls)
    print(data)
    write_to_csv(data)


