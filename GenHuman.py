from Functions import GetConfig, GetLive, LastID, GenHuman, SetCouple, SetPregnant, SetGivingBirth, SetMenopause, SetDied, waktu_proses
# from time import gmtime, strftime
import os
import time
import sys
import random


try:
    # file = sys.argv[0]
    # sesscode = sys.argv[1]
    # function = sys.argv[2]
    z = 0
    for x in range(0, len(sys.argv)):
        print 'Argument ke-{0} : {1}' . format(z, sys.argv[x])
        if z == 0:
            file = sys.argv[x]
            # print 'Argument ke-{0} : {1}' . format(z, file)
        elif z == 1:
            sesscode = sys.argv[x]
            # print 'Argument ke-{0} : {1}' . format(z, sesscode)
        elif z == 2:
            function = sys.argv[x]
            # print 'Argument ke-{0} : {1}' . format(z, function)
        z += 1

    # print('file : ' . format(file))
    # print('sesscode : ' . format(sesscode))
    # print('function : ' . format(function))

    # sys.exit()
except IndexError:
    print('masukkan parameter, misal nama anda + tanpa spasi')

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    z = 0
    for x in range(0, len(sys.argv)):
        print 'Argument ke-{0} : {1}' . format(z, sys.argv[x])
        z += 1

    sys.exit()

try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = LastID()
        if numhuman <= maxnumhuman and sys.argv[1] is not None:
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
                # SetGivingBirth()
                # SetGivingBirth()
            if function is '4':
                print('\n-------- SetMenopause ----------')
                SetMenopause(sys.argv[1])
            if function is '5':
                print('\n-------- SetDied ---------------')
                SetDied(sys.argv[1])
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
