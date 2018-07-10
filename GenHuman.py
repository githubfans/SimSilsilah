from Database import Database
from Functions import genword, genname, gendesc, GetConfig, GetLive, SetLive
from time import gmtime, strftime
import sys
import random
import time
from datetime import datetime


def test():
    db = Database()
    getone_ = db.getone("SELECT * FROM human WHERE 1 and sex='F'")
    print(getone_)


def GenHuman(limit=100, parent=''):
    if __name__ == "__main__":

        db = Database()
        currdatetime = GetLive()

        numhuman = NumHuman()
        # print('numhuman = {0}' . format(numhuman))

        if numhuman >= 10000:
            sys.exit()

        if len(parent) > 1:

            # generate Human
            g = 0
            if limit > 1:
                for w in range(random.randint(1, limit)):
                    # Data Insert into the table
                    g += 1
                    name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
                    name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
                    sexx = random.randint(0, 1)
                    if sexx is 0:
                        sex = 'M'
                    else:
                        sex = 'F'

                    agemenopause = ''
                    if sex is 'F':
                        agemenopause = random.randint(55, 60)

                    email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                    check_email = db.insert("SELECT COUNT(*) FROM human WHERE 1 AND email='{0}'" . format(email))
                    if check_email is None:
                        # print(parent)
                        query = "INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='" + sex[:1] + "', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                        # print(query)
                        db.insert(query)
                        print('{0} Human created : {1} {2}' . format(g, name_1, name_2))
            else:
                # Data Insert into the table
                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
                sexx = random.randint(0, 1)
                if sexx is 0:
                    sex = 'M'
                else:
                    sex = 'F'
                agemenopause = None
                if sex is 'F':
                    agemenopause = random.randint(55, 60)

                email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                check_email = db.insert("SELECT COUNT(*) FROM human WHERE 1 AND email='{0}'" . format(email))
                if check_email is None:
                    query = "INSERT INTO human SET firstname = '" + name_1 + "', lastname = '" + name_1 + "', sex='" + sex[:1] + "', email = '" + email + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                    db.insert(query)
                    print('1 Human created : {0} {1}' . format(name_1, name_2))

        else:
            if numhuman < 2:
                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
                email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='M', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '', idCouple = ''")
                print('First Human created : {0} {1}' . format(name_1, name_2))

                name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
                name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
                email = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='F', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '"+ currdatetime +"', idParent = '', idCouple = ''")
                print('Second Human created : {0} {1}' . format(name_1, name_2))
            elif numhuman is 2:
                print('masih adam hawa di bumi ini.')


def GetNoCouple(sexrequest):
    db = Database()
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    res = db.getone("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND sex='{0}' AND idCouple='' ORDER BY RAND() LIMIT 1000" . format(sexneed))
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
    human_nocouple = db.getall("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND datedied IS NULL AND idCouple='' ORDER BY RAND() LIMIT 1000")
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
                if agecoupledx1 <= age <= agecoupledx2:
                    choose_couple = GetNoCouple(sexrequest=co['sex'])
                    if choose_couple is not None:
                        db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(choose_couple['id'], currdatetime, co['id']))
                        db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(co['id'], currdatetime, choose_couple['id']))
                        print('{0} & {1} **COUPLED**' . format(co['firstname'], choose_couple['firstname']))


def SetPregnant():
    db = Database()
    human_nopregnant = db.getall("SELECT id, firstname, sex, dateborn, datecoupled FROM human WHERE 1 AND sex='F' AND datedied IS NULL  AND datepregnant IS NULL AND idCouple>0 ORDER BY RAND() LIMIT 1000")
    if human_nopregnant:
        for pre in human_nopregnant:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            days_after_coupled = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datecoupled']), date_format)
            days_after_coupled = days_after_coupled.days
            # print('firstname : {0} | days_after_coupled = {1}' . format(pre['firstname'], days_after_coupled))
            pregnantx = GetConfig('pregnant')
            pregnantx1 = int(pregnantx.strip().split(',')[0])
            pregnantx2 = int(pregnantx.strip().split(',')[1])
            if pregnantx1 <= days_after_coupled <= pregnantx2:
                db.insert("UPDATE human SET datepregnant='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))
                print('firstname : {0} | PREGNANT' . format(pre['firstname']))


def SetGivingBirth():
    db = Database()
    human_givingbirth = db.getall("SELECT id, firstname, sex, idCouple, dateborn, datepregnant FROM human WHERE 1 AND sex='F' AND datedied IS NULL AND datepregnant!='' AND idCouple>0 ORDER BY RAND() LIMIT 100")
    if human_givingbirth:
        for pre in human_givingbirth:
            currdatetime = GetLive()
            date_format = "%Y-%m-%d %H:%M:%S"
            days_after_pregnant = datetime.strptime(str(currdatetime), date_format) - datetime.strptime(str(pre['datepregnant']), date_format)
            days_after_pregnant = days_after_pregnant.days
            givingbirthx = GetConfig('givingbirth')
            givingbirthx1 = int(givingbirthx.strip().split(',')[0])
            givingbirthx2 = int(givingbirthx.strip().split(',')[1])
            if givingbirthx1 <= days_after_pregnant <= givingbirthx2:
                parent = '{0}|{1}' . format(pre['idCouple'], pre['id'])
                db.insert("UPDATE human SET datepregnant=NULL WHERE 1 AND id={0}" . format(pre['id']))
                numhuman = NumHuman()
                numgenerate = random.randint(1, 4)
                if numhuman < 10:
                    numgenerate = 10
                elif 10 <= numhuman <= 100:
                    numgenerate = random.randint(3, 6)
                print('firstname : {0} | GIVING BIRTH {1} baby(s)' . format(pre['firstname'], numgenerate))
                GenHuman(numgenerate, parent)


def NumHuman():
    db = Database()
    return db.count("SELECT id FROM human WHERE 1")


try:
    while True:
        # islive = GetConfig('liveison')
        islive = 1
        if islive is 1:
            getlive = GetLive()
            # print(getlive)
            # test()
            GenHuman(1)
            SetCouple()
            SetPregnant()
            SetGivingBirth()
            SetLive()
        # else:
        #     print('sim off.')
except KeyboardInterrupt:
    pass # do cleanup here
