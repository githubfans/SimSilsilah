from Functions_json import *
# from time import gmtime, strftime
# import os
# import time
import sys
import random
# import json
session = sess_code()

# print(sys.argv)
# print(sys.argv[0])


try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = LastID()
        if numhuman <= maxnumhuman and sys.argv[1] is not None:
            startt = time.time()
            GetLive()
            print('>>>>>>' + sys.argv[1])
            # GenHuman(random.randint(50, 100), 1)
            if sys.argv[1] == 'SetCouple':
                SetCouple(sess=session)
            elif sys.argv[1] == 'SetPregnant':
                SetPregnant(sess=session)
            elif sys.argv[1] == 'SetGivingBirth':
                SetGivingBirth(sess=session)
            elif sys.argv[1] == 'SetMenopause':
                SetMenopause(sess=session)
            elif sys.argv[1] == 'SetDied':
                SetDied(sess=session)
            elif sys.argv[1] == 'restart':
                restart(sess=session)
                exit()

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
