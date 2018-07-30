from Functions import GetConfig, GetLive, LastID, GenHuman, SetCouple, SetPregnant, SetGivingBirth, SetMenopause, SetDied, waktu_proses, CreateSessionCode
# from time import gmtime, strftime
import os
import time
import sys
import random 


try:
    sesscode = sys.argv[1]
except IndexError:
    print('masukkan parameter, misal nama anda + tanpa spasi')
    sys.exit()

try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = LastID()
        if numhuman <= maxnumhuman:
            startt = time.time()
            GetLive()
            print('\n-------- GenHuman --------------')
            GenHuman(1)
            if random.randint(0, 1) is 1:
                print('\n-------- SetCouple -------------')
                SetCouple()
            if random.randint(0, 1) is 1:
                print('\n-------- SetPregnant -----------')
                SetPregnant()
            if random.randint(0, 1) is 1:
                print('\n-------- SetGivingBirth --------')
                SetGivingBirth()
                SetGivingBirth()
                SetGivingBirth()
            if random.randint(0, 1) is 1:
                print('\n-------- SetMenopause ----------')
                SetMenopause()
            if random.randint(0, 1) is 1:
                print('\n-------- SetDied ---------------')
                SetDied(sesscode)
            stopt = time.time()
            fwaktu_proses = waktu_proses(int(stopt) - int(startt))
            print('\n******** Time in cycle : {0} ********\n' . format(fwaktu_proses))
        else:
            print('sim off.')
            time.sleep(.4)
            os.system('clear')
except KeyboardInterrupt:
    pass
