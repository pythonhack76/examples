#come leggere un file con python 
import os
from os.path import exists
from pathlib import Path 

contenuto_file = 'contenuto'
with open('file.txt','w') as f:
    file = f.write(contenuto_file)
    Liste = []
    
    for line in file:
        if line[-1] == '\n':
            Liste.append(line[:-1])

    #add_lista = Liste.append()

with open('file.txt', 'r') as f:
    file = f.readlines() 
    print(file)
# 
# 
# contenuto = 'contenuto di prova'
# file = open('file.txt', 'w')
# f = file.write(contenuto)
# 
# file = open('file.txt', 'r')
# leggi_file = file.readlines() 
# newList = []
# for line in leggi_file: 
    # if line[-1] == '\n':
        # newList.append(line[:-1])
# 
# print(newList)
    # 
    # 
# 

# 
# def createFile():
    # with open('filename.txt', 'w') as f:
        # f.write('pippo')
        # file_exists = os.path.exists(f)
        # print(file_exists)
                                # 
# def readFile():
    # with open('filename.txt', 'r') as f:
        # f.readlines()
        # newList = []
        # for lines in f:
            # newList.append(lines[:-1])
            # print(newList)
        # f.close() 
# 
# 
# createFile() 
# readFile() 

