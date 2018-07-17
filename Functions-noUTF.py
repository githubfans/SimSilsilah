import random
import re
from datetime import datetime
from datetime import timedelta


def genword(minchars=3, maxchars=5, istitle=0):
    vocal = ('a', 'e', 'i', 'o', 'u')
    conso = ('w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'b', 'n', 'm')
    group = []
    numchar = random.randint(minchars, maxchars)
    for i in range(numchar):
        rnd = random.randint(0, 10)
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
        if group[1] is not None:
            if group[1] == group[0]:
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
    getx = config.strip().split('{0}=' . format(str))[1]
    getx2 = getx.strip().split(';')[0]
    # print('getx2 = {0}' . format(getx2))
    cari_koma = re.search(',', getx2)
    if cari_koma is not None:
        return getx2
    else:
        return int(getx2)


def GetLive():
    f = open("live.cnf", "r")
    live = f.read()
    if len(live) < 1:
        live = '2000-01-01 00:00:01'
    f.close()
    # print(live)
    return live


def SetLive():
    getLive = GetLive()
    newlive = datetime.strptime(getLive, "%Y-%m-%d %H:%M:%S")
    newlive = newlive + timedelta(seconds=random.randint(3600 * 24, (3600 * (24 * 10))))
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
