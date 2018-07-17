from Database import Database
from Functions import genword, genname, GetConfig, GetLive, SetLive, DateRequest
# from time import gmtime, strftime
import sys
import random
import time
import re
import os
from datetime import datetime, timedelta


def NumHuman2():
    db = Database()
    return db.count("SELECT id FROM human WHERE 1")


try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = NumHuman2()
        if numhuman <= maxnumhuman:
            # getLive = GetLive()
            SetLive()
            print('live....')
            time.sleep(.5)
            os.system('clear')
        else:
            print('sleep....')
            time.sleep(.4)
            os.system('clear')
except KeyboardInterrupt:
    pass # do cleanup here
