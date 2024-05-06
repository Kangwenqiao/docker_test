import requests
from bs4 import BeautifulSoup
import csv
import time

def get_douban_comments(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        comments = soup.find_all('span', class_='short')
        return [comment.text.strip() for comment in comments]
    else:
        print('Failed to fetch comments.')
        return []

def crawl_and_print_comments(url):
    comments = get_douban_comments(url)
    if comments:
        print("===== 评论开始 =====")
        for comment in comments:
            print(comment)
        print("===== 评论结束 =====")

def main():
    url = 'https://movie.douban.com/subject/35593344/'  # 《奥本海默》在豆瓣的网址

    while True:
        crawl_and_print_comments(url)
        time.sleep(120)  # 间隔两分钟

if __name__ == "__main__":
    main()
