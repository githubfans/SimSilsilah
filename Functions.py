from Database import Database
import random
import re
import os
import time
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
    f = open("config.cnf", "r")
    config = f.read()
    f.close()
    getx = config.strip().split('\n{0}=' . format(str))[1]
    getx2 = getx.strip().split(';')[0]
    # print('getx2 = {0}' . format(getx2))
    cari_koma = re.search(',', getx2)
    cari_kali = re.search('x', getx2)
    cari_bagi = re.search('/', getx2)
    if cari_koma is not None:
        return getx2
    if cari_kali is not None:
        hasil_kali = int(getx2.strip().split('x')[0]) * int(getx2.strip().split('x')[1])
        return hasil_kali
    if cari_bagi is not None:
        hasil_bagi = int(getx2.strip().split('/')[0]) * int(getx2.strip().split('/')[1])
        return hasil_bagi
    else:
        return int(getx2)


def GetLive():
    # print(C['live'])
    f = open("live.cnf", "r")
    live = f.read()
    if len(live) < 1:
        live = '1000-01-01 00:00:00'
    f.close()
    # C['live'] = live
    return live


def SetLive():
    getLive = GetLive()
    # getLive = str(getLive['live'])
    # getLive = getLive.strip().split('live="')[1]
    # getLive = getLive.strip().split('"')[0]
    # print(getLive['live'])

    newlive = datetime.strptime(getLive, "%Y-%m-%d %H:%M:%S")
    min_r = GetConfig('simulation_mintimeadd')
    max_r = GetConfig('simulation_maxtimeadd')
    newlive = newlive + timedelta(seconds=random.randint(min_r, max_r))
    newlive = newlive + timedelta(seconds=random.randint(1, 3600))
    f = open("live.cnf", "w+")
    f.write(str(newlive))
    f.close()


def DateRequest(StrConfig, by='seconds'):
    getLive = GetLive()
    timelive = datetime.strptime(getLive, "%Y-%m-%d %H:%M:%S")
    valCOnfig = GetConfig(StrConfig)
    valCOnfig = int(valCOnfig.strip().split(',')[0])
    if by is 'seconds':
        return timelive - timedelta(seconds=valCOnfig * 3600 * 24 * 365)
    if by is 'days':
        return timelive - timedelta(days=valCOnfig)


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
    db = Database()
    daterequest = DateRequest('agecoupled')
    simulation_limit_couple = GetConfig('simulation_limit_couple')
    q_nocouple = "SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND idCouple='' AND dateborn<='{0}' ORDER BY RAND() LIMIT 0,{1}" . format(daterequest, simulation_limit_couple)
    human_nocouple = db.getall(q_nocouple)
    # print(q_nocouplse)
    # sys.exit()
    if human_nocouple:
        g = 0
        for co in human_nocouple:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
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
        if g > 0:
            print('**COUPLED** >> {0} couples' . format(g))


def SetPregnant():
    db = Database()
    human_nopregnant = db.getall("SELECT id, firstname, lastname, sex, dateborn, datecoupled FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND datemenopause IS NULL AND idCouple>0 ORDER BY RAND() LIMIT 0,100")
    if human_nopregnant:
        g = 0
        for pre in human_nopregnant:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            days_after_coupled = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datecoupled']), date_format)
            days_after_coupled = days_after_coupled.days
            pregnantx = GetConfig('pregnant')
            pregnantx1 = int(pregnantx.strip().split(',')[0])
            pregnantx2 = int(pregnantx.strip().split(',')[1])
            random_ = random.randint(pregnantx1, pregnantx2)
            if random_ <= days_after_coupled:
                g += 1
                db.insert("UPDATE human SET datepregnant='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
        if g > 0:
            print('PREGNANT >> {0} females' . format(g))


def SetGivingBirth():
    db = Database()
    simulation_limit_givingbirth = GetConfig('simulation_limit_givingbirth')
    human_givingbirth = db.getall("SELECT id, firstname, lastname, sex, idCouple, dateborn, datepregnant FROM human WHERE 1 AND sex='F' AND datedied IS NULL AND datepregnant IS NOT NULL AND idCouple>0 ORDER BY RAND() LIMIT 0,{0}" . format(simulation_limit_givingbirth))
    if human_givingbirth:
        g = 0
        addbaby = 0
        for pre in human_givingbirth:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            days_after_pregnant = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datepregnant']), date_format)
            days_after_pregnant = days_after_pregnant.days
            givingbirthx = GetConfig('givingbirth')
            givingbirthx1 = int(givingbirthx.strip().split(',')[0])
            givingbirthx2 = int(givingbirthx.strip().split(',')[1])
            random_ = random.randint(givingbirthx1, givingbirthx2)
            if random_ <= days_after_pregnant:
                g += 1
                parent = '{0}|{1}' . format(pre['idCouple'], pre['id'])
                db.insert("UPDATE human SET datepregnant=NULL WHERE 1 AND id={0}" . format(pre['id']))
                numgenerate = random.randint(1, random.randint(1, random.randint(1, random.randint(1, 5))))
                addbaby += numgenerate
                # print('GIVING BIRTH >> {0} {1} : {2} baby(s)' . format(pre['firstname'], pre['lastname'], numgenerate))
                GenHuman(numgenerate, parent)
        if addbaby > 0:
            print('Giving Birth >> {0} babies' . format(addbaby))


def SetMenopause():
    db = Database()
    daterequest = DateRequest('agemenopause')
    human_nomenopause = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND datemenopause IS NULL AND dateborn<='{0}' ORDER BY dateborn LIMIT 0,100" . format(daterequest))
    if human_nomenopause:
        g = 0
        for pre in human_nomenopause:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dateborn']), date_format)
            age = age.days / 365
            # print('days_after_coupled >> {0} {1} = {1}' . format(pre['firstname'], days_after_coupled))
            agemenopausex = GetConfig('agemenopause')
            agemenopausex1 = int(agemenopausex.strip().split(',')[0])
            agemenopausex2 = int(agemenopausex.strip().split(',')[1])
            random_menopause = random.randint(agemenopausex1, agemenopausex2)
            if random_menopause <= age:
                g += 1
                db.insert("UPDATE human SET datemenopause='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
        if g > 0:
            print('MENOPAUSE >> {0} females' . format(g))


def SetDied():
    db = Database()
    daterequest = DateRequest('agedied')
    simulation_limit_dies = GetConfig('simulation_limit_dies')
    human_nodied = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND dateborn<='{0}' ORDER BY dateborn ASC LIMIT 0,{1}" . format(daterequest, simulation_limit_dies))
    if human_nodied:
        g = 0
        for pre in human_nodied:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            age = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['dateborn']), date_format)
            age = age.days / 365
            agediedx = GetConfig('agedied')
            agediedx1 = int(agediedx.strip().split(',')[0])
            agediedx2 = int(agediedx.strip().split(',')[1])
            random_died = random.randint(agediedx1, agediedx2)
            if random_died <= age:
                g += 1
                db.insert("UPDATE human SET datedied='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
        if g > 0:
            print('DIED >> {0} humans' . format(g))
            try:
                q_move_to_human_died = "REPLACE INTO human_died SELECT * FROM human WHERE 1 AND datedied IS NOT NULL"
                db.insert(q_move_to_human_died)
                q_delete_died_at_human = "DELETE FROM human WHERE 1 and datedied IS NOT NULL"
                db.insert(q_delete_died_at_human)
                print('All died moved.')
            except ValueError:
                print('Fail to move died.')


def NumHumanLife():
    db = Database()
    return db.count("SELECT id FROM human WHERE 1")


def NumHuman2():
    db = Database()
    return db.getone2("SELECT id FROM human WHERE 1 ORDER BY id DESC LIMIT 1")
