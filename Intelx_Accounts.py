# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:48:23 2020

@author: Fabio
"""

from intelxapi import intelx

Accountslist=[]
try:
    with open('Credstuffing_October.csv','r') as f:
        
        for value in f:
            Accountslist.append(value.strip())
            
except FileNotFoundError:
    print('Error opening file')

accounts100=Accountslist[]

print('The number of accounts to be searched will be %s'%(len(accounts100)))

intelx=intelx("API KEY") # API KEY from Intelx


#results=[] # uncomment for using the first time
for target in accounts100:
    result=intelx.search(target)
    results.append(result)

 #%%   

for resu in results:
    for record in resu['records']:
        intelx.FILE_READ(record['systemid'], 0, record['bucket'], "file_%s.txt"%(record['randomid']))

#%%
accountsval=[]
for i in range(len(accounttest)):
    accountsval.append([accounttest[i]])
    
#%%

for i in range(len(accounttest)): 
    if len(resultsxx[i]['records']) > 0:
        resu=resultsxx[i]['records']
        for record in resu:
           
            try:
                with open('file_%s.txt'%(record['randomid']),'r',encoding='UTF8') as f:
                    
                    for value in f:
                        if accounttest[i] in value:
                            accountsval[i].append(value)
                        
            except FileNotFoundError:
                print('Error opening file %s for record %d'%(record['randomid'],i) ) 
            except:
                pass

#%%
import csv

with open('Accounts_Validated.csv', 'w',newline='') as f: 
      
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
   # write.writerow(['Account','Record']) 
    for account in accountsval:
        write.writerow(account)
        
    
 