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


def firstname(sex):
    if sex == 'M':
        first = 'budi joko slamet teguh widodo herman hermawan wawan doni dodi didik didit dudung dadang tatang aceng akum asep afif memet mamat amat wasiyat tris rio roy rahmat rohmat eko fajar ujang'
    elif sex == 'F':
        first = 'budiani widy widya hermin wiwin dini rini rina rani nina nani nini ninik nunik tini ekowati fitriani dika suci suciati suciani'
    out = first.strip().split(' ')
    len_out = len(out)
    randoms = random.randint(0, (len_out - 1))
    return out[randoms].title()


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
    sexx = random.randint(0, 1)
    if sexx is 0:
        sex = 'M'
    else:
        sex = 'F'
    name_1 = firstname(sex=sex) + ' ' + genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
    name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
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
    # print('\n-------- GenHuman --------------')
    # if __name__ == "__main__":

    numberOfLine_InFile = 0
    numhuman = 0
    numhuman = stats(var='num_human')
    if numhuman == 0:
        parent = '0'
        limit = 2

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
                print('|', end='', flush=True)
        queryx = ',\n' . join(queryes)
        # exit(' = ' + str(num_generating))
        if num_generating > 0:
            return str(queryx)


def GetNoCouple(sexrequest, temp_data=''):
    # print('GetNoCouple()')
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    if temp_data == '':
        jloads = loads_dbjson()
    else:
        jloads = temp_data
    returns = ''
    for data in jloads['humans']:
        sdata = str(data)
        if data['idCouple'] == '' and data['sex'] == sexneed and "'datemenopause'" not in sdata and "'datedied'" not in sdata:
            # print(data)
            currdatetime = GetLive()
            age = get_age(currdatetime, data['dateborn'])
            agecoupledx = GetConfig('agecoupled')
            agecoupledx1 = int(agecoupledx.strip().split(',')[0])
            agecoupledx2 = int(agecoupledx.strip().split(',')[1])
            if agecoupledx1 <= int(age) <= agecoupledx2:
                returns = data
                break
    return returns


def SetCouple(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print('\n\n' + this_function_name)
    # exit()
    startt = time.time()
    if getdata == '':
        jloads = loads_dbjson()
    else:
        jloads = getdata
    generate = 0
    hit = 0
    stat_numcoupled = int(get_stat(var='num_couple'))
    stat_numHuman = int(get_stat(var='num_human_life'))
    temp_data = {}
    n_notset = 0
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        # print('hit' + str(hit))
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        # print(sdata)
        if cek_in_use(id=data['id']) is False and is_run() is True:
            if data['idCouple'] == '' and "'datedied'" not in sdata:
                # print(sdata)
                agecoupledx = GetConfig('agecoupled')
                currdatetime = GetLive()
                # print('currdatetime : ' + currdatetime)
                age = math.floor(get_age(currdatetime, data['dateborn'], return_days=False))
                agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                if agecoupledx1 <= int(age) or agecoupledx2 < int(age):
                    # <= agecoupledx2:
                    maxnum = 0
                    if stat_numHuman >= 100:
                        maxnum = 0
                    if stat_numHuman >= 1000:
                        maxnum = 0
                    if stat_numHuman >= 10000:
                        maxnum = 1
                    if stat_numHuman >= 100000:
                        maxnum = 2
                    getornot = random.randint(0, maxnum)
                    if getornot == 0:
                        # print('if getornot')
                        try:
                            if getdata == '':
                                insert_data_in_use(sess=this_function_name, id=data['id'])
                            choose_couple = GetNoCouple(sexrequest=data['sex'], temp_data=temp_data)
                            name_sex_1 = data['firstname'] + ' [' + data['sex'] + ']'
                            # print(name_sex_1, ' + ', end=' ', flush=True)
                            if len(str(choose_couple)) > 10:
                                # print('if choose_couple')
                                if getdata == '':
                                    insert_data_in_use(sess=this_function_name, id=choose_couple['id'])
                                returnIndexOrder = findId_returnIndexOrder(find_id=choose_couple['id'])
                                index_num = int(returnIndexOrder.strip().split('|')[0])
                                # line_num = int(returnIndexOrder.strip().split('|')[1])

                                # human ke-1
                                temp_data['humans'][hit]['idCouple'] = choose_couple['id']
                                temp_data['humans'][hit]['datecoupled'] = currdatetime

                                name_sex_2 = choose_couple['firstname'] + ' [' + choose_couple['sex'] + ']'
                                # print(name_sex.ljust(10, ' ') + ', age : ' + str(age), end='\t', flush=True)

                                if index_num is not False:
                                    # human ke-2
                                    temp_data['humans'][index_num]['idCouple'] = data['id']
                                    temp_data['humans'][index_num]['datecoupled'] = currdatetime
                                if temp_data['humans'][hit]['idCouple'] != '' and temp_data['humans'][index_num]['idCouple'] != '':
                                    generate += 1
                                    # print(name_sex_2, '\n')
                                    print(str(generate) + '. ' + name_sex_1 + ' + ' + name_sex_2)
                                    # print('generate = ' + str(generate))
                                    # print('|', end='', flush=True),

                                # exit('test 1 data....')

                        except IndexError:
                            print('Error.... SetCouple > try')
        hit += 1
        simulation_limit_couple = GetConfig('simulation_limit_couple')
        if generate >= simulation_limit_couple:
            print('over ' + str(simulation_limit_couple))
            break
            # continue
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        # tot_num_couple = stat_numcoupled + generate
        # find_replace_line(file_name='stat.cnf', text_find='num_couple=', text_replace='num_couple=' + str(tot_num_couple))
        print('\n**COUPLED** >> {0} couples in {1}' . format(generate, fwaktu_proses))
        # print('{0} couples generated' . format(tot_num_couple))
    else:
        temp_data = jloads
    # update_stat(temp_data)
    return temp_data


def set_pregnant(sess, temp_data, hit, id, currdatetime, generate, getdata):

    stat_numHuman = int(get_stat(var='num_human_life'))
    maxnum = 0
    if stat_numHuman >= 100:
        maxnum = 0
    if stat_numHuman >= 1000:
        maxnum = 1
    if stat_numHuman >= 10000:
        maxnum = 2
    getornot = 0
    getornot = random.randint(0, maxnum)
    getornot = 0
    if getornot == 0:
        try:
            temp_data['humans'][hit]['isPregnant'] = '1'
            temp_data['humans'][hit]['datepregnant'] = currdatetime
            # exit('exit = \n' + str(temp_data['humans'][hit]))
            generate += 1
            print('|', end='', flush=True),

        except IndexError:
            print('Error.... set_pregnant > try')
    return generate


def SetPregnant(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print('\n\n' + this_function_name)
    startt = time.time()
    if getdata == '':
        jloads = loads_dbjson()
    else:
        jloads = getdata
    generate = 0
    hit = 0
    temp_data = {}
    n_notset = 0
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
            if data['sex'] == 'F' and data['idCouple'] != '' and ("'isPregnant': '0'" in sdata or "'isPregnant'" not in sdata) and "'datemenopause'" not in sdata and "'datedied'" not in sdata:
                currdatetime = GetLive()
                days_after_givingbirth = 0
                days_after_coupled = get_age(currdatetime, data['datecoupled'], return_days=True)
                if "dategivingbirth" in sdata:
                    days_after_givingbirth = get_age(currdatetime, data['dategivingbirth'], return_days=True)

                pregnant_days_after_birth = GetConfig('pregnant_aftergbirth')
                pregnant_days_after_coupled = GetConfig('pregnant')
                if days_after_givingbirth > 0:
                    pregnant_days_after_birth_1 = math.floor(int(pregnant_days_after_birth.strip().split(',')[0]))
                    pregnant_days_after_birth_2 = math.floor(int(pregnant_days_after_birth.strip().split(',')[1]))
                    if pregnant_days_after_birth_1 <= int(days_after_givingbirth) or pregnant_days_after_birth_2 < int(days_after_givingbirth):
                        # <= pregnant_days_after_birth_2:
                        # print('sdata = \n' + sdata)
                        generate += set_pregnant(this_function_name, temp_data, hit, data['id'], currdatetime, generate, getdata)

                elif days_after_coupled > 0:
                    pregnant_days_after_coupled_1 = math.floor(int(pregnant_days_after_coupled.strip().split(',')[0]))
                    pregnant_days_after_coupled_2 = math.floor(int(pregnant_days_after_coupled.strip().split(',')[1]))
                    if pregnant_days_after_coupled_1 <= int(days_after_coupled) or pregnant_days_after_coupled_2 < int(days_after_coupled):
                        # <= pregnant_days_after_coupled_2:
                        # print('sdata = \n' + sdata)
                        generate += set_pregnant(this_function_name, temp_data, hit, data['id'], currdatetime, generate, getdata)
                time.sleep(0)
        if generate < 1:
            n_notset += 1
        if n_notset >= 100:
            # print('trying 10x with null generated')
            break
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        print('\n**pregnant** >> {0} pregnant in {1}' . format(generate, fwaktu_proses))
    else:
        temp_data = jloads
    # update_stat(temp_data)
    return temp_data


def SetGivingBirth(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print('\n\n' + this_function_name)
    startt = time.time()
    if getdata == '':
        jloads = loads_dbjson()
    else:
        jloads = getdata
    # generate = 0
    hit = 0
    # real_numPregnant = numPregnant()
    stat_numPregnant = int(get_stat(var='num_pregnant'))
    print('stat_numPregnant = ' + str(stat_numPregnant))
    stat_numHuman = int(get_stat(var='num_human_life'))
    temp_data = {}
    generate = 0
    GenHuman_res = 0
    GenHuman_res_append = []
    num_generating = 0
    limit = 1
    n_notset = 0
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    if stat_numPregnant > 0:
        for data in jloads['humans']:
            if temp_data == {}:
                temp_data = jloads
                data = temp_data['humans'][hit]
            else:
                pass
            sdata = str(data)
            if cek_in_use(id=data['id']) is False and is_run() is True:
                # print(sdata)
                if "'isPregnant': '1'" in sdata and "'datemenopause'" not in sdata and "'datedied'" not in sdata:
                    # exit(sdata)
                    currdatetime = GetLive()
                    # print('currdatetime = ' + currdatetime)
                    days_after_pregnant = get_age(currdatetime, data['datepregnant'], return_days=True)
                    GetConfig_givingbirth = GetConfig('givingbirth')
                    # print('GetConfig_givingbirth = ' + str(GetConfig_givingbirth))
                    GetConfig_givingbirth_1 = int(GetConfig_givingbirth.strip().split(',')[0])
                    # GetConfig_givingbirth_2 = int(GetConfig_givingbirth.strip().split(',')[1])
                    if GetConfig_givingbirth_1 <= int(days_after_pregnant):
                        # print('days_after_pregnant = ' + str(days_after_pregnant))
                        # <= GetConfig_givingbirth_2:
                        try:
                            if temp_data['humans'][hit]['idCouple'] != '' and temp_data['humans'][hit]['id'] != '':
                                # exit(sdata)
                                if getdata == '':
                                    insert_data_in_use(sess=this_function_name, id=data['id'])
                                temp_data['humans'][hit]['dategivingbirth'] = currdatetime
                                temp_data['humans'][hit]['isPregnant'] = '0'
                                temp_data['humans'][hit]['datepregnant'] = ''
                                parent = '{0}|{1}' . format(temp_data['humans'][hit]['idCouple'], temp_data['humans'][hit]['id'])
                                if stat_numHuman >= 100:
                                    limit = random.randint(3, 6)
                                if stat_numHuman >= 1000:
                                    limit = random.randint(2, 5)
                                if stat_numHuman >= 10000:
                                    limit = random.randint(1, 4)
                                if stat_numHuman >= 100000:
                                    limit = random.randint(1, 3)
                                if limit < 1:
                                    limit = random.randint(3, 6)
                                if limit > 0:
                                    # exit(sdata)
                                    GenHuman_res = GenHuman(limit=limit, parent=parent)
                                    if GenHuman_res is not None:
                                        update_humans(json_=temp_data)
                                        GenHuman_res_append.append(GenHuman_res)
                                        # exit(GenHuman_res)
                            else:
                                print('Error: PARENT empty.... set_givingbirth > try')

                        except IndexError:
                            print('Error.... set_givingbirth > try')
                    # exit('test 1 data....')
            if generate < 1:
                n_notset += 1
            # if n_notset >= 1000:
            #     # print('trying 10x with null generated')
            #     break
            hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    # exit(GenHuman_res_append)
    if GenHuman_res_append != []:
        # print('GenHuman_res_append')
        # print(GenHuman_res_append)
        queries = ''
        queries = '' . join(GenHuman_res_append)
        queries = queries.replace('}{"id"', '}, {"id"')
        # print('queries')
        # exit(queries)
        # count repeated > "id":
        repe = queries.strip().split('"id":')
        num_generating = len(repe) - 1
        # nrep = 0
        # for re in repe:

        temp_data_dumps = json.dumps(temp_data['humans'])
        dall = temp_data_dumps + queries
        dall = dall.replace('}][{', '}, {')
        dall = dall.replace('}]{', '}, {')
        dall = dall.replace('}]\n{', '}, {')
        dall = dall.replace('}, {', '},\n{')
        dall = dall.replace('}{', '},\n{')
        dall = '{"humans": ' + dall + '\n]\n}'
        dall2 = dall.replace('},\n{', '}, {')
        dall2 = dall.replace('\n]\n}', ']}')
        dall2 = dall.replace('}]]}', '}]}')
        dall2 = dall.replace('}]\n]\n}', '}]}')
        # dall2 = dall2.encode('utf-8')
        # print(dall_loads)
        # with open('db-test.json', 'w') as the_file:
        #     if the_file.write(str(dall2)):
        #         print('queries >>> writed !!!')
        dall_loads = json.loads(dall2)

        if getdata == '':
            empty_data_in_use(sess=this_function_name)
        print('\n**giving birth** >> {0} birth in {1}' . format(num_generating, fwaktu_proses))
        # temp_data = loads_dbjson()
        temp_data = dall_loads
    else:
        temp_data = jloads
    # update_stat(temp_data)
    return temp_data


def loads_dbjson():
    with open('db.json', 'r') as f:
        fread = f.read()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        f.close()
        return json.loads(fread)


def genmaxnum_getornot(numhuman):
    maxnum = 0
    if numhuman >= 100:
        maxnum = 400
    if numhuman >= 1000:
        maxnum = 300
    if numhuman >= 10000:
        maxnum = 200
    return maxnum


def SetMenopause(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print('\n\n' + this_function_name)
    startt = time.time()
    if getdata == '':
        jloads = loads_dbjson()
    else:
        jloads = getdata
    generate = 0
    hit = 0
    temp_data = {}
    stat_numHuman = int(get_stat(var='num_human_life'))
    # real_numhuman = numHuman()
    maxnum = 10000
    # num_generating = 0
    n_notset = 0
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
            if data['sex'] == 'F' and "'isPregnant': '0'" in sdata and "'datedied'" not in sdata:
                currdatetime = GetLive()
                # print('currdatetime = ' + str(currdatetime))
                age = get_age(currdatetime, data['dateborn'], return_days=False)
                GetConfig_agemenopause = GetConfig('agemenopause')
                GetConfig_agemenopause_1 = int(GetConfig_agemenopause.strip().split(',')[0])
                GetConfig_agemenopause_2 = int(GetConfig_agemenopause.strip().split(',')[1])
                # random_range = random.randint(GetConfig_agemenopause_1, GetConfig_agemenopause_2)
                if GetConfig_agemenopause_1 < int(age):
                    if getdata == '':
                        insert_data_in_use(sess=this_function_name, id=data['id'])
                    temp_data['humans'][hit]['datemenopause'] = currdatetime
                    generate += 1
                    print('|', end='', flush=True),
                elif GetConfig_agemenopause_1 <= int(age):
                    try:
                        maxnum = genmaxnum_getornot(stat_numHuman)
                        getornot = random.randint(0, maxnum)
                        if getornot == 0:
                            # print('getornot :::: ' + str(getornot))
                            if getdata == '':
                                insert_data_in_use(sess=this_function_name, id=data['id'])
                            temp_data['humans'][hit]['datemenopause'] = currdatetime
                            generate += 1
                            print('|', end='', flush=True),

                    except IndexError:
                        print('Error.... set_menopause > try')
                # exit('test 1 data....')
        # if generate < 1:
        #     n_notset += 1
        # if n_notset >= 10:
        #     print('trying 10x with null generated')
        #     break
        hit += 1
        simulation_limit_menopause = GetConfig('simulation_limit_menopause')
        if generate >= simulation_limit_menopause:
            break
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        print('\n**menopause** >> {0} sets in {1}' . format(generate, fwaktu_proses))
    else:
        temp_data = jloads
    # update_stat(temp_data)
    return temp_data


def SetDied(sess, getdata=''):
    this_function_name = sess + '|' + sys._getframe().f_code.co_name
    print('\n\n' + this_function_name)
    startt = time.time()
    if getdata == '':
        jloads = loads_dbjson()
    else:
        jloads = getdata
    stat_numHuman = int(get_stat(var='num_human_life'))
    # real_numhuman = numHuman()
    maxnum = 10000
    generate = 0
    hit = 0
    temp_data = {}
    n_notset = 0
    # num_generating = 0
    currdatetimexx = GetLive()
    print('currdatetime = ' + str(currdatetimexx))
    for data in jloads['humans']:
        if temp_data == {}:
            temp_data = jloads
            data = temp_data['humans'][hit]
        else:
            pass
        sdata = str(data)
        if cek_in_use(id=data['id']) is False and "'isPregnant': '0'" in sdata:
            currdatetime = GetLive()
            # print('currdatetime = ' + str(currdatetime))
            age = get_age(currdatetime, data['dateborn'], return_days=False)
            GetConfig_agedied = GetConfig('agedied')
            GetConfig_agedied_1 = int(GetConfig_agedied.strip().split(',')[0])
            GetConfig_agedied_2 = int(GetConfig_agedied.strip().split(',')[1])
            # if GetConfig_agedied_1 <= int(age) <= GetConfig_agedied_2:

            if GetConfig_agedied_2 < int(age):
                if getdata == '':
                    insert_data_in_use(sess=this_function_name, id=data['id'])
                temp_data['humans'][hit]['datedied'] = currdatetime
                generate += 1
                print('|', end='', flush=True),

            elif GetConfig_agedied_1 <= int(age):
                try:
                    maxnum = genmaxnum_getornot(stat_numHuman)
                    getornot = random.randint(0, maxnum)
                    if getornot == 0:
                        # print('getornot :::: ' + str(getornot))
                        if getdata == '':
                            insert_data_in_use(sess=this_function_name, id=data['id'])
                        temp_data['humans'][hit]['datedied'] = currdatetime
                        generate += 1
                        print('|', end='', flush=True),

                except IndexError:
                    print('Error.... set_died > try')
            # exit('test 1 data....')
        # if generate < 1:
        #     n_notset += 1
        # if n_notset >= 10:
        #     print('trying 10x with null generated')
        #     break
        hit += 1
        simulation_limit_dies = GetConfig('simulation_limit_dies')
        if generate >= simulation_limit_dies:
            break
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if generate > 0:
        if getdata == '':
            update_humans(json_=temp_data)
            empty_data_in_use(sess=this_function_name)
        print('\n**died** >> {0} sets in {1}' . format(generate, fwaktu_proses))
    else:
        temp_data = jloads
    # update_stat(temp_data)
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


def is_run():
    maxnumhuman = GetConfig('simulation_maxnumhuman')
    numhuman = int(stats(var='num_human'))
    if numhuman <= maxnumhuman:
        return True
    else:
        return False


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
    with open(filedb, "r") as f:
        contents = f.readlines()
        f.close()
        contents.insert(insert_to_line, text + '\n')
    with open(filedb, 'w') as the_file:
        contents = "".join(contents)
        res = the_file.writelines(contents)
        print(text)

    # f = open(filedb, "w")
    # contents = "".join(contents)
    # # print('contents = ' + contents)
    # if f.write(contents):
    #     print('InsertDataToDB done !!')
    # else:
    #     print('InsertDataToDB error !!')
    f.close()
    # f2 = open(filedb, "r")
    # contents2 = f2.read()
    # print('contents 2 = ' + contents2)
    # f2.close()
    # time.sleep(1)


def insert_data_in_use(sess, id):
    # time.sleep(1)
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


def update_stat(temp_data=''):
    if is_run() is True:
        content = "num_human=" + str(numHuman(temp_data)) + "\nnum_human_life=" + str(numHumanLife(temp_data)) + "\nnum_coupleless_male=" + str(numCoupleless_M_extractmode(temp_data)) + "\nnum_coupleless_female=" + str(numCoupleless_F_extractmode(temp_data)) + "\nnum_couple=" + str(numCoupled(temp_data)) + "\nnum_couple_female_nomenopause=" + str(numCoupled_F_before_menopause(temp_data)) + "\nnum_pregnant=" + str(numPregnant(temp_data)) + "\nnum_menopause=" + str(numMenopause(temp_data)) + "\nnum_died=" + str(numDied(temp_data)) + ""
        # print(content)
        f = open('stat.cnf', 'w')
        try:
            f.write(content)
        except IOError:
            print('Error write to stat !!!')
        f.close()


def get_stat(var):
    f = open('stat.cnf', 'r')
    fread = f.read()
    f.close()
    get = fread.strip().split(var + '=')[1]
    return get.strip().split('\n')[0]


def numHuman(temp_data=''):
    # time.sleep(1)
    if temp_data == '':
        with open('db.json', 'r') as f:
            fread = f.read()
            f.close()
            # print(fread)
            fread = str(fread).replace('\n', '')
            # print(fread)
            fread = fread.encode('utf-8')
            # print(fread)
            jloads = json.loads(fread)
            # print(len(jloads['humans']))
            return len(jloads['humans'])
    else:
        temp_data = json.dumps(temp_data)
        temp_data_dumps = temp_data.strip().split('"id":')
        len_items = len(temp_data_dumps) - 1
        # print(len_items)
        return len_items


def numCoupled(temp_data=''):
    # time.sleep(1)
    if temp_data == '':
        with open('db.json', 'r') as f:
            fread = f.read()
            f.close()
            fread = str(fread).replace('\n', '')
            fread = fread.encode('utf-8')
            jloads = json.loads(fread)
            # hit = 0
            coupled = [n for n in jloads['humans'] if n['idCouple'] != '']
            return len(coupled)
    else:
        coupled = [n for n in temp_data['humans'] if n['idCouple'] != '']
        return len(coupled)


def numCoupled_F_before_menopause(temp_data=''):
    # time.sleep(1)
    jloads = loads_dbjson()
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        if data['sex'] == 'F' and data['idCouple'] != '' and "'datemenopause'" not in sdata and "'datedied'" not in sdata:
            n += 1
        else:
            n += 0
    return n


def numCoupleless_M(temp_data=''):
    # time.sleep(1)
    with open('db.json', 'r') as f:
        fread = f.read()
        f.close()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        jloads = json.loads(fread)
        # hit = 0
        coupleless = [n for n in jloads['humans'] if n['idCouple'] == '' and n['sex'] == 'M']
        return len(coupleless)


def numCoupleless_F(temp_data=''):
    # time.sleep(1)
    with open('db.json', 'r') as f:
        fread = f.read()
        f.close()
        fread = str(fread).replace('\n', '')
        fread = fread.encode('utf-8')
        jloads = json.loads(fread)
        # hit = 0
        coupleless = [n for n in jloads['humans'] if n['idCouple'] == '' and n['sex'] == 'F']
        return len(coupleless)


def numCoupleless_M_extractmode(temp_data=''):
    # time.sleep(1)
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        try:
            if "'idCouple': ''" in sdata and "'datedied'" not in sdata and data['sex'] == 'M':
                n += 1
        except IndexError:
            n += 0
    return n


def numCoupleless_F_extractmode(temp_data=''):
    # time.sleep(1)
    f = open('db.json', 'r')
    fread = f.read()
    f.close()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        try:
            if "'idCouple': ''" in sdata and "'datedied'" not in sdata and data['sex'] == 'F':
                n += 1
        except IndexError:
            n += 0
    return n


def numPregnant(temp_data=''):
    # time.sleep(1)
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
            n += 0
    return n


def numDied(temp_data=''):
    # time.sleep(1)
    jloads = loads_dbjson()
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print('died ===== ')
        # print(sdata)
        try:
            if "'datedied'" in sdata:
                # print('if')
                n += 1
            else:
                # print('else')
                n += 0
        except IndexError:
            n += 0
        # print('delete : ')
        # print(n)
    return n


def numMenopause(temp_data=''):
    # time.sleep(1)
    jloads = loads_dbjson()
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        try:
            if "'datemenopause': '" in sdata and "'datedied'" not in sdata:
                n += 1
        except IndexError:
            n += 0
    return n


def numHumanLife(temp_data=''):
    # time.sleep(1)
    jloads = loads_dbjson()
    n = 0
    for data in jloads['humans']:
        sdata = str(data)
        # print(sdata)
        try:
            if "'datedied': '" not in sdata:
                n += 1
        except IndexError:
            n += 0
    return n


def stats(var):
    with open('stat.cnf', 'r') as openstat:
        stat = openstat.read()
        # print(stat)
        try:
            varnh = str(stat).strip().split(var + '=')[1]
            return varnh.strip().split('\n')[0]
        except IndexError:
            print('trying get stat....')
            return 0


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
    # time.sleep(1)
    return True


def is_process(file):
    import psutil
    pids = psutil.pids()
    returns = False
    for p in pids:
        # print(p)
        try:
            p = psutil.Process(p)
            if 'chrome' in p.name():
                cmdline = p.cmdline()
                scmdline = str(cmdline)
                if '--type=renderer' in scmdline:
                    try:
                        mem = p.memory_full_info()
                        if mem.pss >= 300000000:
                            print(p.ppid(), p.pid, p.name(), 'memory : ' + str(mem.pss), 'Terminated' + str())
                            p.terminate()
                    except IndexError:
                        break
        except IndexError:
            break
        try:
            if p.name() == 'python':
                cmdline = p.cmdline()
                scmdline = str(cmdline)
                try:
                    if file in scmdline and "'run'" in scmdline:
                        # print(file)
                        print(scmdline)
                        returns = True
                        break
                except IndexError:
                    break
        except IndexError:
            break
    return returns


# pids = psutil.pids()
# for p in pids:
#     # print(p)
#     p = psutil.Process(p)
#     if 'chrome' in p.name():
#         cmdline = p.cmdline()
#         scmdline = str(cmdline)
#         if '--type=renderer' in scmdline:
#             mem = p.memory_full_info()
#             if mem.pss >= 115000000:
#                 print(p.ppid(), p.pid, p.name(), mem.pss)
#                 p.terminate()
