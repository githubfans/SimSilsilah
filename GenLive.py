from Database import Database
from Functions import genword, genname, GetConfig, GetLive, SetLive, DateRequest
# from time import gmtime, strftime
import sys
import random
import time
import re
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
            time.sleep(.5)
            print('live....')
        else:
            print('sleep....')
except KeyboardInterrupt:
    pass # do cleanup here
