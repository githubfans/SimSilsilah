from Functions_json import *
# from time import gmtime, strftime
import time
import os
# import sys

try:
    while True:
        startt = time.time()
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        # speed = GetConfig('simulation_speed')
        numhuman = stats(var='num_human')
        numhumanlife = stats(var='num_human_life')
        numCoupled = stats(var='num_couple')
        numCoupled_F_before_menopause = stats(var='num_couple_female_nomenopause')
        numCoupleless_M = stats(var='num_coupleless_male')
        numCoupleless_F = stats(var='num_coupleless_female')
        numPregnant = stats(var='num_pregnant')
        numMenopause = stats(var='num_menopause')
        numDied = stats(var='num_died')
        live = GetLive()
        cek = int(numhumanlife) + int(numDied)
        print('')
        print('curr. time : {0}' . format(live))
        # print('speed {0}' . format(1 / speed))
        print('target gen. : {0}' . format(maxnumhuman))
        print('')
        print('num. human : {0}' . format(numhuman))
        # print('died + life : {0}' . format(cek))
        print('num. human life : {0}' . format(numhumanlife))
        print('num. couple : {0}' . format(numCoupled))
        print('num. couple female before menopause : {0}' . format(numCoupled_F_before_menopause))
        print('num. coupleless male : {0}' . format(numCoupleless_M))
        print('num. coupleless female : {0}' . format(numCoupleless_F))
        print('num. pregnant : {0}' . format(numPregnant))
        print('num. menopause : {0}' . format(numMenopause))
        print('num. died : {0}' . format(numDied))
        # if cek != int(numhuman):
        #     print('WARNING !!!/nnumhumanlife + numDied != numhuman')
        if int(numhuman) <= int(maxnumhuman) and is_process(file='test2.py') is True:
            # getLive = GetLive()
            SetLive()
            print('live....')
            time.sleep(1)
            os.system('clear')
        else:
            print('sleep....')
            time.sleep(5)
            os.system('clear')
            stopt = time.time()
            fwaktu_proses = waktu_proses(int(stopt) - int(startt))
except KeyboardInterrupt:
    pass
