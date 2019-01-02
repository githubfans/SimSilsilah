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
        if numhuman <= maxnumhuman:
            startt = time.time()
            if sys.argv[1] == 'restart':
                print('>>>>>>' + sys.argv[1])
                restart(sess=session)
                restart(sess=session)
                restart(sess=session)
                exit()
            elif sys.argv[1] == 'run':
                GetLive()
                print('>>>>>> ' + sys.argv[1])
                # GenHuman(random.randint(50, 100), 1)
                f = open('db.json', 'r')
                fread = f.read()
                fread = str(fread).replace('\n', '')
                fread = fread.encode('utf-8')
                data = json.loads(fread)
                f.close()
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                data = SetCouple(sess=session, getdata=data)
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                data = SetPregnant(sess=session, getdata=data)
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                data = SetGivingBirth(sess=session, getdata=data)
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                data = SetMenopause(sess=session, getdata=data)
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                data = SetDied(sess=session, getdata=data)
                print('\n*********\ngetdata = \n' + str(data) + '\n**********\n\n')
                update_humans(json_=data)

            stopt = time.time()
            fwaktu_proses = waktu_proses(int(stopt) - int(startt))
            print('\n******** Time in cycle : {0} ********\n' . format(fwaktu_proses))
            time.sleep(random.randint(0, 1))
        else:
            print('sim off.')
            time.sleep(1)
            os.system('clear')
except KeyboardInterrupt:
    pass
