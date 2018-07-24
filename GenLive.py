from Functions import GetConfig, SetLive, GetLive, NumHuman2, NumHumanLife
# from time import gmtime, strftime
import time
import os


try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = NumHuman2()
        numhumanLife = NumHumanLife()
        live = GetLive()
        print('{0}' . format(live))
        print('last id : {0}' . format(numhuman))
        print('humans : {0}' . format(numhumanLife))
        if numhuman <= maxnumhuman:
            # getLive = GetLive()
            SetLive()
            print('live....')
            time.sleep(1)
            os.system('clear')
        else:
            print('sleep....')
            time.sleep(1)
            os.system('clear')
except KeyboardInterrupt:
    pass
