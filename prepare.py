import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd
import acquire


def basic_clean(blog):
    blog = blog.lower()
    blog = (unicodedata.normalize('NFKD', blog)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore'))
    blog = re.sub(r"[^a-z0-9'\s]", '', blog)
    return blog

def tokenize(blog):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    blog = tokenizer.tokenize(blog, return_str=True)
    return blog

def stem(blog):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in blog.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed


def lemmatize(blog):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in blog.split()]
    article_lemmatized = ' '.join(lemmas)

    return article_lemmatized


def remove_stopwords(string, extra_words=None, exclude_words=None):
    
    stopword_list = stopwords.words('english')
    
    if exclude_words:
        
        stopword_list = stopword_list + exclude_words
        
    if extra_words:
        
        for word in extra_words:
            
            stopword_list.remove(word)
            
    words = string.split()
    
    filtered_words = [word for word in words if word not in stopword_list]
    
    filtered_string = ' '.join(filtered_words)
    
    return filtered_string



