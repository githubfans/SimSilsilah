from Functions_json import *
# from time import gmtime, strftime
# import os
# import time
# import sys
import random
# import json

# GenHuman_json(random.randint(3, 5), 1)
GetNoCouple_json(sexrequest='M')

# def numHuman():
#     f = open('db.json', 'r')
#     fread = f.read()
#     fread = str(fread).replace('\n', '')
#     fread = fread.encode('utf-8')
#     print(fread)
#     jloads = json.loads(fread)
#     # jloads['humans']
#     return len(jloads['humans'])


# def InsertDataToDB(filedb, insert_to_line, text):
#     f = open(filedb, "r")
#     contents = f.readlines()
#     f.close()
#     contents.insert(insert_to_line, text + '\n')
#     f = open(filedb, "w")
#     contents = "".join(contents)
#     f.write(contents)
#     f.close()


# def getHumanId(index):
#     f = open('db.json', 'r')
#     fread = f.read()
#     fread = str(fread).replace('\n', '')
#     fread = fread.encode('utf-8')
#     jloads = json.loads(fread)
#     return jloads['humans'][index]['id']
