from Database import Database
from Functions import genword, genname, GetConfig, GetLive, DateRequest
# from time import gmtime, strftime
import sys
import random
import time
import re
from datetime import datetime, timedelta


def test():
    print(genname(minwords=2, maxwords=3, minchars=3, maxchars=5, istitle=1))


def GenHuman(limit=100, parent=''):
    if __name__ == "__main__":

        db = Database()

        numhuman = NumHuman()
        # print('numhuman = {0}' . format(numhuman))

        if len(parent) > 1:

            # generate Human
            g = 0
            if limit > 1:
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
                    query = "INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='" + sex[:1] + "', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                    try:
                        db.insert(query)
                        print('{0} Human created : {1} {2}' . format(g, name_1, name_2))
                    except ValueError:
                        print(query)
                        print('{0} Human creating FAILED : {1} {2}' . format(g, name_1, name_2))
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
                    print('1 Human created : {0} {1}' . format(name_1, name_2))
                except ValueError:
                    print(query)
                    print('1 Human creating FAILED : {0} {1}' . format(name_1, name_2))

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
    res = db.getone("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND sex='{0}' AND idCouple='' AND dateborn<='{1}' ORDER BY RAND() LIMIT 0,10" . format(sexneed, daterequest))
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
    q_nocouple = "SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND idCouple='' AND dateborn<='{0}' ORDER BY RAND() LIMIT 0,100" . format(daterequest)
    human_nocouple = db.getall(q_nocouple)
    # print(q_nocouplse)
    # sys.exit()
    if human_nocouple:
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
                        db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(choose_couple['id'], currdatetime, co['id']))
                        db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(co['id'], currdatetime, choose_couple['id']))
                        print('{0} & {1} **COUPLED**' . format(co['firstname'], choose_couple['firstname']))


def SetPregnant():
    db = Database()
    human_nopregnant = db.getall("SELECT id, firstname, lastname, sex, dateborn, datecoupled FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND datemenopause IS NULL AND idCouple>0 ORDER BY RAND() LIMIT 0,100")
    if human_nopregnant:
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
                db.insert("UPDATE human SET datepregnant='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
                print('PREGNANT >> {0} {1}' . format(pre['firstname'], pre['lastname']))


def SetGivingBirth():
    db = Database()
    human_givingbirth = db.getall("SELECT id, firstname, lastname, sex, idCouple, dateborn, datepregnant FROM human WHERE 1 AND sex='F' AND datedied IS NULL AND datepregnant IS NOT NULL AND idCouple>0 ORDER BY RAND() LIMIT 0,100")
    if human_givingbirth:
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
                parent = '{0}|{1}' . format(pre['idCouple'], pre['id'])
                db.insert("UPDATE human SET datepregnant=NULL WHERE 1 AND id={0}" . format(pre['id']))
                numhuman = NumHuman()
                numgenerate = random.randint(1, random.randint(1, 5))
                if numhuman < 100:
                    numgenerate = 50
                elif 100 <= numhuman <= 1000:
                    numgenerate = random.randint(random.randint(3, 6), 6)
                print('GIVING BIRTH >> {0} {1} : {2} baby(s)' . format(pre['firstname'], pre['lastname'], numgenerate))
                GenHuman(numgenerate, parent)


def SetMenopause():
    db = Database()
    daterequest = DateRequest('agemenopause')
    human_nomenopause = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND datemenopause IS NULL AND dateborn<='{0}' ORDER BY dateborn LIMIT 0,10" . format(daterequest))
    if human_nomenopause:
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
                db.insert("UPDATE human SET datemenopause='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
                print('MENOPAUSE >> {0} {1}' . format(pre['firstname'], pre['lastname']))


def SetDied():
    db = Database()
    daterequest = DateRequest('agedied')
    human_nodied = db.getall("SELECT id, firstname, lastname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND dateborn<='{0}' ORDER BY dateborn ASC LIMIT 10" . format(daterequest))
    if human_nodied:
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
                db.insert("UPDATE human SET datedied='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
                print('DIED >> {0} {1}' . format(pre['firstname'], pre['lastname']))
                # time.sleep(1)


def NumHuman():
    db = Database()
    return db.count("SELECT id FROM human WHERE 1")


try:
    while True:
        maxnumhuman = GetConfig('simulation_maxnumhuman')
        numhuman = NumHuman()
        if numhuman <= maxnumhuman:
            getlive = GetLive()
            # print(getlive)
            # test()
            print('\n-------- GenHuman --------------')
            GenHuman(1)
            print('\n-------- SetCouple -------------')
            SetCouple()
            print('\n-------- SetPregnant -----------')
            SetPregnant()
            print('\n-------- SetGivingBirth --------')
            SetGivingBirth()
            print('\n-------- SetMenopause ----------')
            SetMenopause()
            print('\n-------- SetDied ---------------')
            SetDied()
        else:
            print('sim off.')
except KeyboardInterrupt:
    pass # do cleanup here
