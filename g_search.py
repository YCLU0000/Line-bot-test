#!/usr/bin/env python
# coding: utf-8

# In[86]:


# Import the beautifulsoup 
# and request libraries of python.
import requests
from bs4 import BeautifulSoup
import re


# In[87]:


def g_search(query):
    # Make two strings with default google search URL
    # 'https://google.com/search?q=' and
    # our customized search keyword.
    # Concatenate them
    text= query
    url = 'https://www.google.com/search?q=' + text
    #Fetch the URL data using requests.get(url),
    # store it in a variable, request_result.
    request_result=requests.get( url )
  
    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
                         "lxml")
    # Find all the a tags and get the text/href
    tags = soup.find_all("a")
    for tag in tags:
        href = re.search("https?://\S*&sa",tag["href"])
        text = tag.getText()
        if (href and text not in ["地圖","規劃路線","網站"]):
            href = href.group(0)[:-3]
            print(text)
            print(href)
            print("------")


# In[88]:


#test
if __name__ == "__main__":
    g_search("梨園湯包")


# In[ ]:




