#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyodbc
import pandas as pd
import numpy as np
import pickle as p

class preprocess:
    def __init__(self,path):
        self.path=path
        
    def get_data_sql(self,ip,uid,pwd,query):
        conn=pyodbc.connect('Driver={SQL Server};SERVER=%s;DATABASE=PBSA;UID=%s;PWD=%s'%(ip,uid,pwd))
        txn=pd.read_sql_query(query,conn)
        retuen txn
               
    def Amt_bin(self,amt,bin_num,rankAmt):
        for idx, th in enumerate(rankAmt):
            if amt<=th:
                return idx
        return bin_num
    
    def word2idx(self,vocab,data):
        word2idx_dic={word:idx for idx,word in enumerate(vocb)}
        word2idx_dic['padding']=len(vocb)
        data2idx=[[word2idx_dic[w] for w in s] for s in data]
        return word2idx_dic,data2idx

if __name__=="__main__":
    pre=prepprocess()
    txn=pre.get_data_sql()
    
    bin_num=20.0
    rankAmt=[txn['BaseAmt'].quantile(i/bin_num) for i in range(bin_num)]
    txn['BaseAmt_Bin']=txn['BaseAmt'].apply(Amt_bin,args=(bin_num,rankAmt))
    txn['word']=txn.apply(lambda x: '_'.join(x),axis=1)
    
    vocab=txn['word'].unique()
    cust_unique=txn['Cust'].unique()
    txn=txn.sort_values(by=['Cust','BookDate'])
    docs=[list(txn[txn['Cust']==cust_unique[i]]['word']) for i in range(len(cust_unique))]
    
    word2idx_dic,txn2idx=pre.word2idx(vocab,docs)
    with open(pre.path+'/data_paper.pickle','wb') as f:
        p.dump(txn2idx,f)
    with open(pre.path+'/word2idx_dic_paper.pickle','wb') as f:
        p.dump(word2idx_dic,f)
    

