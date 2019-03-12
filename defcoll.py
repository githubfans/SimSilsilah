# def
# import sys
import json
import inspect
import datetime
import time
import math


def restart(sess=''):
    # this_function_name = sess + '|' + sys._getframe().f_code.co_name
    # empty_data_in_use()
    f = open("START-UP.txt", "r")
    new = f.read()
    f.close()
    live_new = str(new).strip().split('live.cnf=\n')[1]
    live_new = live_new.strip().split('\n=end')[0]
    db_coupled = str(new).strip().split('db.json=\n')[1]
    db_coupled = db_coupled.strip().split('\n=end')[0]
    db_empty = str(new).strip().split('empty-db=\n')[1]
    db_empty = db_empty.strip().split('\n=end')[0]
    stat_new = str(new).strip().split('stat.cnf=\n')[1]
    stat_new = stat_new.strip().split('\n=end')[0]
    flive = open("live.cnf", "w")
    if flive.write(live_new):
        print('live restart done !!')
    else:
        print('live restart error !!')
    # fdb = open("db.json", "w")
    # if fdb.write(db_coupled):
    #     print('db restart done !!')
    # else:
    #     print('db restart error !!')
    fdb = open("db.single.json", "w")
    if fdb.write(db_empty):
        print('db-single restart done !!')
    else:
        print('db-single restart error !!')
    # print(db_coupled)
    fdb = open("db.coupled.json", "w")
    if fdb.write(db_coupled):
        print('db-coupled restart done !!')
    else:
        print('db-coupled restart error !!')
    fdb = open("db.menopause.json", "w")
    if fdb.write(db_empty):
        print('db-menopause restart done !!')
    else:
        print('db-menopause restart error !!')
    fdb = open("db.died.json", "w")
    if fdb.write(db_empty):
        print('db-died restart done !!')
    else:
        print('db-died restart error !!')
    fstat = open("stat.cnf", "w")
    if fstat.write(stat_new):
        print('stat restart done !!')
    else:
        print('stat restart error !!')
    fstat = open("stat.cnf", "r")
    print(fstat.read())


def GetLive():
    import os.path
    if os.path.exists('live.cnf') and os.access('live.cnf', os.R_OK):
        filelive1 = os.path.getmtime('live.cnf')
        filelive2 = os.path.getmtime('live.run')
        if filelive1 > filelive2:
            nf = open("live.cnf", "r")
            newlive = nf.read()
            nf.close()
            if len(newlive) > 10:
                f = open("live.run", "w+")
                f.write(newlive)
                f.close()

    f = open("live.run", "r")
    live = f.read()
    f.close()

    if len(live) < 10:
        nf = open("live.cnf", "r")
        newlive = nf.read()
        live = newlive
        nf.close()
        if len(newlive) > 10:
            f = open("live.run", "w+")
            f.write(newlive)
            f.close()
    return live


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    # print('replace_line >>>\n' + lines[line_num])
    try:
        out = open(file_name, 'w')
        while not out.closed:
            try:
                out.writelines(lines)
                print('Replace done...')
            except IndexError:
                print('ERROR Replace...')
            out.close()
    except IndexError:
        print('ERROR open db...')


def find_replace_line(file_name, text_find, text_replace):
    fopen = open(file_name, 'r')
    fopen_read = fopen.read()
    fopen_part = fopen_read.strip().split('\n')
    linemark = 0
    for data in fopen_part:
        # print(data)
        if text_find in data:
            text_replace = text_replace + '\n'
            replace_line(file_name=file_name, line_num=linemark, text=text_replace)
        linemark += 1
    fopen.close()


def loads_db(dbname):
    with open('db.' + dbname + '.json', 'r') as rfile:
        read = rfile.read()
        # exit(read)
        return json.loads(read)


def UpdateStat():
    with open('db.single.json', 'r') as rfile:
        content_single = rfile.read()
        # print(content_single.strip().split('"id"'))
    num_single = content_single.count('"id":')
    num_single_female = content_single.count('"sex": "F"')
    num_single_male = content_single.count('"sex": "M"')
    print('num_single = ', num_single)
    with open('db.coupled.json', 'r') as rfile:
        content_coupled = rfile.read()
        # print(content_coupled.strip().split('"id"'))
    # content_coupled = content_coupled.replace("\n", '')
    # print(inspect.stack()[0][2], content_coupled)
    num_coupled = content_coupled.count('"id":')
    print('num_coupled = ', num_coupled)
    num_coupled_female = content_coupled.count('"sex": "F"')
    print('num_coupled_female = ', num_coupled_female)
    jloads_coupled = json.loads(content_coupled)
    # exit(jloads_coupled)
    nPregnant = 0
    for data in jloads_coupled:
        # print(data)
        if 'isPregnant' in data:
            if data['isPregnant'] != '' or data['isPregnant'] != '0':
                nPregnant += 1
    print('num_pregnant = ', nPregnant)
    with open('db.menopause.json', 'r') as rfile:
        content_menopause = rfile.read()
        # print(content_menopause.strip().split('"id"'))
    num_menopause = content_menopause.count('"id":')
    print('num_menopause = ', num_menopause)
    with open('db.died.json', 'r') as rfile:
        content_died = rfile.read()
        # print(content_died.strip().split('"id"'))
    num_died = content_died.count('"id":')
    print('num_died = ', num_died)

    num_human = num_single + num_coupled + num_menopause + num_died
    num_human_life = num_single + num_coupled + num_menopause
    find_replace_line(file_name='stat.cnf', text_find='num_human=', text_replace='num_human=' + str(num_human))
    find_replace_line(file_name='stat.cnf', text_find='num_human_life=', text_replace='num_human_life=' + str(num_human_life))
    find_replace_line(file_name='stat.cnf', text_find='num_single=', text_replace='num_single=' + str(num_single))
    find_replace_line(file_name='stat.cnf', text_find='num_single_female=', text_replace='num_single_female=' + str(num_single_female))
    find_replace_line(file_name='stat.cnf', text_find='num_single_male=', text_replace='num_single_male=' + str(num_single_male))
    find_replace_line(file_name='stat.cnf', text_find='num_coupled=', text_replace='num_coupled=' + str(num_coupled))
    find_replace_line(file_name='stat.cnf', text_find='num_coupled_female=', text_replace='num_coupled_female=' + str(num_coupled_female))
    find_replace_line(file_name='stat.cnf', text_find='num_menopause=', text_replace='num_menopause=' + str(num_menopause))
    find_replace_line(file_name='stat.cnf', text_find='num_died=', text_replace='num_died=' + str(num_died))


def GetStat():
    import os.path
    if os.path.exists('stat.cnf') and os.access('stat.cnf', os.R_OK):
        fileconfig1 = os.path.getmtime('stat.cnf')
        fileconfig2 = os.path.getmtime('stat.run')
        if fileconfig1 > fileconfig2:
            nf = open("stat.cnf", "r")
            newconfig = nf.read()
            nf.close()
            if len(newconfig) > 20:
                f = open("stat.run", "w+")
                f.write(newconfig)
                f.close()
    stat_read = '{EMPTY_STAT}'
    with open("stat.run", "r") as f:
        stat_read = f.read()
        f.close()
    return stat_read


def GetConfig(str):
    import os.path
    if os.path.exists('config.cnf') and os.access('config.cnf', os.R_OK):
        fileconfig1 = os.path.getmtime('config.cnf')
        fileconfig2 = os.path.getmtime('config.run')
        if fileconfig1 > fileconfig2:
            nf = open("config.cnf", "r")
            newconfig = nf.read()
            nf.close()
            if len(newconfig) > 20:
                f = open("config.run", "w+")
                f.write(newconfig)
                f.close()

    f = open("config.run", "r")
    config = f.read()
    f.close()

    if len(config) < 20:
        nf = open("config.cnf", "r")
        newconfig = nf.read()
        config = newconfig
        nf.close()
        if len(newconfig) > 20:
            f = open("config.run", "w+")
            f.write(newconfig)
            f.close()
    try:
        getx = config.strip().split('\n{0}=' . format(str))[1]
        getx2 = getx.strip().split(';')[0]
        # print('getx2 = {0}' . format(getx2))
        # cari_koma = re.search(',', getx2)
        # cari_kali = re.search('x', getx2)
        # cari_bagi = re.search('/', getx2)
        if ',' in getx2:

            getx2_1 = getx2.strip().split(',')[0]
            getx2_2 = getx2.strip().split(',')[1]

            # cari_kali_1 = re.search('x', getx2_1)
            # cari_kali_2 = re.search('x', getx2_2)

            if 'x' in getx2_1:
                getx2_x1 = int(getx2_1.strip().split('x')[0]) * int(getx2_1.strip().split('x')[1])
            else:
                getx2_x1 = getx2_1

            if 'x' in getx2_2:
                getx2_x2 = int(getx2_2.strip().split('x')[0]) * int(getx2_2.strip().split('x')[1])
            else:
                getx2_x2 = getx2_2

            if int(getx2_x1) >= 0 and int(getx2_x2) >= 0:
                getx2 = '{0},{1}' . format(getx2_x1, getx2_x2)

            return getx2

        elif 'x' in getx2:
            hasil_kali = int(getx2.strip().split('x')[0]) * int(getx2.strip().split('x')[1])
            return hasil_kali
        elif '/' in getx2:
            hasil_bagi = int(getx2.strip().split('/')[0]) * int(getx2.strip().split('/')[1])
            return hasil_bagi
        else:
            return int(getx2)
    except IndexError:
        return 0


def get_age(currdatetime, dateborn, return_days=False):
    currdatetime = datetime_to_timestamp(currdatetime)
    dateborn = datetime_to_timestamp(dateborn)
    if return_days is True:
        return_ = timestamp_to_days(currdatetime - dateborn)
    else:
        return_ = timestamp_to_years(currdatetime - dateborn)
    return round(return_, 0)


def datetime_to_timestamp(strdatetime):
    return time.mktime(datetime.datetime.strptime(strdatetime, "%Y-%m-%d %H:%M:%S").timetuple())


def timestamp_to_days(inttimestamp):
    return inttimestamp / 86400


def timestamp_to_years(inttimestamp):
    return inttimestamp / (86400 * 365)


def load_dbtemp(dbname):
    readlist = []
    with open('dbtemp.' + dbname + '.json', 'r') as f:
        read = f.read()
        readlist = list(read.strip().split(' '))
    return readlist


def save_dbtemp(dbname, content):
    with open('dbtemp.' + dbname + '.json', 'a') as dbtemp:
        dbtemp.write(content + ' ')


def empty_dbtemp(dbname):
    open('dbtemp.' + dbname + '.json', 'w').close()


def reformat_db(dbname):
    with open('db.' + dbname + '.json', 'r') as rfile:
        content = rfile.read()
        content = content.replace('[{"id":', '[\n{"id":')
        content = content.replace('}]', '}\n]')
        content = content.replace('"[removed]", ', '')
        content = content.replace('"[removed]"', '')
        content = content.replace('}, {"id":', '},\n{"id":')
        content = content.replace('}\n][', '},')
        content = content.replace('[\n][', '[')
        content = content.replace('"", {', ',\n{')
        content = content.replace('"", "", {', ',\n{')
        content = content.replace('"", "", "", {', ',\n{')
        content = content.replace('"", "", "", "", {', ',\n{')
        content = content.replace('}, "", ,', '},')
        content = content.replace('}, "", "", ,', '},')
        content = content.replace('}, "", "", "", ,', '},')
        content = content.replace('}, "", "", "", "", ,', '},')
        content = content.replace('}, "", "", "", "", "", ,', '},')
        content = content.replace('}, "", "", "", "", "", "", ,', '},')
        content = content.replace('}, ,', '},')
        content = content.replace('["", ,', '[')
        content = content.replace('[,', '[')
        content = content.replace('}, ]', '}\n]')
    with open('db.' + dbname + '.json', 'w') as wfile:
        wfile.write(content)


def del_dict_item(dbname, id):
    hit = 0
    index_ = 0
    list_db = loads_db(dbname)
    for data in list_db:
        try:
            if data['id'] == id:
                return__ = data
                hit += 1
        except Exception:
            pass
        index_ += 1
    return return__
