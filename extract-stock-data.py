#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install pandas')
import yfinance as yf
import pandas as pd


# In[22]:


apple = yf.Ticker("AAPL")
apple_info = apple.info # get stock info
apple_info
print('Sector:', apple_info['sector'])

hist = apple.history(period="max") # get the share price
hist.head()


# In[17]:


hist.reset_index(inplace=True)
hist.plot(x="Date", y="Open")
hist.plot(x="Date", y="Close")


# In[18]:


apple.dividends.plot()


# In[ ]:




