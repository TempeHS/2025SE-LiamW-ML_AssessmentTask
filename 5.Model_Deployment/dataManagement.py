
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
        if not 0 < int(data) < 1:
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
