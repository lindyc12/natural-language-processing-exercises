from requests import get
import pandas as pd
import os

def get_soup(url, headers = {'User-Agent': 'Codeup Data Science'}):
    from bs4 import BeautifulSoup
    response = get(url, headers=headers)
    return BeautifulSoup(response.content)

blogs = ['https://codeup.com/codeup-news/codeup-dallas-campus/', 'https://codeup.com/data-science/jobs-after-a-coding-bootcamp-part-1-data-science/', 'https://codeup.com/tips-for-prospective-students/mental-health-first-aid-training/', 'https://codeup.com/codeup-news/inclusion-at-codeup-during-pride-month-and-always/',
        'https://codeup.com/tips-for-prospective-students/is-our-cloud-administration-program-right-for-you/']


def get_blog_articles(blogs):
    #make empty list
    data = []
    for blog in blogs:
        # assign url 
        url = blog
        headers = {'User-Agent': 'Codeup Data Science'} 
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('div', id= 'main-content')
        # get title
        title = article.find('h1', {'class': 'entry-title',})
        # get content
        content = article.find('div', {'class': 'entry-content'})
        # make the dictionary
        blog_dict = {'title': title.text, 'content': content.text}
        data.append(blog_dict)

    return data


def get_news_articles():
    # define categories 
    base_url = 'https://inshorts.com/en/read/'
    categories = [
        'business',
        'sports',
        'technology',
        'entertainment',
        ]
    data = []
    for category in categories:
        # make url 
        soup = get_soup(base_url+category)
        cards = soup.find_all(class_='news-card' )
        for card in cards:
            # make dictionary
            article_dict = {
                'title': card.find(itemprop='headline').string,
                'author': card.find(class_='author').string,
                'published': card.find(class_='time')['content'],
                'category': category,
                'content': card.find(itemprop='articleBody').text
            }
            # put dictionary into a list
            data.append(article_dict)
    # make into df
    df = pd.DataFrame(data)

    return df