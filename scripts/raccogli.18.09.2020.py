#!/usr/bin/python3.6

'''
raccogli elaborati esame 
'''

import os                                                                             
import sys  
from pandas import read_csv 
from shutil import copy2 
from datetime import datetime

file_dati_studenti = '/home/dzambell/Geo20/esame/iscritti.18.09.2020.csv'
cartella_esame = '/esame.18.09.2020/'
cartella_elaborati = '/elaborati.18.09.2020/'

df = read_csv(file_dati_studenti, 
                 usecols = [0,1,5],
                 skiprows=1,
                 names=['nome', 'cognome', 'user'],
                 ) 
df['user'] = [ x.split('@')[0] for x in df['user'] ]

elaborati = '/home/dzambell/Geo20/esame' + cartella_elaborati +  datetime.now().time().replace(microsecond=0).isoformat()
os.makedirs(elaborati)

for i in df.index:
    path = '/home/' + df.loc[i,'user'] + cartella_esame
    cognome = df.loc[i,'cognome'].replace(" ", "").replace("'", "")   
    nome = df.loc[i,'nome'].replace(" ", "").replace("'", "") 
    file = path + cognome + '.' + nome + '.ipynb' 
    print(file)
    copy2( file, elaborati + '/' )
    
    # aggiunto per correggere un errore:
    #if os.path.exists(path): copy2( path, elaborati + "/"  + cognome + '.'+ nome + '.ipynb' )
    #else: print ('File "' + path + '" does not exist') 
    
os.system( f"chown -R dzambell:dzambell {'/home/dzambell/Geo20/esame/'}" )
    
