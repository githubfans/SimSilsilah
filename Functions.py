from Database import Database
import random
import re
import os
import time
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
    cari_koma = re.search(',', getx2)
    cari_kali = re.search('x', getx2)
    cari_bagi = re.search('/', getx2)
    if cari_koma is not None:

        getx2_1 = getx2.strip().split(',')[0]
        getx2_2 = getx2.strip().split(',')[1]

        cari_kali_1 = re.search('x', getx2_1)
        cari_kali_2 = re.search('x', getx2_2)

        if cari_kali_1 is not None:
            getx2_x1 = int(getx2_1.strip().split('x')[0]) * int(getx2_1.strip().split('x')[1])
        else:
            getx2_x1 = getx2_1

        if cari_kali_2 is not None:
            getx2_x2 = int(getx2_2.strip().split('x')[0]) * int(getx2_2.strip().split('x')[1])
        else:
            getx2_x2 = getx2_2

        if getx2_x1 >= 0 and getx2_x2 >= 0:
            getx2 = '{0},{1}' . format(getx2_x1, getx2_x2)

        return getx2

    elif cari_kali is not None:
        hasil_kali = int(getx2.strip().split('x')[0]) * int(getx2.strip().split('x')[1])
        return hasil_kali
    elif cari_bagi is not None:
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

    numhuman = LastID()
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


def GenHuman(limit=100, parent=''):
    # if __name__ == "__main__":

    db = Database()

    numhuman = NumHumanLife()

    # print('limit:{0} | parent:{1}' . format(limit, parent))

    if len(parent) > 1:

        # generate Human
        g = 0
        if limit > 1:
            query_head = "INSERT INTO human (firstname, lastname, sex, email, dateadd, dateborn, idParent, idCouple) VALUES "
            queryes = []
            for w in range(random.randint(limit, limit)):
                currdatetime = GetLive()
                if currdatetime is not None:
                    # Data Insert into the table
                    g += 1
                    name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
                    name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
                    # daddy_id = parent.strip().split('|')[0]
                    # daddy_row = db.getone("SELECT firstname, lastname FROM human WHERE 1 AND id={0}" . format(daddy_id))
                    # daddy_lastname = daddy_row['lastname']
                    # count_bin = daddy_lastname.count("bin")
                    # if count_bin >= 3:
                    #     n = 0
                    #     group = []
                    #     for c in daddy_lastname.strip().split('bin'):
                    #         n += 1
                    #         if 2 <= n <= 3:
                    #             group.append(c)
                    #     daddy_row['lastname'] = ' ' . join(group)
                    # name_2 = '{0} {1}' . format(daddy_row['firstname'], daddy_row['lastname'])
                    sexx = random.randint(0, 1)
                    if sexx is 0:
                        sex = 'M'
                        # infixname = 'bin'
                    else:
                        sex = 'F'
                        # infixname = 'binti'
                    # name_2 = '{0} {1}' . format(infixname, name_2)
                    email_suffix = re.sub('[^0-9a-zA-Z]+', '', currdatetime)
                    email = '{0}.{1}@{2}.com' . format(name_1, email_suffix, genword(minchars=5, maxchars=10, istitle=0))
                    email = email.lower()
                    # query = "INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='" + sex[:1] + "', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                    query_v = "('" + str(name_1) + "', '" + str(name_2) + "', '" + sex[:1] + "', '" + str(email) + "', '" + currdatetime + "', '" + currdatetime + "', '" + parent + "', '')"
                    queryes.append(query_v)
                    # try:
                    #     db.insert(query)
                    #     print('{0} Human created : {1} {2}' . format(g, name_1, name_2))
                    # except ValueError:
                    #     print(query)
                    #     print('{0} Human creating FAILED : {1} {2}' . format(g, name_1, name_2))
            queryx = ',' . join(queryes)
            query = '{0}{1}' . format(query_head, queryx)
            if len(queryx) > 10:
                db.insert(query)
                # print('{0} Human created' . format(g))
            # else:
                # print('{0} Human FAIL created' . format(g))
        else:
            currdatetime = GetLive()
            if currdatetime is not None:
                # Data Insert into the table
                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
                # daddy_id = parent.strip().split('|')[0]
                # daddy_row = db.getone("SELECT firstname, lastname FROM human WHERE 1 AND id={0}" . format(daddy_id))
                # name_2 = '{0} {1}' . format(daddy_row['firstname'], daddy_row['lastname'])
                sexx = random.randint(0, 1)
                if sexx is 0:
                    sex = 'M'
                    # infixname = 'bin'
                else:
                    sex = 'F'
                    # infixname = 'binti'
                # name_2 = '{0} {1}' . format(infixname, name_2)
                email_suffix = re.sub('[^0-9a-zA-Z]+', '', currdatetime)
                email = '{0}.{1}@{2}.com' . format(name_1, email_suffix, genword(minchars=5, maxchars=5, istitle=0))
                query = "INSERT INTO human SET firstname = '" + name_1 + "', lastname = '" + name_2 + "', sex='" + sex[:1] + "', email = '" + email + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                try:
                    db.insert(query)
                    # print('1 Human created : {0} {1}' . format(name_1, name_2))
                except ValueError:
                    print(query)
                    # print('1 Human creating FAILED : {0} {1}' . format(name_1, name_2))

    else:
        currdatetime = GetLive()
        if currdatetime is not None:
            if numhuman < 2:
                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
                email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='M', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '', idCouple = ''")
                print('First Human created : {0} {1}' . format(name_1, name_2))

                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=10)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=10)
                email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='F', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '', idCouple = ''")
                print('Second Human created : {0} {1}' . format(name_1, name_2))
            elif numhuman is 2:
                print('masih adam hawa di bumi ini.')

            # if numhuman >= 80000:
            #     sys.exit()


def GetNoCouple(sexrequest):
    db = Database()
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    daterequest = DateRequest('agecoupled')
    res = db.getone("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND sex='{0}' AND idCouple='' AND dateborn<='{1}' ORDER BY dateborn ASC LIMIT 0,100" . format(sexneed, daterequest))
    if res is not None:
        currdatetime = GetLive()
        age = db.getone("SELECT DATEDIFF('{0}', '{1}')" . format(currdatetime, res['dateborn']))
        agecoupledx = GetConfig('agecoupled')
        agecoupledx1 = int(agecoupledx.strip().split(',')[0])
        agecoupledx2 = int(agecoupledx.strip().split(',')[1])
        random_age = random.randint(agecoupledx1, agecoupledx2)
        if random_age < age:
            return res


def SetCouple():
    startt = time.time()
    db = Database()
    daterequest = DateRequest('agecoupled')
    simulation_limit_couple = GetConfig('simulation_limit_couple')
    q_nocouple = "SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND idCouple='' AND dateborn<='{0}' ORDER BY dateborn ASC LIMIT 0,{1}" . format(daterequest, simulation_limit_couple)
    human_nocouple = db.getall(q_nocouple)
    # print(q_nocouplse)
    # sys.exit()
    g = 0
    if human_nocouple:
        for co in human_nocouple:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            if currdatetime is not None and co['dateborn'] is not None:
                age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(co['dateborn']), date_format)
                age = age.days / 365
                if age > 0:
                    agecoupledx = GetConfig('agecoupled')
                    agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                    agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                    random_ = random.randint(agecoupledx1, agecoupledx2)
                    if random_ <= age:
                        choose_couple = GetNoCouple(sexrequest=co['sex'])
                        if choose_couple is not None:
                            g += 1
                            db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(choose_couple['id'], currdatetime, co['id']))
                            db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(co['id'], currdatetime, choose_couple['id']))
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        print('**COUPLED** >> {0} couples in {1}' . format(g, fwaktu_proses))


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

                    if 100000 <= numhuman < 200000:
                        numgenerate = random.randint(1, random.randint(1, random.randint(1, random.randint(1, 5))))
                    elif 1000 <= numhuman < 100000:
                        numgenerate = random.randint(1, 5)
                    elif 0 < numhuman < 1000:
                        numgenerate = random.randint(2, 10)

                    addbaby += numgenerate
                    # print(addbaby)
                    # print('GIVING BIRTH >> {0} {1} : {2} baby(s)' . format(pre['firstname'], pre['lastname'], numgenerate))
                    GenHuman(numgenerate, parent)
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
        print('Giving Birth >> {0} babies in {1}' . format(addbaby, fwaktu_proses))


def SetMenopause():
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
                db.insert("UPDATE human SET datemenopause='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
    stopt = time.time()
    fwaktu_proses = waktu_proses(int(stopt) - int(startt))
    if g > 0:
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
    if g > 0:
        try:
            q_move_to_human_died = "REPLACE INTO human_died SELECT * FROM human WHERE 1 AND datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_move_to_human_died)
            q_delete_died_at_human = "DELETE FROM human WHERE 1 and datedied IS NOT NULL AND in_use='{0}'" . format(sesscode)
            db.insert(q_delete_died_at_human)
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
