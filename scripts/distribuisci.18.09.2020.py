#!/usr/bin/python3.6

'''
distribuisci testo esame 
'''
import os                                                                               
import sys  
from pandas import read_csv
from shutil import copy

file_dati_studenti = '/home/dzambell/Geo20/esame/iscritti.18.09.2020.csv'
testo_esame = '/home/dzambell/Geo20/esame/esame.18.09.2020.ipynb'
cartella_elaborati = '/esame.18.09.2020/'

df = read_csv(file_dati_studenti, 
                  usecols = [0,1,5],
                  skiprows=1,
                  names=['nome','cognome','email'],
             )
df['user'] = [ x.split('@')[0] for x in df['email'] ]

for i in df.index:
    path = '/home/' + df.loc[i,'user'] + cartella_elaborati
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print ('Folder "' + path + '" already exists')
        
    cognome = df.loc[i,'cognome'].replace(" ", "").replace("'", "")   
    nome = df.loc[i,'nome'].replace(" ", "").replace("'", "")  
    file = path + cognome + '.' + nome + '.ipynb'
    copy( testo_esame, file )
   
    os.system(f"chown -R {df.loc[i,'user']}:{df.loc[i,'user']} {path}" )
    #print(f"chown -R {df.loc[i,'user']}:{df.loc[i,'user']} {path}")
    os.system(f"chmod 600 {file}")
    #print(f"chmod 600 {file}")
