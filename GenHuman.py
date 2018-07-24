from Functions import GetConfig, GetLive, NumHuman2, GenHuman, SetCouple, SetPregnant, SetGivingBirth, SetMenopause, SetDied
# from time import gmtime, strftime
import os
import time

try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = NumHuman2()
        if numhuman <= maxnumhuman:
            getlive = GetLive()
            # print(getlive)
            # test()
            print('\n-------- GenHuman --------------')
            GenHuman(1)
            # os.system('clear')
            print('\n-------- SetCouple -------------')
            SetCouple()
            # os.system('clear')
            print('\n-------- SetPregnant -----------')
            SetPregnant()
            # os.system('clear')
            print('\n-------- SetGivingBirth --------')
            SetGivingBirth()
            # os.system('clear')
            print('\n-------- SetMenopause ----------')
            SetMenopause()
            # os.system('clear')
            print('\n-------- SetDied ---------------')
            SetDied()
            SetDied()
            # os.system('clear')
        else:
            print('sim off.')
            time.sleep(.4)
            os.system('clear')
except KeyboardInterrupt:
    pass
