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
        numhuman = int(stats(var='num_human'))
        if numhuman <= maxnumhuman:
            startt = time.time()
            print('')
            print('-------[ ' + sys.argv[1] + ' ]-------')
            if sys.argv[1] == 'restart':
                restart(sess=session)
                restart(sess=session)
                restart(sess=session)
                exit()
            elif sys.argv[1] == 'run':
                GetLive()
                with open('db.json', 'r') as f:
                    fread = f.read()
                    fread = str(fread).replace('\n', '')
                    fread = fread.encode('utf-8')
                    data = json.loads(fread)
                    f.close()
                data = SetCouple(sess=session, getdata=data)
                data = SetPregnant(sess=session, getdata=data)
                data = SetGivingBirth(sess=session, getdata=data)
                data = SetMenopause(sess=session, getdata=data)
                data = SetDied(sess=session, getdata=data)
                print('\n>>>> update_humans <<<<<<<<<<<<<<<<<')
                update_humans(json_=data)
                update_stat()

            stopt = time.time()
            fwaktu_proses = waktu_proses(int(stopt) - int(startt))
            print('\n******** Time in cycle : {0} ********\n' . format(fwaktu_proses))
            time.sleep(random.randint(1, 1))
        else:
            print('sim off.')
            time.sleep(3)
            # os.system('clear')
except KeyboardInterrupt:
    pass
