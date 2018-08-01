from Functions import GetConfig, GetLive, LastID, GenHuman, SetCouple, SetPregnant, SetGivingBirth, SetMenopause, SetDied, waktu_proses
# from time import gmtime, strftime
import os
import time
import sys
# import random 


try:
    sesscode = sys.argv[1]
    function = sys.argv[2]
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
            GenHuman(1)
            if function is '1':
                print('\n-------- SetCouple -------------')
                SetCouple()
            if function is '2':
                print('\n-------- SetPregnant -----------')
                SetPregnant()
            if function is '3':
                print('\n-------- SetGivingBirth --------')
                SetGivingBirth()
                SetGivingBirth()
                SetGivingBirth()
            if function is '4':
                print('\n-------- SetMenopause ----------')
                SetMenopause()
            if function is '5':
                print('\n-------- SetDied ---------------')
                SetDied(sesscode)
            stopt = time.time()
            fwaktu_proses = waktu_proses(int(stopt) - int(startt))
            print('\n******** Time in cycle : {0} ********\n' . format(fwaktu_proses))
            time.sleep(random.randint(1, 3))
        else:
            print('sim off.')
            time.sleep(1)
            os.system('clear')
except KeyboardInterrupt:
    pass
