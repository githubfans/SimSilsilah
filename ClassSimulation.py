from defcoll import *
import random
import time
import hashlib
import json


class GenerateRandomText:

    def __init__(self, numWord, numCharPerWord, typetext='name', sex='M'):
        self.numWord = numWord
        self.numCharPerWord = numCharPerWord
        self.typetext = typetext
        self.sex = sex
        self.vocal = ['a', 'e', 'i', 'o', 'u']
        self.conso = ['w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'b', 'n', 'm']
        group = []
        for i in range(self.numWord):
            ditem = self.genword()
            group.append(ditem)
        self.genword_ = self.firstname() + ' ' + " ".join(group)

    def genword(self):
        group = []
        minChar = 5
        if self.numCharPerWord <= minChar + 3:
            self.numCharPerWord = minChar + 3
        numchar = random.randint(minChar, self.numCharPerWord)
        what_first = random.randint(0, 1)
        for i in range(0, numchar):
            rnd = i % 2
            if rnd is what_first:
                gen = self.vocal[random.randint(0, len(self.vocal) - 1)]
            else:
                gen = self.conso[random.randint(0, len(self.conso) - 1)]
            group.append(gen)
        group_string = "".join(group)
        return_ = group_string[:numchar]
        return return_

    def genText(self):
        group = []
        for i in range(self.numWord):
            ditem = self.genword()
            group.append(ditem)
        return_ = " ".join(group)

        return return_

    def _name(self):
        return_ = self.genword_
        return_ = return_.title()
        return return_

    def _email(self):
        return_ = self._name()
        return_ = return_.replace(' ', '.')
        return_ += '.' + str(time.time()).replace('.', '')
        return_ += "@gmail.com"
        return return_

    def _desc(self):
        group = []
        for i in range(2, 20):
            self.numWord = random.randint(4, 10)
            return_sentences = self.genText() + '. '
            group.append(return_sentences)
        return_ = " ".join(group)
        return return_

    def firstname(self):
        first = ''
        if self.sex == 'M':
            first = 'abi aceng afif agus agustinus akum amat ambo asep bangun basir beben beni benji budi bobi boby cecep dadang daeng didik didit diran dodi doni dudung eko fajar febri gugun gusur harun herman hermawan hidayat igun jawir joko jono kaisar kemis kenu maman mamat marno maryanto memet ojak oktavianus puang rahmat riko rio rohmat rojak roma roy slamet suciman sudiran sujiman sukiman sukir sukiran sukirman sumarno sumaryanto suyono tatang teguh tris tukimin ucok ujang untung vicky viki viky wasiyat wawan widodo yanto yatno yono'

        elif self.sex == 'F':
            first = 'adel adelia aulia aliyah ayu bening budiani caca cahaya cici cucu dayu denok devi devy dewi dika dini ekowati erna erni etik ethy fitriani fransiska hayu hermin hermina hidayati jenny jessica jessy komariah lucy lusi lusiana lusy maria mariana marni maryam maryati michelle mimi mimin mina minah mini mumun nani nina nini ninik nunik nur nurul pilia radias rahayu rani retno rianti rika rina rindi rini rumi rumini siska sofia sophia suci suciani suciati sumarni tami tanti tanty tini umi utami wati widy widya wini winni wiwin yanti yuli yuliana yulianti'
        out = first.strip().split(' ')
        len_out = len(out)
        randoms = random.randint(0, (len_out - 1))
        return out[randoms].title()


# s = GenerateRandomText(random.randint(1, 3), 10, 'name', 'F')
# print(s._name())
# name_1 = s._name().strip().split(' ')[0]
# name_2 = s._name().replace(name_1, '')
# print('name_1 = ', name_1)
# print('name_2 = ', name_2.strip())

# print(s._email())
# print(s._desc())


class GenerateHumanData:
    def __init__(self, numLoops, parent):
        self.numLoops = numLoops
        self.parent = parent

    def generateJSON(self):
        print('\nGENERATING HUMAN')
        queryes = []
        n = 0
        for loop in range(0, self.numLoops):
            sexx = random.randint(0, 1)
            if sexx is 0:
                sex = 'M'
            else:
                sex = 'F'
            s = GenerateRandomText(random.randint(1, 3), 10, 'name', sex)
            name_1 = s._name().strip().split(' ')[0]
            name_2 = s._name().replace(name_1, '')
            email = s._email()
            source_idhuman = email.encode(encoding='UTF-8', errors='strict')
            m = hashlib.md5()
            m.update(source_idhuman)
            idhuman = m.hexdigest()
            currdatetime = '2019-01-01 00:00:00'        # GetLive()
            dateborn_y = str(random.randint(1000, 2000))
            dateborn_m = str(random.randint(1, 12))
            dateborn_d = str(random.randint(1, 28))
            dateborn = '{0}-{1}-{2} 00:00:00' . format(dateborn_y, dateborn_m.zfill(2), dateborn_d.zfill(2))
            # print('dateborn ==> ', dateborn)
            # exit()
            jsonstr = {
                'id': idhuman,
                'firstname': name_1,
                'lastname': name_2.strip(),
                'sex': sex[:1],
                'email': email.strip(),
                'dateadd': currdatetime,
                'dateborn': dateborn,
                'idParent': str(self.parent),
                'idCouple': '',
            }
            queryes.append(jsonstr)
            n += 1
            print(n, jsonstr['id'], jsonstr['sex'], jsonstr['firstname'])

        return queryes

    def SaveJSON2File(self):
        jsonData = self.generateJSON()
        if len(jsonData) > 0:
            with open('db.single.json', 'a') as afile:
                afile.write(json.dumps(jsonData))
            # time.sleep(5)
            reformat_db(dbname='single')


class GenerateHumanCouple:
    def __init__(self, numLoops):
        self.numLoops = numLoops

    def SetCouple(self):
        print('\nFILTER COUPLE')
        # mengosongkan file dbtemp
        empty_dbtemp(dbname='single')
        self.loads_single = loads_db(dbname='single')
        index_num = 0
        n = 0
        currdatetime = '2019-01-01 00:00:00'        # GetLive()
        for data in self.loads_single:
            readlist = load_dbtemp(dbname='single')
            if data['id'] not in readlist:
                age = get_age(currdatetime, data['dateborn'])
                agecoupledx = GetConfig('agecoupled')
                agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                # agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                couple = []
                if agecoupledx1 <= int(age):
                    self.except_id = data['id']
                    if data['sex'] == 'M':
                        self.sexneed = 'F'
                    else:
                        self.sexneed = 'M'
                    couple = self.GetNoCouple()
                    try:
                        if len(couple['id']) == 32 and len(data['id']) == 32:
                            n += 1
                            print('\n', n, couple['data']['id'], couple['data']['sex'], ' >< ', data['sex'], data['id'])
                            self.loads_single[index_num]['idCouple'] = couple['id']
                            self.loads_single[couple['index_num']]['idCouple'] = data['id']
                            save_dbtemp(dbname='single', content=data['id'] + ' ' + couple['id'])
                    except Exception:
                        pass
            index_num += 1
            if n >= self.numLoops:
                break
        print('\n\n---------len before delete = ', len(self.loads_single))
        print('\n\n---------pick coupled--------')
        list_db = self.loads_single    # loads_db(dbname='single')
        coupled = []
        readtemplist = load_dbtemp(dbname='single')
        print('readtemplist = ', len(readtemplist))
        index_ = 0
        hit = 0
        for data_coupled in list_db:
            if data_coupled['id'] in readtemplist:
                coupled.append(data_coupled)
                list_db[index_] = '[removed]'
                hit += 1
            index_ += 1
        print('index_ append = ', index_)
        print('hit append = ', hit)
        print('\n\n-----------len after coupled = ', len(self.loads_single))
        return {'list_coupled': coupled, 'list_single': self.loads_single}

    def GetNoCouple(self):
        loads_single = self.loads_single
        returns = ''
        index_num = 0
        for data_nocouple in loads_single:
            readlist = load_dbtemp(dbname='single')
            if data_nocouple['id'] not in readlist:
                if data_nocouple['id'] != self.except_id and data_nocouple['sex'] == self.sexneed and data_nocouple['idCouple'] == '':
                    age = get_age(currdatetime, data_nocouple['dateborn'])
                    agecoupledx = GetConfig('agecoupled')
                    agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                    # agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                    if agecoupledx1 <= int(age):
                        randpick = 0    # random.randint(0, 3)
                        if randpick == 0:
                            returns = data_nocouple
                            break
            index_num += 1
        return {'id': data_nocouple['id'], 'data': returns, 'index_num': index_num}

    def SaveJSON2File(self):
        SetCoupleData = self.SetCouple()
        jsonData = SetCoupleData['list_coupled']
        list_single = SetCoupleData['list_single']
        num_jsonData = len(jsonData)
        if num_jsonData > 0:
            # append db.coupled
            with open('db.coupled.json', 'a') as afile:
                afile.write(json.dumps(jsonData))
            reformat_db(dbname='coupled')
            # append db.single
            with open('db.single.json', 'w') as afile:
                afile.write(json.dumps(list_single))
            reformat_db(dbname='single')


class GenerateHumanMenopause:
    def __init__(self, numLoops):
        self.numLoops = numLoops

    def SelectDB(self):
        empty_dbtemp(dbname='single')
        empty_dbtemp(dbname='coupled')
        self.menopause = []
        self.dbname = 'single'
        self.SetMenopause()
        list_single = self.list_db
        self.dbname = 'coupled'
        self.SetMenopause()
        list_coupled = self.list_db
        print('len(menopause) = ', len(self.menopause))
        print('len(list_single) = ', len(list_single))
        print('len(list_coupled) = ', len(list_coupled))
        return {'list_menopause': self.menopause, 'list_single': list_single, 'list_coupled': list_coupled}

    def SetMenopause(self):
        print('\nFILTER MENOPAUSE FOR : ', self.dbname)
        # mengosongkan file dbtemp
        currdatetime = '2019-01-01 00:00:00'        # GetLive()
        # exit('before self.list_db')
        self.list_db = loads_db(self.dbname)
        index_num = 0
        n = 0
        for data in self.list_db:
            readlist = load_dbtemp(self.dbname)
            if data['id'] not in readlist and data['sex'] == 'F':
                age = get_age(currdatetime, data['dateborn'])
                agecoupledx = GetConfig('agemenopause')
                agecoupledx1 = int(agecoupledx.strip().split(',')[0])
                # agecoupledx2 = int(agecoupledx.strip().split(',')[1])
                if agecoupledx1 <= int(age):
                    # print(age)
                    # try:
                    self.list_db[index_num]['datemenopause'] = currdatetime
                    save_dbtemp(self.dbname, content=data['id'])
                    # except Exception:
                    #     print('TypeError: string indices must be integers')
            index_num += 1
            n += 1
            # if n >= self.numLoops:
            #     break
        print('\n\n---------len before delete = ', len(self.list_db))
        print('\n\n---------pick menopause--------')
        readtemplist = load_dbtemp(self.dbname)
        print('readtemplist = ', len(readtemplist))
        print('')
        index_ = 0
        hit = 0
        for data_menopause in self.list_db:
            if data_menopause['id'] in readtemplist:
                self.menopause.append(data_menopause)
                self.list_db[index_] = '[removed]'
                hit += 1
            index_ += 1
        print('index_ append = ', index_)
        print('hit append = ', hit)
        print('')
        print('\n\n-----------len after delete = ', len(self.list_db))

    def SaveJSON2File(self):
        SetMenopauseData = self.SelectDB()
        list_menopause = SetMenopauseData['list_menopause']
        list_single = SetMenopauseData['list_single']
        list_coupled = SetMenopauseData['list_coupled']
        num_list_menopause = len(list_menopause)
        if num_list_menopause > 0:
            # append db.coupled
            with open('db.menopause.json', 'a') as afile:
                afile.write(json.dumps(list_menopause))
            reformat_db(dbname='menopause')
            # append db.single
            with open('db.single.json', 'w') as afile:
                afile.write(json.dumps(list_single))
            reformat_db(dbname='single')
            # append db.coupled
            with open('db.coupled.json', 'w') as afile:
                afile.write(json.dumps(list_coupled))
            reformat_db(dbname='coupled')


class GenerateHumanDied:
    def __init__(self, numLoops):
        self.numLoops = numLoops

    def SelectDB(self):
        empty_dbtemp(dbname='single')
        empty_dbtemp(dbname='coupled')
        empty_dbtemp(dbname='menopause')

        self.died = []

        self.dbname = 'single'
        self.SetDied()
        list_single = self.list_db

        self.dbname = 'coupled'
        self.SetDied()
        list_coupled = self.list_db

        self.dbname = 'menopause'
        self.SetDied()
        list_menopause = self.list_db

        print('len(died) = ', len(self.died))
        print('len(list_single) = ', len(list_single))
        print('len(list_coupled) = ', len(list_coupled))
        print('len(list_menopause) = ', len(list_menopause))
        # return {'list_died': self.died, 'list_single': list_single}
        return {'list_died': self.died, 'list_menopause': list_menopause, 'list_single': list_single, 'list_coupled': list_coupled}

    def SetDied(self):
        print('\nFILTER DIED FOR : ', self.dbname)
        # mengosongkan file dbtemp
        currdatetime = '2019-01-01 00:00:00'        # GetLive()
        self.list_db = loads_db(self.dbname)
        index_num = 0
        n = 0
        countz = 0
        for data in self.list_db:
            readlist = load_dbtemp(self.dbname)
            try:
                if data['id'] not in readlist:
                    age = get_age(currdatetime, data['dateborn'])
                    agediedx = GetConfig('agedied')
                    agediedx1 = int(agediedx.strip().split(',')[0])
                    # agediedx2 = int(agediedx.strip().split(',')[1])
                    if agediedx1 <= int(age):
                        try:
                            # time.sleep(.1)
                            # print(data['id'], age)
                            self.list_db[index_num]['datedied'] = currdatetime
                            save_dbtemp(self.dbname, content=data['id'])
                            countz += 1
                        except Exception:
                            print('error :: datedied not set !')
            except Exception:
                pass
            index_num += 1
            n += 1
            if n >= self.numLoops:
                break
        print('countz = ', countz)
        print('\n\n---------len before delete = ', len(self.list_db))
        print('\n\n---------pick died--------')
        readtemplist = load_dbtemp(self.dbname)
        print('readtemplist = ', len(readtemplist))
        index_ = 0
        hit = 0
        for data_died in self.list_db:
            try:
                if data_died['id'] in readtemplist:
                    self.died.append(data_died)
                    self.list_db[index_] = '[removed]'
                    hit += 1
            except Exception:
                pass
            index_ += 1
        print('index_ append = ', index_)
        print('hit append = ', hit)
        print('\n\n-----------len after delete = ', len(self.list_db))

    def SaveJSON2File(self):
        SetDiedData = self.SelectDB()
        list_died = SetDiedData['list_died']
        list_single = SetDiedData['list_single']
        list_coupled = SetDiedData['list_coupled']
        list_menopause = SetDiedData['list_menopause']
        num_list_died = len(list_died)
        if num_list_died > 0:
            # append db.coupled
            with open('db.died.json', 'a') as afile:
                afile.write(json.dumps(list_died))
            reformat_db(dbname='died')
            # write db.single
            with open('db.single.json', 'w') as afile:
                afile.write(json.dumps(list_single))
            reformat_db(dbname='single')
            # write db.coupled
            with open('db.coupled.json', 'w') as afile:
                afile.write(json.dumps(list_coupled))
            reformat_db(dbname='coupled')
            # write db.menopause
            with open('db.menopause.json', 'w') as afile:
                afile.write(json.dumps(list_menopause))
            reformat_db(dbname='menopause')


restart()
currdatetime = GetLive()
h = GenerateHumanData(random.randint(1000, 1000), '0|0')
h.SaveJSON2File()

c = GenerateHumanCouple(random.randint(10, 10))
c.SaveJSON2File()

m = GenerateHumanMenopause(random.randint(10, 200))
m.SaveJSON2File()

m = GenerateHumanDied(random.randint(100, 100))
m.SaveJSON2File()

UpdateStat()
print(GetStat())
