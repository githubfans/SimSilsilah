from Functions_json import *
# from time import gmtime, strftime
# import os
# import time
# import sys
import random
# import json

GenHuman_json(random.randint(1, 10), 1)
# GetNoCouple_json(sexrequest='F')
# GetNoCouple_json(sexrequest='M')
SetCouple()

# def optimizedb():
#     f = open('db.json', 'r')
#     fread = f.read()
#     fread = str(fread).replace('\n', '')
#     fread = str(fread).replace('}\n,\n{', '},\n{')
#     print(fread)
#     fread = fread.encode('utf-8')
#     jloads = json.loads(fread)
#     # jloads['humans']
#     fread = str(json.dumps(jloads))
#     fread = fread.replace('{"humans": [{', '{\n"humans":\n[\n{')
#     fread = fread.replace('}, {', '},\n{')
#     f = open('db.json', 'w')
#     f.write(fread)
#     f.close()
    # # return jloads['humans']

# optimizedb()


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
