# from Database import Database
import random
import re
import os
import json
import sys
import time
import datetime
from time import gmtime, strftime
import hashlib
from datetime import datetime
from datetime import timedelta
from lockfile import LockFile
import math


def genword(minchars=3, maxchars=5, istitle=0):
    vocal = ('a', 'e', 'i', 'o', 'u')
    conso = ('w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'b', 'n', 'm')
    group = []
    numchar = random.randint(minchars, maxchars)
    for i in range(numchar):
        rnd = random.randint(0, 20)
        if rnd is 0:
            full_name = random.choice(vocal) + random.choice(conso)
        if rnd > 0:
            full_name = random.choice(conso) + random.choice(vocal)
        group.append(full_name)
    group_string = "".join(group)
    if istitle is 1:
        return group_string[:numchar].title()
    else:
        return group_string[:numchar]


def genname(minwords=2, maxwords=3, minchars=3, maxchars=5, istitle=1):
    import random
    numword = random.randint(minwords, maxwords)
    group = []
    for i in range(numword):
        dword = genword(minchars, maxchars, istitle)
        group.append(dword)
    return " ".join(group)


def gendesc(minitem=3, maxitem=100, minwords=5, maxwords=10, minchars=3, maxchars=7, istitle=0):
    import random
    numitem = random.randint(minitem, maxitem)
    group = []
    for i in range(numitem):
        ditem = genname(minwords, maxwords, minchars, maxchars, istitle)
        group.append(ditem)
    return ". ".join(group) + "."


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

    # numhuman = 0
    # # LastID()
    # # print(numhuman)
    # if len(live) < 10:
    #     live = '1000-01-01 00:00:00'
    #     # print('GetLive() -- reset live type 1')
    #     fx = open("live.cnf", "w+")
    #     fx.write(str(live))
    #     fx.close()
    # elif numhuman < 1:
    #     live = '1000-01-01 00:00:00'
    #     # print('GetLive() -- reset live type 2')
    #     fx = open("live.cnf", "w+")
    #     fx.write(str(live))
    #     fx.close()
    return live


def SetLive():
    print('> SetLive')
    getLive = GetLive()
    newlive = datetime.strptime(getLive, "%Y-%m-%d %H:%M:%S")
    min_r = GetConfig('simulation_mintimeadd')
    max_r = GetConfig('simulation_maxtimeadd')
    newlive = newlive + timedelta(seconds=random.randint(min_r, max_r))
    newlive = newlive + timedelta(seconds=random.randint(1, 3600))
    f = open("live.cnf", "w+")
    f.write(str(newlive))
    f.close()


def DateRequest(StrConfig, by='seconds'):
    # print('DateRequest')
    getLive = GetLive()
    timelive = datetime.strptime(getLive, "%Y-%m-%d %H:%M:%S")
    valCOnfig = GetConfig(StrConfig)
    # print(StrConfig)
    # print(valCOnfig)
    valCOnfig = int(valCOnfig.strip().split(',')[0])
    # print(valCOnfig)
    val_seconds = valCOnfig * 3600 * 24 * 365
    # print(val_seconds)
    if by is 'seconds':
        result = timelive - timedelta(seconds=val_seconds)
        # print('result : ' . format(result))
        return result
    if by is 'days':
        result = timelive - timedelta(days=valCOnfig)
        # print('result : ' . format(result))
        return result


def waktu_proses(seconds):
    '''

    format time()


    '''

    detik = '{:.4f}' . format(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if seconds >= 60:
        return '{0} jam {1} menit {2} detik' . format(h, m, s)
    else:
        return '{0} detik' . format(detik)


def CreateSessionCode(str):
    # md5 for session code = receipt code
    sessioncode = '{0}|{1}' . format(str, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    m = hashlib.md5()
    m.update(sessioncode)
    return m.hexdigest()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def test():
    print(genname(minwords=2, maxwords=3, minchars=3, maxchars=5, istitle=1))


def json_humans(jsonstr):
    # jsonstr = {
    #     'firstname': firstname,
    #     'lastname': lastname,
    #     'sex': sex,
    #     'email': email,
    #     'dateadd': dateadd,
    #     'dateborn': dateborn,
    #     'idParent': idParent,
    #     'idCouple': idCouple,
    # }
    # print('jsonstr = ' + str(jsonstr))
    source_idhuman = '{0}|{1}' . format(str(jsonstr['email']), strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    source_idhuman = source_idhuman.encode(encoding='UTF-8', errors='strict')
    # print(source_idhuman)
    m = hashlib.md5()
    m.update(source_idhuman)
    idhuman = m.hexdigest()
    returns = '{"id":"' + idhuman + '", "firstname":"' + jsonstr['firstname'] + '", "lastname":"' + jsonstr['lastname'] + '", "sex":"' + jsonstr['sex'] + '", "email":"' + jsonstr['email'] + '", "dateadd":"' + jsonstr['dateadd'] + '", "dateborn":"' + jsonstr['dateborn'] + '", "idParent":"' + jsonstr['idParent'] + '", "idCouple":"' + jsonstr['idCouple'] + '"}'
    # print('returns = ' + returns)
    return returns


def ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def macadd():
    import subprocess
    proc = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out1 = str(out).strip().split('    ')[1]
    out2 = str(out1).strip().split("Ethernet  HWaddr ")[1]
    return str(out2).strip().split(" ")[0]


def sess_code():
    import uuid
    # prefix = uuid.uuid4().hex.upper()[0:4]
    macadd_ = macadd()
    # source = '{0}-{1}' . format(macadd_, strftime("%Y-%m-%d", gmtime()))
    source = '{0}' . format(macadd_)
    print('macadd_ = ' + str(macadd_))
    print(source)
    source = source.encode(encoding='UTF-8', errors='strict')
    # print(source)
    m = hashlib.md5()
    m.update(source)
    md5 = m.hexdigest()
    from pathlib import Path
    my_file = Path(md5 + ".data")
    if my_file.is_file():
        # file exists
        pass
    else:
        f = open("inuse/" + md5 + ".data", 'a')
    returns = md5
    # print('returns = ' + returns)
    return returns


def generate_json_human(queryes, parent, currdatetime):
    # print(currdatetime)
    # Data Insert into the table
    name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
    name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
    sexx = random.randint(0, 1)
    if sexx is 0:
        sex = 'M'
    else:
        sex = 'F'
    # email_suffix = re.sub('[^0-9a-zA-Z]+', '', currdatetime)
    email_suffix = abs(time.mktime(datetime.strptime(currdatetime, "%Y-%m-%d %H:%M:%S").timetuple()))
    # print(email_suffix)
    email = '{0}.{1}@{2}.com' . format(name_1, email_suffix, genword(minchars=5, maxchars=10, istitle=0))
    email = email.lower()
    idCouple = ''
    jsonstr = {
        'firstname': name_1,
        'lastname': name_2,
        'sex': sex[:1],
        'email': email,
        'dateadd': currdatetime,
        'dateborn': currdatetime,
        'idParent': str(parent),
        'idCouple': idCouple,
    }
    query_v = json_humans(jsonstr)
    queryes.append(query_v)

    return queryes


def restart(sess):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    empty_data_in_use()
    f = open("START-UP.txt", "r")
    new = f.read()
    live_new = str(new).strip().split('live.cnf=\n')[1]
    live_new = live_new.strip().split('\n=end')[0]
    db_new = str(new).strip().split('db.json=\n')[1]
    db_new = db_new.strip().split('\n=end')[0]
    stat_new = str(new).strip().split('stat.cnf=\n')[1]
    stat_new = stat_new.strip().split('\n=end')[0]
    flive = open("live.cnf", "w")
    if flive.write(live_new):
        print('live restart done !!')
    else:
        print('live restart error !!')
    fdb = open("db.json", "w")
    if fdb.write(db_new):
        print('db restart done !!')
    else:
        print('db restart error !!')
    fstat = open("stat.cnf", "w")
    if fstat.write(stat_new):
        print('stat restart done !!')
    else:
        print('stat restart error !!')


def GenHuman(limit=100, parent=''):
    print('\n-------- GenHuman --------------')
    # if __name__ == "__main__":

    # db = Database()

    numhuman = stats(var='num_human')
    print('numhuman = ' + str(numhuman))
    if numhuman == 0:
        parent = '0'
        limit = 2

    print('limit = ' + str(limit))
    # generate Human
    num_generating = 0
    if limit > 1:
        queryes = []
        queryx = ''
        for w in range(random.randint(limit, limit)):
            currdatetime = GetLive()
            if currdatetime is not None:
                # Data Insert into the table
                num_generating += 1
                queryes = generate_json_human(queryes, parent, currdatetime)
        queryx = ',\n' . join(queryes)
        print('306:num_generating = ' + str(num_generating))
        if num_generating > 0:
            optimizedb()
            numberOfLine_InFile = numberOfLineInFile('db.json')
            print('before insert :' + str(numberOfLine_InFile))
            try:
                # queryx = queryx.exncode('utf-8')
                to_line = numberOfLine_InFile - 2
                print('insert to line : ' + str(to_line))
                text_to_insert = ',\n' + queryx
                print(queryx)
                InsertDataToDB('db.json', insert_to_line=to_line, text=text_to_insert)
                optimizedb()
                numberOfLine_InFile = numberOfLineInFile('db.json')
                print('after insert :' + str(numberOfLine_InFile))
                last_numhuman = int(numhuman) + int(num_generating)
                real_numhuman = numHuman()
                if real_numhuman != last_numhuman:
                    last_numhuman = real_numhuman
                find_replace_line(file_name='stat.cnf', text_find='num_human=', text_replace='num_human=' + str(last_numhuman))
                # if last_numhuman == 2:
                #     findID_updateKey(file_name='db.json', find_id='c86bb95295a4d42f4913eb8f4eeffdb3', key='idCouple', key_new_value='xxx')
            except IndexError:
                print('Error while write.....')
            print('414:num_generating = ' + str(num_generating))
            try:
                print('416:num_generating = ' + str(num_generating))
                return int(num_generating)
            except IndexError:
                print('419:num_generating = ' + str(num_generating))
                num_generating = 0
                return int(num_generating)


def GetNoCouple(sexrequest, temp_data=''):
    # print('GetNoCouple()')
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    if temp_data == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = temp_data
    returns = ''
    for data in jloads['humans']:
        if data['idCouple'] == '' and data['sex'] == sexneed:
            # print(data)
            currdatetime = GetLive()
            age = get_age(currdatetime, data['dateborn']) + 25
            agecoupledx = GetConfig('agecoupled')
            agecoupledx1 = int(agecoupledx.strip().split(',')[0])
            agecoupledx2 = int(agecoupledx.strip().split(',')[1])
            if agecoupledx1 <= int(age) <= agecoupledx2:
                returns = data
                break
    return returns


def SetCouple(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print(this_function_name)
    # exit()
    startt = time.time()
    if getdata == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = getdata
    generate = 0
    hit = 0
    real_numcoupled = numCoupled()
    stat_numcoupled = int(get_stat(var='num_couple'))
    random_number_of_humans_tocouple = random.randint(10, 20)
    temp_data = {}
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        if cek_in_use(id=data['id']) is False:
            # print(sdata)
            if "'idCouple': ''" in sdata and 'datedied' not in sdata:
                agecoupledx = GetConfig('agecoupled')
                # print(agecoupledx)
                currdatetime = GetLive()
                age = math.floor(get_age(currdatetime, data['dateborn'], return_days=False))
                agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                if (agecoupledx1 + 3) == int(age):
                    print(data['firstname'] + ' [' + data['sex'] + '] : ' + str(age))
                if agecoupledx1 <= int(age):
                    # <= agecoupledx2:
                    # print('if age')
                    getornot = random.randint(0, 3)
                    if getornot == 0:
                        # print('getornot')
                        try:
                            if getdata == '':
                                insert_data_in_use(sess=this_function_name, id=data['id'])
                            # print(data)
                            choose_couple = GetNoCouple(sexrequest=data['sex'], temp_data=temp_data)
                            # print(choose_couple)
                            if choose_couple != '':
                                # print('if choose_couple')
                                if getdata == '':
                                    insert_data_in_use(sess=this_function_name, id=choose_couple['id'])
                                returnIndexOrder = findId_returnIndexOrder(find_id=choose_couple['id'])
                                index_num = int(returnIndexOrder.strip().split('|')[0])
                                line_num = int(returnIndexOrder.strip().split('|')[1])

                                # human ke-1
                                temp_data['humans'][hit]['idCouple'] = choose_couple['id']
                                temp_data['humans'][hit]['datecoupled'] = currdatetime

                                if index_num is not False:
                                    # human ke-2
                                    temp_data['humans'][index_num]['idCouple'] = data['id']
                                    temp_data['humans'][index_num]['datecoupled'] = currdatetime
                                if temp_data['humans'][hit]['idCouple'] != '' and temp_data['humans'][index_num]['idCouple'] != '':
                                    generate += 1

                                # exit('test 1 data....')

                        except IndexError:
                            print('Error.... SetCouple > try')
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        # print('\n\n' + str(temp_data))
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        # exit('selesai------------')
        # print(real_numcoupled, '|', stat_numcoupled)
        real_numcoupled = numCoupled()
        if stat_numcoupled != real_numcoupled:
            print('real !')
            tot_num_couple = real_numcoupled + generate
        else:
            print('stat !')
            tot_num_couple = stat_numcoupled + generate
        find_replace_line(file_name='stat.cnf', text_find='num_couple=', text_replace='num_couple=' + str(tot_num_couple))
        print('**COUPLED** >> {0} couples in {1}' . format(generate, fwaktu_proses))
        print('{0} couples generated' . format(tot_num_couple))
        # print(jloads)
    else:
        temp_data = jloads
    return temp_data


def set_pregnant(sess, temp_data, hit, id, currdatetime, generate, getdata):

    getornot = random.randint(0, 0)
    if getornot == 0:
        try:
            # if getdata == '':
            #     insert_data_in_use(sess=sess, id=id)
            temp_data['humans'][hit]['isPregnant'] = '1'
            temp_data['humans'][hit]['datepregnant'] = currdatetime

            if temp_data['humans'][hit]['isPregnant'] == '1':
                print('\n======================\nset_pregnant() ========================= \n' + str(temp_data['humans'][hit]))
                generate += 1

        except IndexError:
            print('Error.... set_pregnant > try')
    return generate


def SetPregnant(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print(this_function_name)
    startt = time.time()
    if getdata == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = getdata
    generate = 0
    hit = 0
    real_numPregnant = numPregnant()
    stat_numPregnant = int(get_stat(var='num_pregnant'))
    temp_data = {}
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        # print(data)
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        # print(sdata)
        if cek_in_use(id=data['id']) is False:
            # print('not in use : ' + data['id'])
            # print('SetPregnant ================================ ' + sdata)
            if (data['sex'] == 'F' or "'sex': 'F'" in sdata) and ("'isPregnant': '0'" in sdata or "'isPregnant'" not in sdata) and "'datecoupled':" in sdata:
                print('SetPregnant == if sex = F ================================ ' + sdata)
                currdatetime = GetLive()
                days_after_givingbirth = 0
                days_after_coupled = get_age(currdatetime, data['datecoupled'], return_days=True)
                if "dategivingbirth" in sdata:
                    days_after_givingbirth = get_age(currdatetime, data['dategivingbirth'], return_days=True)
                    print('AGE days_after_givingbirth' + str(days_after_givingbirth))

                pregnant_days_after_birth = GetConfig('pregnant_aftergbirth')
                pregnant_days_after_coupled = GetConfig('pregnant')
                print('pregnant_days_after_birth >> ' + pregnant_days_after_birth)
                print('pregnant_days_after_coupled >> ' + pregnant_days_after_coupled)
                if days_after_givingbirth > 0:
                    print('pregnant_days_after_birth = ' + str(pregnant_days_after_birth))
                    pregnant_days_after_birth_1 = math.floor(int(pregnant_days_after_birth.strip().split(',')[0]))
                    # print('pregnant_days_after_birth_1 = ' + str(pregnant_days_after_birth_1))
                    # pregnant_days_after_birth_2 = math.floor(int(pregnant_days_after_birth.strip().split(',')[1]))
                    # print('pregnant_days_after_birth_2 = ' + str(pregnant_days_after_birth_2))
                    if pregnant_days_after_birth_1 <= int(days_after_givingbirth):
                        # <= pregnant_days_after_birth_2:
                        generate += set_pregnant(this_function_name, temp_data, hit, data['id'], currdatetime, generate, getdata)

                elif days_after_coupled > 0:
                    print('GetConfig pregnant_days_after_coupled = ' + str(pregnant_days_after_coupled))
                    pregnant_days_after_coupled_1 = math.floor(int(pregnant_days_after_coupled.strip().split(',')[0]))
                    # print('pregnant_days_after_coupled_1 = ' + str(pregnant_days_after_coupled_1))
                    # pregnant_days_after_coupled_2 = math.floor(int(pregnant_days_after_coupled.strip().split(',')[1]))
                    # print('pregnant_days_after_coupled_2 = ' + str(pregnant_days_after_coupled_2))
                    print('days_after_coupled = ' + str(days_after_coupled))
                    if pregnant_days_after_coupled_1 <= int(days_after_coupled):
                        # <= pregnant_days_after_coupled_2:
                        generate += set_pregnant(this_function_name, temp_data, hit, data['id'], currdatetime, generate, getdata)
            # exit('test 1 data....')
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    # print('\n\n' + str(temp_data))
    # exit('TEST AJA--------------')
    if generate > 0:
        print('\nif generate > 0:\n' + str(temp_data))
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        # exit('selesai------------')
        # print(real_numPregnant, '|', stat_numPregnant)
        real_numPregnant = numPregnant()
        if stat_numPregnant != real_numPregnant:
            print('real !')
            tot_num_pregnant = real_numPregnant + generate
        else:
            print('stat !')
            tot_num_pregnant = stat_numPregnant + generate
        find_replace_line(file_name='stat.cnf', text_find='num_pregnant=', text_replace='num_pregnant=' + str(tot_num_pregnant))
        print('**pregnant** >> {0} pregnant in {1}' . format(generate, fwaktu_proses))
        print('{0} pregnant generated' . format(tot_num_pregnant))
        # print(jloads)
        # exit(temp_data)
    else:
        temp_data = jloads
    return temp_data


def SetGivingBirth(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print(this_function_name)
    startt = time.time()
    if getdata == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = getdata
    # print(str(jloads))
    # if "'isPregnant': '1'" in str(jloads):
    #     exit(str(jloads))
    # generate = 0
    hit = 0
    real_numPregnant = numPregnant()
    # stat_numPregnant = int(get_stat(var='num_pregnant'))
    stat_numHuman = int(get_stat(var='num_human'))
    temp_data = {}
    GenHuman_res = 0
    num_generating = 0
    limit = 0
    print('real_numPregnant = ' + str(real_numPregnant))
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        if cek_in_use(id=data['id']) is False:
            # print(sdata)
            if "'isPregnant': '1'" in sdata and "'datedied'" not in sdata:
                print(sdata)
                currdatetime = GetLive()
                # print('currdatetime = ' + currdatetime)
                days_after_pregnant = get_age(currdatetime, data['datepregnant'], return_days=True)
                print('days_after_pregnant = ' + str(days_after_pregnant))
                GetConfig_givingbirth = GetConfig('givingbirth')
                # print('GetConfig_givingbirth = ' + str(GetConfig_givingbirth))
                GetConfig_givingbirth_1 = int(GetConfig_givingbirth.strip().split(',')[0])
                GetConfig_givingbirth_2 = int(GetConfig_givingbirth.strip().split(',')[1])
                if GetConfig_givingbirth_1 <= int(days_after_pregnant):
                    # <= GetConfig_givingbirth_2:
                    try:
                        if temp_data['humans'][hit]['idCouple'] != '' and temp_data['humans'][hit]['id'] != '':
                            if getdata == '':
                                insert_data_in_use(sess=this_function_name, id=data['id'])
                            temp_data['humans'][hit]['dategivingbirth'] = currdatetime
                            temp_data['humans'][hit]['isPregnant'] = ''
                            temp_data['humans'][hit]['datepregnant'] = ''
                            parent = '{0}|{1}' . format(temp_data['humans'][hit]['idCouple'], temp_data['humans'][hit]['id'])
                            # print('parent = ' + parent)
                            if stat_numHuman < 100:
                                limit = random.randint(4, 7)
                            elif stat_numHuman >= 100:
                                limit = random.randint(3, 6)
                            elif stat_numHuman >= 1000:
                                limit = random.randint(2, 5)
                            elif stat_numHuman >= 10000:
                                limit = random.randint(1, 4)
                            print('stat_numHuman = ' + str(stat_numHuman))
                            print('limit = ' + str(limit))
                            if limit > 0:
                                GenHuman_res = GenHuman(limit=limit, parent=parent)
                                print('GenHuman_res = ' + str(GenHuman_res))
                                num_generating += GenHuman_res
                        else:
                            print('Error: PARENT empty.... set_givingbirth > try')

                    except IndexError:
                        print('Error.... set_givingbirth > try')
                # exit('test 1 data....')
        hit += 1
    print('num data hit = ' + str(hit))
    # data_append = ',\n' . join(data_gen)
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))

    if GenHuman_res > 0:
        print('\n\nafter ' + this_function_name + ' === \n' + str(temp_data))
    # exit('TEST AJA--------------')
    # if num_generating > 0:
        # exit('\n\n' + str(temp_data))
        # update_humans(json_=temp_data)
        if getdata == '':
            empty_data_in_use(sess=this_function_name)
        # exit('selesai------------')
        # print(real_numPregnant, '|', stat_numPregnant)
        print('**giving birth** >> {0} birth in {1}' . format(num_generating, fwaktu_proses))
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        temp_data = json.loads(fread)
        # exit(temp_data)
    else:
        temp_data = jloads

    return temp_data


def SetMenopause(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print(this_function_name)
    startt = time.time()
    if getdata == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = getdata
    generate = 0
    hit = 0
    temp_data = {}
    stat_numHuman = int(get_stat(var='num_human'))
    maxnum = 10000
    num_generating = 0
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        if cek_in_use(id=data['id']) is False:
            if data['sex'] == 'F' and 'datedied' not in sdata:
                currdatetime = GetLive()
                # print('currdatetime = ' + str(currdatetime))
                age = get_age(currdatetime, data['dateborn'], return_days=False)
                GetConfig_agemenopause = GetConfig('agemenopause')
                GetConfig_agemenopause_1 = int(GetConfig_agemenopause.strip().split(',')[0])
                GetConfig_agemenopause_2 = int(GetConfig_agemenopause.strip().split(',')[1])
                if GetConfig_agemenopause_1 <= int(age):
                    # <= GetConfig_agemenopause_2:
                    try:
                        if stat_numHuman < 100:
                            maxnum = 100
                        elif stat_numHuman >= 1000:
                            maxnum = 50
                        elif stat_numHuman >= 10000:
                            maxnum = 10
                        if stat_numHuman < 100:
                            maxnum = 100
                        elif stat_numHuman >= 100:
                            maxnum = 75
                        elif stat_numHuman >= 1000:
                            maxnum = 50
                        elif stat_numHuman >= 10000:
                            maxnum = 25
                        getornot = random.randint(0, maxnum)
                        if getornot == 0:
                            if getdata == '':
                                insert_data_in_use(sess=this_function_name, id=data['id'])
                            temp_data['humans'][hit]['datemenopause'] = currdatetime
                            generate += 1

                    except IndexError:
                        print('Error.... set_menopause > try')
                # exit('test 1 data....')
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        print('**menopause** >> {0} sets in {1}' . format(generate, fwaktu_proses))
    else:
        temp_data = jloads
    return temp_data


def SetDied(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print(this_function_name)
    startt = time.time()
    if getdata == '':
        f = open('db.json', 'r')
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        jloads = json.loads(fread)
    else:
        jloads = getdata
    stat_numHuman = int(get_stat(var='num_human'))
    maxnum = 10000
    generate = 0
    hit = 0
    temp_data = {}
    num_generating = 0
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        if cek_in_use(id=data['id']) is False:
            currdatetime = GetLive()
            # print('currdatetime = ' + str(currdatetime))
            age = get_age(currdatetime, data['dateborn'], return_days=False)
            GetConfig_agedied = GetConfig('agedied')
            GetConfig_agedied_1 = int(GetConfig_agedied.strip().split(',')[0])
            GetConfig_agedied_2 = int(GetConfig_agedied.strip().split(',')[1])
            # if GetConfig_agedied_1 <= int(age) <= GetConfig_agedied_2:
            if GetConfig_agedied_1 <= int(age):
                try:
                    if stat_numHuman < 100:
                        maxnum = 100
                    elif stat_numHuman >= 1000:
                        maxnum = 50
                    elif stat_numHuman >= 10000:
                        maxnum = 10
                    if stat_numHuman < 100:
                        maxnum = 100
                    elif stat_numHuman >= 100:
                        maxnum = 75
                    elif stat_numHuman >= 1000:
                        maxnum = 50
                    elif stat_numHuman >= 10000:
                        maxnum = 25
                    getornot = random.randint(0, maxnum)
                    if getornot == 0:
                        if getdata == '':
                            insert_data_in_use(sess=this_function_name, id=data['id'])
                        temp_data['humans'][hit]['datedied'] = currdatetime
                        generate += 1

                except IndexError:
                    print('Error.... set_died > try')
            # exit('test 1 data....')
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        print('**died** >> {0} sets in {1}' . format(generate, fwaktu_proses))
    else:
        temp_data = jloads
    return temp_data


def NumHumanLife(cond=''):
    db = Database()
    where = ''
    if cond is not None:
        where = cond
    return db.count("SELECT id FROM human WHERE 1 {0}" . format(where))


def NumHumanDied():
    db = Database()
    return db.count("SELECT id FROM human_died WHERE 1")


def LastID():
    # db = Database()
    # return db.getone2("SELECT id FROM human WHERE 1 ORDER BY id DESC LIMIT 1")
    return True

# db-text


def get_age(currdatetime, dateborn, return_days=False):
    date_format = "%Y-%m-%d %H:%M:%S"
    age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(dateborn), date_format)
    if return_days is False:
        return math.floor(age.days / 365)
    else:
        return math.floor(age.days)


def clear_in_use(datas, sess):

    temp_data['humans'][hit]['in__use'] = sess


def get_stat(var):
    f = open('stat.cnf', 'r')
    fread = f.read()
    f.close()
    get = fread.strip().split(var + '=')[1]
    return get.strip().split('\n')[0]


def findID_updateData_json(find_id, body):
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    f.close()
    jloads = json.loads(fread)
    hit = 0
    linenum = 3
    total_line = numberOfLineInFile('db.json')
    LAST_line = total_line - 2
    print('LAST_line=' + str(LAST_line))
    for data in jloads['humans']:
        if data['id'] == find_id:
            # data[key] = key_new_value
            # jdumps_data = json.dumps(data)
            # print(data)
            # print(body)
            merged_dict = {**data, **body}
            print('')
            print('linenum ::: ' + str(linenum))
            # print(merged_dict)
            jdumps_data = json.dumps(merged_dict)
            if linenum == LAST_line:
                text = '' + jdumps_data + '\n'
                print('------ DATA LAST LINE --------------')
            else:
                text = '' + jdumps_data + ',\n'
            print(jdumps_data)
            replace_line('db.json', line_num=linenum, text=text)
            break
        linenum += 1
        hit += 1


def findID_updateData(find_id, key, key_new_value):
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    f.close()
    jloads = json.loads(fread)
    hit = 0
    linenum = 3
    for data in jloads['humans']:
        if data['id'] == find_id:
            data[key] = key_new_value
            jdumps_data = json.dumps(data)
            # print('linenum ::: ' + str(linenum))
            # print(jdumps_data)
            replace_line('db.json', line_num=linenum, text='' + jdumps_data + ',\n')
            break
        linenum += 1
        hit += 1


def update_humans(json_):
    jdumps = json.dumps(json_)
    jdumps = jdumps.replace('{"humans": [{', '{\n"humans":\n[\n{')
    jdumps = jdumps.replace('}, {', '},\n{')
    if jdumps.endswith('}]}'):
        jdumps = jdumps.replace('}]}', '}\n]\n}')
    if jdumps.endswith('},\n]\n}'):
        jdumps = jdumps.replace('},\n]\n}', '}\n]\n}')
    # print(jdumps)
    # return jdumps
    # if "'isPregnant': '1'" in str(json_):
    #     exit(str(json_))
    f = open('db.json', "w")
    f.write(str(jdumps))
    f.close()
    # time.sleep(1)


def findId_returnIndexOrder(find_id):
    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    f.close()
    jloads = json.loads(fread)
    hit = 0
    returns = False
    for data in jloads['humans']:
        if data['id'] == find_id:
            returns_hit = hit
            returns_line_number = hit + 4
            returns = str(returns_hit) + '|' + str(returns_line_number)
            break
        hit += 1
    return returns


def load_database(file_name):

    f = open(file_name, 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    f.close()
    return json.loads(fread)


def numberOfLineInFile(thefilepath):
    return len(open(thefilepath).readlines())


def readInSpecLineFile(thefilepath, line_num):
    lines = open(thefilepath, 'r').readlines()
    return lines[line_num]


def readInSpecLineFile_key(thefilepath, line_num, key):
    lines = open(thefilepath, 'r').readlines()
    fread = str(lines[line_num]).replace('},\n', '}')
    fread = fread.replace('\n', '')
    print(fread)
    # fread = fread.encode('utf-8')
    # print(fread)
    jloads = json.loads(fread)
    return jloads[key]


def is_file_not_in_use(file_name):
    if os.path.exists(file_name):
        try:
            os.rename(file_name, file_name)
            print('Available....')
            return True
        except OSError as e:
            # print 'Access-error on file "' + f + '"! \n' + str(e)
            print('Database busy....')
            return False
    else:
        return False


def LockFile(file_name):
    lock = LockFile(file_name)
    lock.acquire()


def UnLockFile(file_name):
    lock = LockFile(file_name)
    lock.release()


def LockFile_status(file_name):
    lock = LockFile(file_name)
    lock.is_locked()


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


def findText_returnData(file_name, text_find):
    fopen = open(file_name, 'r')
    fopen_read = fopen.read()
    fopen_part = fopen_read.strip().split('\n')
    linemark = 0
    returns = False
    for data in fopen_part:
        # print(data)
        if text_find in data:
            returns = data
            break
        linemark += 1
    fopen.close()
    return returns


def findID_returnData(file_name, text_find):
    fopen = open(file_name, 'r')
    fopen_read = fopen.read()
    fopen_part = fopen_read.strip().split('\n')
    linemark = 0
    for data in fopen_part:
        # print(data)
        if '"id":"' + text_find + '"' in data:
            returns = linemark + '|||' + data
            break
        linemark += 1
    fopen.close()
    return returns


def findID_updateKey(file_name, find_id, key, key_new_value):
    f = open(file_name, 'r')
    fread = f.read()
    f.close()
    # print(fread)
    fread = str(fread).replace('\n', '')
    # print(fread)
    fread = fread.encode('utf-8')
    # print(fread)
    jloads = json.loads(fread)
    hit = 0
    for data in jloads['humans']:
        if data['id'] == find_id and data['idCouple'] == '':
            print('=========================\ndata ke-' + str(hit))
            print(data)
            # print('sebelum update')
            # print(data)
            # data[key] = key_new_value
            jloads['humans'][hit][key] = key_new_value
            # print('setelah update **')
            # print(data)
        hit += 1
    # print('after  combine')
    # print(jloads['humans'][6])
    # print(jloads['humans'][5])
    jdumps = json.dumps(jloads)
    print(jdumps)
    jdumps = jdumps.replace('{"humans": [{', '{\n"humans":\n[\n{')
    jdumps = jdumps.replace('}, {', '},\n{')
    if jdumps.endswith('}]}'):
        jdumps = jdumps.replace('}]}', '}\n]\n}')
    if jdumps.endswith('},\n]\n}'):
        jdumps = jdumps.replace('},\n]\n}', '}\n]\n}')
    # time.sleep(3)
    f = open(file_name, "w")
    f.write(str(jdumps))
    f.close()


def InsertDataToDB(filedb, insert_to_line, text):
    print('[[[[ InsertDataToDB ]]]]')
    f = open(filedb, "r")
    contents = f.readlines()
    f.close()
    contents.insert(insert_to_line, text + '\n')
    f = open(filedb, "w")
    contents = "".join(contents)
    # print('contents = ' + contents)
    if f.write(contents):
        print('InsertDataToDB done !!')
    else:
        print('InsertDataToDB error !!')
    f.close()
    f2 = open(filedb, "r")
    contents2 = f2.read()
    # print('contents 2 = ' + contents2)
    f2.close()
    # time.sleep(1)


def insert_data_in_use(sess, id):
    # time.sleep(1)
    time.sleep(1)
    f = open("inuse/" + sess + ".data", 'a')
    with open("inuse/" + sess + ".data", 'a') as outfile:
            outfile.write(id + "\n")
    f.close()


def empty_data_in_use(sess=''):
    print('empty_data_in_use')
    # time.sleep(1)
    if sess == '':
        for file in os.listdir("inuse"):
            try:
                f = open("inuse/" + file, 'w')
                with open("inuse/" + file, 'w') as outfile:
                    if outfile.write(""):
                        print('empty_data_in_use')
                    else:
                        print('ERROR -- empty_data_in_use')
                f.close()
            except IOError:
                print('IOError')
    else:
        print('EMPTY IN USE in : ' + sess)
        f = open("inuse/" + sess + ".data", 'w')
        with open("inuse/" + sess + ".data", 'w') as outfile:
            if outfile.write(""):
                print('empty_data_in_use : ' + sess)
            else:
                print('ERROR -- empty_data_in_use : ' + sess)
        f.close()


def cek_in_use(id):
    # import os
    # for file in os.listdir("inuse"):
    #     find = findText_returnData("inuse/" + file, text_find=id)
    #     if find == id:
    #         return True
    #     else:
    #         return False
    return False


def numHuman():
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    # print(fread)
    fread = str(fread).replace('\n', '')
    # print(fread)
    fread = fread.encode('utf-8')
    # print(fread)
    jloads = json.loads(fread)
    return len(jloads['humans'])


def numCoupled():
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    # hit = 0
    coupled = [n for n in jloads['humans'] if n['idCouple'] != '']
    return len(coupled)


def numPregnant():
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    # datas = [n for n in jloads['humans'] if n['isPregnant'] == '1']
    # return len(datas)
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        try:
            if "'isPregnant': '1'" in sdata:
                n += 1
        except IndexError:
            pass
    return n


def stats(var):
    openstat = open('stat.cnf', 'r')
    stat = openstat.read()
    # print(stat)
    varnh = str(stat).strip().split(var + '=')[1]
    return varnh.strip().split('\n')[0]


def getHumanId(index):
    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    return jloads['humans'][index]['id']


def optimizedb():
    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = str(fread).replace('}\n,\n{', '},\n{')
    # print(fread)
    fread = fread.encode('utf-8')
    f.close()
    jloads = json.loads(fread)
    # jloads['humans']
    fread = str(json.dumps(jloads))
    fread = fread.replace('{"humans": [{', '{\n"humans":\n[\n{')
    fread = fread.replace('}, {', '},\n{')
    if fread.endswith('}]}'):
        fread = fread.replace('}]}', '}\n]\n}')
    if fread.endswith('},\n]\n}'):
        fread = fread.replace('},\n]\n}', '}\n]\n}')
    f = open('db.json', 'w')
    f.write(fread)
    f.close()
    time.sleep(1)
    return True
