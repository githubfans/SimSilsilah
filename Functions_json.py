# from Database import Database
import random
import re
# import os
import json
import time
import datetime
from time import gmtime, strftime
import hashlib
from datetime import datetime
from datetime import timedelta
# import Cookie
# C = Cookie.SimpleCookie()


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

    numhuman = 0
    # LastID()
    # print(numhuman)
    if len(live) < 10:
        live = '1000-01-01 00:00:00'
        # print('GetLive() -- reset live type 1')
        fx = open("live.cnf", "w+")
        fx.write(str(live))
        fx.close()
    elif numhuman < 1:
        live = '1000-01-01 00:00:00'
        # print('GetLive() -- reset live type 2')
        fx = open("live.cnf", "w+")
        fx.write(str(live))
        fx.close()
    return live


def SetLive():
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


def generate_json_human(queryes, parent, currdatetime):
    print(currdatetime)
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
    print(email_suffix)
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


def GenHuman_json(limit=100, parent=''):
    # print('\n-------- GenHuman --------------')
    # if __name__ == "__main__":

    # db = Database()

    # numhuman = numHuman()
    # openstat = open('stat.cnf', 'r')
    # stat = openstat.read()
    # print(stat)
    # varnh = str(stat).strip().split('num_human=')[1]
    # numhuman = varnh.strip().split('\n')[0]
    numhuman = stats(var='num_human')
    print(numhuman)
    if numhuman == 0:
        parent = '0'
        limit = 2

    # print('limit:{0} | parent:{1}' . format(limit, parent))

    # generate Human
    num_generating = 0
    if limit > 1:
        queryes = []
        for w in range(random.randint(limit, limit)):
            currdatetime = GetLive()
            if currdatetime is not None:
                # Data Insert into the table
                num_generating += 1
                queryes = generate_json_human(queryes, parent, currdatetime)
        queryx = ',\n' . join(queryes)
        # print(queryx)
        # queryx = '{\n"humans":\n[\n' + queryx + '\n]\n}'
        optimizedb()
        numberOfLine_InFile = numberOfLineInFile('db.json')
        print('before insert :' + str(numberOfLine_InFile))
        if queryx != '':
            try:
                # queryx = queryx.exncode('utf-8')
                to_line = numberOfLine_InFile - 2
                if numberOfLine_InFile >= 7:
                    text_to_insert = ',\n' + queryx
                else:
                    text_to_insert = '' + queryx
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
        else:
            print('Tidak dilanjutkan ke proses WRTITE.TO.DB')


def GetNoCouple_json(sexrequest):
    print('GetNoCouple_json')
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    # daterequest = DateRequest('agecoupled')
    # res = db.getone("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND sex='{0}' AND idCouple='' ORDER BY dateborn ASC LIMIT 0,1" . format(sexneed))

    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    returns = ''
    for data in jloads['humans']:
        if data['idCouple'] == '' and data['sex'] == sexneed:
            # print(data)
            currdatetime = '1028-12-19 00:00:00'
            # GetLive()
            age = get_age(currdatetime, data['dateborn'])
            agecoupledx = GetConfig('agecoupled')
            agecoupledx1 = int(agecoupledx.strip().split(',')[0])
            agecoupledx2 = int(agecoupledx.strip().split(',')[1])
            if agecoupledx1 <= int(age) <= agecoupledx2:
                returns = data
                break
    return returns


def get_age(currdatetime, dateborn):
    # ts = '2013-01-12 15:27:43'
    # f = '%Y-%m-%d %H:%M:%S'
    # currdatetime = datetime.strptime(currdatetime, f)
    # dateborn = datetime.strptime(dateborn, f)
    # selisih = currdatetime - dateborn
    # return selisih
    date_format = "%Y-%m-%d %H:%M:%S"
    age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(dateborn), date_format)
    return age.days / 365


def SetCouple():
    startt = time.time()
    # db = Database()
    daterequest = DateRequest('agecoupled')
    simulation_limit_couple = GetConfig('simulation_limit_couple')
    # q_nocouple = "SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND idCouple='' AND dateborn<='{0}' ORDER BY dateborn ASC LIMIT 0,{1}" . format(daterequest, simulation_limit_couple)
    # human_nocouple = db.getall(q_nocouple)
    # print(q_nocouplse)
    # sys.exit()
    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    g = 0
    hit = 0
    for data in jloads['humans']:
        if data['idCouple'] == '':
            g += 1
            # print('---' + str(g))
            currdatetime = '1028-12-19 00:00:00'
            # GetLive()
            age = get_age(currdatetime, data['dateborn'])
            # print(age)

            agecoupledx = GetConfig('agecoupled')
            # print(agecoupledx)
            agecoupledx1 = int(agecoupledx.strip().split(',')[0])
            agecoupledx2 = int(agecoupledx.strip().split(',')[1])
            # random_age = random.randint(agecoupledx1, agecoupledx2)
            # print(age)
            if agecoupledx1 <= int(age) <= agecoupledx2:
                try:
                    choose_couple = GetNoCouple_json(sexrequest=data['sex'])
                    if choose_couple != '':
                        print('~~~~~~~~~~\nset couple for : ', data['id'], choose_couple['id'])
                        # perubahan data : dilakukan 2 data bersamaan
                        jloads['humans'][hit]['idCouple'] = choose_couple['id']
                        index_num = findId_returnIndexOrder(find_id=choose_couple['id'])
                        if index_num is not False:
                            jloads['humans'][index_num]['idCouple'] = data['id']
                        if jloads['humans'][hit]['idCouple'] != '' and jloads['humans'][index_num]['idCouple'] != '':
                            update_humans(json_=jloads)
                        # findID_updateKey(file_name='db.json', find_id=data['id'], key='idCouple', key_new_value=choose_couple['id'])
                        # time.sleep(1)
                        # findID_updateKey(file_name='db.json', find_id=choose_couple['id'], key='idCouple', key_new_value=data['id'])
                except IndexError:
                    print('Error.... SetCouple > try')
        hit += 1
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        print('**COUPLED** >> {0} couples in {1}' . format(g, fwaktu_proses))
        print(jloads)


def update_humans(json_):
    jdumps = json.dumps(json_)
    print(jdumps)
    jdumps = jdumps.replace('{"humans": [{', '{\n"humans":\n[\n{')
    jdumps = jdumps.replace('}, {', '},\n{')
    if jdumps.endswith('}]}'):
        jdumps = jdumps.replace('}]}', '}\n]\n}')
    if jdumps.endswith('},\n]\n}'):
        jdumps = jdumps.replace('},\n]\n}', '}\n]\n}')
    print(jdumps)
    # exit()
    # time.sleep(1)
    f = open('db.json', "w")
    f.write(str(jdumps))
    f.close()


def findId_returnIndexOrder(find_id):
    f = open('db.json', 'r')
    fread = f.read()
    fread = str(fread).replace('\n', '')
    fread = fread.encode('utf-8')
    jloads = json.loads(fread)
    g = 0
    hit = 0
    returns = False
    for data in jloads['humans']:
        if data['id'] == find_id:
            returns = hit
            break
        hit += 1
    return returns


def SetPregnant():
    startt = time.time()
    db = Database()
    simulation_limit_pregnant = GetConfig('simulation_limit_pregnant')
    q_human_nopregnant = "SELECT id, firstname, lastname, sex, dateborn, datecoupled, dategivingbirth FROM human WHERE 1 AND sex='F' AND datedied IS NULL AND datepregnant IS NULL AND datemenopause IS NULL AND idCouple>0 ORDER BY datecoupled ASC LIMIT 0,{0}" . format(simulation_limit_pregnant)
    human_nopregnant = db.getall(q_human_nopregnant)
    g = 0
    # print(q_human_nopregnant)
    if human_nopregnant:
        for pre in human_nopregnant:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            if currdatetime is not None:
                if pre['dategivingbirth'] is not None:
                    pregnantx = GetConfig('pregnant_aftergbirth')
                    days_after_gbirth = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dategivingbirth']), date_format)
                    days_after_last = days_after_gbirth.days

                elif pre['datecoupled'] is not None:
                    pregnantx = GetConfig('pregnant')
                    days_after_coupled = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datecoupled']), date_format)
                    days_after_last = days_after_coupled.days

                pregnantx1 = int(pregnantx.strip().split(',')[0])
                pregnantx2 = int(pregnantx.strip().split(',')[1])

                random_ = random.randint(pregnantx1, pregnantx2)
                if random_ <= days_after_last:
                    g += 1
                    db.insert("UPDATE human SET datepregnant='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        print('PREGNANT >> {0} females in {1}' . format(g, fwaktu_proses))


def SetGivingBirth():
    startt = time.time()
    db = Database()
    numhuman = LastID()
    simulation_limit_givingbirth = GetConfig('simulation_limit_givingbirth')
    human_givingbirth = db.getall("SELECT id, firstname, lastname, sex, idCouple, dateborn, datepregnant FROM human WHERE 1 AND sex='F' AND datedied IS NULL AND datepregnant IS NOT NULL AND idCouple>0 ORDER BY datepregnant ASC LIMIT 0,{0}" . format(simulation_limit_givingbirth))
    g = 0
    numgenerate = 0
    addbaby = 0
    if human_givingbirth:
        for pre in human_givingbirth:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            if currdatetime is not None and pre['datepregnant'] is not None:
                days_after_pregnant = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datepregnant']), date_format)
                days_after_pregnant = days_after_pregnant.days
                givingbirthx = GetConfig('givingbirth')
                givingbirthx1 = int(givingbirthx.strip().split(',')[0])
                givingbirthx2 = int(givingbirthx.strip().split(',')[1])
                random_ = random.randint(givingbirthx1, givingbirthx2)
                if random_ <= days_after_pregnant:
                    g += 1
                    parent = '{0}|{1}' . format(pre['idCouple'], pre['id'])
                    db.insert("UPDATE human SET datepregnant=NULL, dategivingbirth='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))

                    if numhuman >= 200000:
                        numgenerate = random.randint(1, 2)
                    if 100000 <= numhuman < 200000:
                        numgenerate = random.randint(1, random.randint(1, random.randint(1, random.randint(1, 5))))
                    elif 1000 <= numhuman < 100000:
                        numgenerate = random.randint(1, 5)
                    elif 0 <= numhuman < 1000:
                        numgenerate = random.randint(2, 10)

                    addbaby += numgenerate
                    # print('addbaby = {0}' . format(addbaby))
                    # print('numgenerate = {0}' . format(numgenerate))
                    # print('GIVING BIRTH >> {0} {1} : {2} baby(s)' . format(pre['firstname'], pre['lastname'], numgenerate))
                    GenHuman(numgenerate, parent)
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        print('Giving Birth >> {0} babies in {1}' . format(addbaby, fwaktu_proses))


def SetMenopause(sesscode):
    startt = time.time()
    db = Database()
    numhuman = LastID()
    addage = 0
    if numhuman < 100000:
        addage = 100
    elif 100000 <= numhuman < 200000:
        addage = 50
    elif 200000 <= numhuman < 300000:
        addage = 20
    daterequest = DateRequest('agemenopause')
    simulation_limit_menopause = GetConfig('simulation_limit_menopause')
    human_nomenopause = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND datemenopause IS NULL AND dateborn<='{0}' ORDER BY dateborn LIMIT 0,{1}" . format(daterequest, simulation_limit_menopause))
    g = 0
    if human_nomenopause:
        for pre in human_nomenopause:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dateborn']), date_format)
            age = int(age.days / 365)
            # print('days_after_coupled >> {0} {1} = {1}' . format(pre['firstname'], days_after_coupled))
            agemenopausex = GetConfig('agemenopause')
            agemenopausex1 = int(agemenopausex.strip().split(',')[0])
            agemenopausex2 = int(agemenopausex.strip().split(',')[1]) + addage
            random_menopause = random.randint(agemenopausex1, agemenopausex2)
            if random_menopause <= age:
                g += 1
                db.insert("UPDATE human SET datemenopause='{0}', in_use='{1}' WHERE 1 AND id={2}" . format(currdatetime, sesscode, pre['id']))
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        try:
            q_move_to_human_meno = "REPLACE INTO human_meno SELECT * FROM human WHERE 1 AND datemenopause IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_move_to_human_meno)
            q_delete_meno_at_human = "DELETE FROM human WHERE 1 and datemenopause IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_delete_meno_at_human)
            # print('All meno moved.')
        except ValueError:
            print('Fail to move menopause.')
        stopt = time.time()
        fwaktu_proses = waktu_proses(int(stopt) - int(startt))
        print('MENOPAUSE >> {0} females' . format(g, fwaktu_proses))


def SetDied(sesscode):
    startt = time.time()
    db = Database()
    numhuman = LastID()
    addage = 0
    if numhuman < 100000:
        addage = 100
    elif 100000 <= numhuman < 200000:
        addage = 50
    elif 200000 <= numhuman < 300000:
        addage = 20
    daterequest = DateRequest('agedied')
    simulation_limit_dies = GetConfig('simulation_limit_dies')

    # tbl human
    human_nodied = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND dateborn<='{0}' AND in_use='' ORDER BY dateborn ASC LIMIT 0,{1}" . format(daterequest, simulation_limit_dies))
    g = 0
    if human_nodied:
        for pre in human_nodied:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dateborn']), date_format)
            age = age.days / 365
            agediedx = GetConfig('agedied')
            agediedx1 = int(agediedx.strip().split(',')[0])
            agediedx2 = int(agediedx.strip().split(',')[1])
            random_died = random.randint(agediedx1, agediedx2) + addage
            if random_died <= age:
                g += 1
                db.insert("UPDATE human SET datedied='{0}', in_use='{1}' WHERE 1 AND id={2}" . format(currdatetime, sesscode, pre['id']))

    # tbl human_meno
    human_nodied = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human_meno WHERE 1 AND datedied IS NULL AND in_use='' ORDER BY dateborn ASC LIMIT 0,{1}" . format(daterequest, simulation_limit_dies))
    # g = 0
    if human_nodied:
        for pre in human_nodied:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dateborn']), date_format)
            age = age.days / 365
            agediedx = GetConfig('agedied')
            agediedx1 = int(agediedx.strip().split(',')[0])
            agediedx2 = int(agediedx.strip().split(',')[1])
            random_died = random.randint(agediedx1, agediedx2) + addage
            if random_died <= age:
                g += 1
                db.insert("UPDATE human_meno SET datedied='{0}', in_use='{1}' WHERE 1 AND id={2}" . format(currdatetime, sesscode, pre['id']))

    if g > 0:
        try:

            q_move_to_human_died = "REPLACE INTO human_died SELECT * FROM human WHERE 1 AND datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_move_to_human_died)

            q_move_to_human_died = "REPLACE INTO human_died SELECT * FROM human_meno WHERE 1 AND datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_move_to_human_died)

            q_delete_died_at_human = "DELETE FROM human WHERE 1 and datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_delete_died_at_human)

            q_delete_died_at_human_meno = "DELETE FROM human_meno WHERE 1 and datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_delete_died_at_human_meno)

            # print('All died moved.')
        except ValueError:
            print('Fail to move died.')

        stopt = time.time()
        fwaktu_proses = waktu_proses(int(stopt) - int(startt))
        print('DIED >> {0} humans in {1}' . format(g, fwaktu_proses))


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
    db = Database()
    return db.getone2("SELECT id FROM human WHERE 1 ORDER BY id DESC LIMIT 1")


# db-text


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


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    print(lines[line_num])
    try:
        out = open(file_name, 'w')
        try:
            out.writelines(lines)
            print('Write to db done...')
        except IndexError:
            print('ERROR Write to db...')
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
    f = open(filedb, "r")
    contents = f.readlines()
    f.close()
    contents.insert(insert_to_line, text + '\n')
    f = open(filedb, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


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


def stats(var):
    openstat = open('stat.cnf', 'r')
    stat = openstat.read()
    print(stat)
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
