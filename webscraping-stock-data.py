#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')

import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[4]:


# use requests to extract data

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')


# In[6]:


nf_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    nf_data = nf_data.append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)  
    
nf_data.head(10)


# In[9]:


# use read_html to read url

pd_data = pd.read_html(url)
pd_data = pd.read_html(str(soup)) # conver soup to str

nf_dataframe1 = pd_data[0] # take the first table

nf_dataframe1.head(10)


# In[10]:


amzn_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'

html_data = requests.get(amzn_url).text

beautiful_soup = BeautifulSoup(html_data, 'html5lib')

beautiful_soup.prettify()

title = beautiful_soup.title

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in beautiful_soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    
amazon_data.head()


# In[ ]:




