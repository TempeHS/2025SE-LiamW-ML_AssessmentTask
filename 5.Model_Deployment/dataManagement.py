
def findgenre(genre):
    list = []
    genrelist = ["Action","Adventure","Fighting","Misc","Platform","Puzzle","Racing","Role-Playing","Shooter","Simulation","Sports","Strategy"]
    for type in genrelist:
        if genre == type:
            list.append(True)
        else:
            list.append(False)
    return list

def popfilter(data):
    try:
        if not 0 < float(data) < 1:
            return False
        return True
    except ValueError:
        return False


def yearfilter(year):
    try:
        if not 1982 < int(year) < 2030:
            return False
        return True
    except ValueError:
        return False

def csvReady(list):
    newlist = [f"NaN,NaN,NaN,{list[1]},NaN,0,0,0,0,{list[14]},{list[2]},{list[3]},{list[4]},{list[5]},{list[6]},{list[7]},{list[8]},{list[9]},{list[10]},{list[11]},{list[12]},{list[13]},{list[0]}"]
    return newlist