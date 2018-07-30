from Functions import GetConfig, SetLive, GetLive, LastID, NumHumanLife, NumHumanDied
# from time import gmtime, strftime
import time
import os
# import sys

try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        speed = GetConfig('simulation_speed')
        numhuman = LastID()
        numhumanLife = NumHumanLife()
        numhumanLife_Coupled = NumHumanLife(cond='AND idCouple>0')
        numhumanLife_Pregnant = NumHumanLife(cond='AND datepregnant IS NOT NULL')
        numhumanLife_Menopause = NumHumanLife(cond='AND datemenopause IS NOT NULL')
        numhumanLife_Menopause_Single = NumHumanLife(cond='AND datemenopause IS NOT NULL AND idCouple=""')
        numhumanDied = NumHumanDied()
        total = numhumanLife + numhumanDied
        error = numhuman - total
        live = GetLive()
        print('{0}' . format(live))
        print('speed {0}' . format(1 / speed))
        print('last id : {0}' . format(numhuman))
        print('lifes : {0}' . format(numhumanLife))
        print('deads : {0}' . format(numhumanDied))
        print('total : {0}' . format(total))
        print('coupled : {0}' . format(numhumanLife_Coupled))
        print('pregnant : {0}' . format(numhumanLife_Pregnant))
        print('menopause : {0}' . format(numhumanLife_Menopause))
        print('menopause+single : {0}' . format(numhumanLife_Menopause_Single))
        if 0 > error < 1:
            print('error : {0} <<<< PERBAIKI INI ..  ' . format(error))
        if numhuman <= maxnumhuman:
            # getLive = GetLive()
            SetLive()
            print('live....')
            time.sleep(1 / speed)
            os.system('clear')
        else:
            print('sleep....')
            time.sleep(1)
            os.system('clear')
except KeyboardInterrupt:
    pass
