#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import argparse
from argparse import ArgumentParser

def import_data(data):
    df = pd.read_csv(data)  
    return df

if __name__ == '__main__': 
    parser = argparse.ArgumentParser() 
    parser.add_argument('f1')  
    args = parser.parse_args()
    import_data(args.f1)


# In[ ]:




