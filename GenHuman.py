from Database import Database
from Functions import genword, genname, gendesc, GetConfig, GetLive, SetLive
from time import gmtime, strftime
import sys
import random
import datetime


def GenHuman(limit=100, parent=''):
    if __name__ == "__main__":

        db = Database()
        currlive = GetLive()
        currdatetime = strftime("%Y-%m-%d %H:%M:%S", currlive)

        numhuman = db.getone("SELECT COUNT(id) FROM human WHERE 1")
        if numhuman >= 2:

            # generate Human
            g = 0
            for w in range(random.randint(10, limit)):
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

                email  = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                check_email = db.insert("SELECT COUNT(*) FROM human WHERE 1 AND email='{0}'" . format(email))
                if check_email is None:
                    query = "INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='" + sex + ", 'email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '" + parent + "', idCouple = ''"
                    db.insert(query)
                    print('{0} Human created : {1} {2}' . format(g, name_1, name_2))

        else:
            name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
            name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
            email  = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
            db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='M', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" + currdatetime + "', idParent = '', idCouple = 2")
            print('First Human created : {1} {2}' . format(name_1, name_2))

            name_1 = genname(minwords=1, maxwords=1, minchars=3, maxchars=5)
            name_2 = genname(minwords=1, maxwords=2, minchars=3, maxchars=5)
            email  = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
            db.insert("INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='F', email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '"+ currdatetime +"', idParent = '', idCouple = 1")
            print('Second Human created : {1} {2}' . format(name_1, name_2))


def GetNoCouple(sexrequest):
    if sexrequest is 'M':
        sexneed = 'F'
    elif sexrequest is 'F':
        sexneed = 'M'
    res = db.getone("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND datedied='' AND sex='" + sexneed + "' AND idCouple='' ORDER BY RAND() LIMIT 100")
    if res is not None:
        getlive = GetLive()
        currdatetime = strftime("%Y-%m-%d %H:%M:%S", getlive)
        dateborn = res['dateborn']
        age = db.getone("SELECT TIMEDIFF('" + currdatetime + " ','" + dateborn + "')")
        agecoupledx = GetConfig('agecoupled')
        agecoupledx1 = agecoupledx.strip().split(',')[0]
        agecoupledx2 = agecoupledx.strip().split(',')[1]
        if age >= agecoupledx1 or age <= agecoupledx2:
            return res


def SetCouple():
    human_nocouple = db.getall("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND datedied='' AND idCouple='' ORDER BY RAND() LIMIT 100")
    if human_nocouple:
        for co in human_nocouple:
            getlive = GetLive()
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", getlive)
            age = db.getone("SELECT DATEDIFF('" + currdatetime + " ','" + co['dateborn'] + "')")
            agecoupledx = GetConfig('agecoupled')
            agecoupledx1 = agecoupledx.strip().split(',')[0]
            agecoupledx2 = agecoupledx.strip().split(',')[1]
            if age >= agecoupledx1 or age <= agecoupledx2:
                choose_couple = GetNoCouple(sexneed=co['sex'])
                if choose_couple is not None:
                    db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(choose_couple['id'], currdatetime, co['id']))
                    db.insert("UPDATE human SET idCouple={0}, datecoupled='{1}' WHERE 1 AND id={2}" . format(co['id'], currdatetime, choose_couple['id']))


def SetPregnant():
    human_nopregnant = db.getall("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND sex='F', datedied='' AND datepregnant='' AND idCouple>0 ORDER BY RAND() LIMIT 100")
    if human_nopregnant:
        for pre in human_nopregnant:
            getlive = GetLive()
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", getlive)
            days_after_coupled = db.getone("SELECT DATEDIFF('" + currdatetime + " ','" + res['datecoupled'] + "')")
            pregnantx = GetConfig('pregnant')
            pregnantx1 = pregnantx.strip().split(',')[0]
            pregnantx2 = pregnantx.strip().split(',')[1]
            if days_after_coupled >= pregnantx1 or days_after_coupled <= pregnantx2:
                db.insert("UPDATE human SET datepregnant='{0}' WHERE 1 AND id={1}" . format(currdatetime, pre['id']))


def SetGivingBirth():
    human_givingbirth = db.getall("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND sex='F', datedied='' AND datepregnant!='' AND idCouple>0 ORDER BY RAND() LIMIT 100" . format(currdatetime, pregnantx1, pregnantx2))
    if human_givingbirth:
        for pre in human_givingbirth:
            getlive = GetLive()
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", getlive)
            days_after_pregnant = db.getone("SELECT DATEDIFF('" + currdatetime + " ','" + res['datecoupled'] + "')")
            givingbirthx = GetConfig('pregnant')
            givingbirthx1 = givingbirthx.strip().split(',')[0]
            givingbirthx2 = givingbirthx.strip().split(',')[1]
            if days_after_pregnant >= givingbirthx1 or days_after_coupled <= givingbirthx2:
                parent_male = db.getone("SELECT id FROM human WHERE 1 AND id={0}" . format(pre['idCouple']))
                parent_female = db.getone("SELECT id FROM human WHERE 1 AND id={0}" . format(pre['id']))
                parent = parent_male + '|' + parent_female
                GenHuman(random.randint(1, 2), parent)


try:
    while True:
        SetLive()
        getlive = GetLive()
        print(getlive)
except KeyboardInterrupt:
    pass # do cleanup here
