from Database import Database
from Functions import genword, genname, gendesc, GetConfig
from time import gmtime, strftime
import sys
import random


def GenHuman(limit=100, currlive=0):
    if __name__ == "__main__":

        db = Database()
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

                parent_male = db.getone("SELECT COUNT(id) FROM human WHERE 1 AND sex='M' ORDER BY RAND()")
                parent_female = db.getone("SELECT COUNT(id) FROM human WHERE 1 AND sex='F' ORDER BY RAND()")
                parent = parent_male + '|' + parent_female

                agemenopause = ''
                if sex='F':
                    agemenopause = random.randint(55, 60)

                email  = '{0}@{1}.com' . format(name_1, genword(minchars=5, maxchars=10, istitle=0))
                check_email = db.insert("SELECT COUNT(*) FROM human WHERE 1 AND email='{0}'" . format(email))
                if check_email is None:
                    query = "INSERT INTO human SET firstname = '" + str(name_1) + "', lastname = '" + str(name_2) + "', sex='" + sex + ", 'email = '" + str(email) + "', dateadd='" + currdatetime + "', dateborn = '" +  + "', idParent = '" + parent + "', idCouple = ''"
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


def SetCouple():
    human_nocouple = db.getall("SELECT id, firstname, sex, dateborn FROM human WHERE 1 AND idCouple='' ORDER BY RAND() LIMIT 100")
    if human_nocouple:
        for co in human_nocouple:
            getlive = GetLive()
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", getlive)
            




try:
    while True:
        getlive = GetLive()
        GenHuman(limit=50, currlive=getlive)
except KeyboardInterrupt:
    pass # do cleanup here
