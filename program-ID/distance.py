"""Select an ID for each object and compute edit + angle distance"""
import pandas as pd
import numpy as np
import re
import string

def levenshteinDistance(s1, s2):
    s1 = re.sub('\[\d+.*\]', '', s1)
    s1 = re.sub('\(Number of walks: \d+\)', '', s1)
    s2 = re.sub('\[\d+.*\]', '', s2)
    s2 = re.sub('\(Number of walks: \d+\)', '', s2)
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def angledistance(string1, string2):
    anglepattern = re.compile('\[(\d+\.?[1234567890e\-\+]*)\]')
    brackets = re.compile('\[|\]')

    found1 = re.findall(anglepattern, string1)
    found2 = re.findall(anglepattern, string2)
    angles1 = [float(brackets.sub('', angle)) for angle in found1]
    angles2 = [float(brackets.sub('', angle)) for angle in found2]


    listindex = min(len(angles1), len(angles2))
    alldistances = []
    for index in range(listindex):
        angle1 = angles1[index]
        angle2 = angles2[index]
        angdist = abs(angle1-angle2)
        alldistances.append(angdist)

    if len(alldistances) == 0: # one of the strings has no angles
        averageangledistance = 0
    else:
        averageangledistance = sum(alldistances)/len(alldistances)

    return averageangledistance

df = pd.read_excel('.\\Data\\skeletonID.xlsx', keep_default_na=False)
allitems = list(df.columns.values) # get names of all items
del(allitems[0]) # first column is empty
ids = dict()
for item in allitems:
    itemids = [id for id in df[item] if id != ''] # list of all IDs for an item
    # if len(itemids) <= 0:
    #     print(item)
    idindex = np.random.randint(0, len(itemids))
    ids.update({item: itemids[idindex]}) # dictionary containing (item: [all corresponding IDs]) pairs

finaldata = dict()

for firstobject, firstID in ids.items(): # iterate through dictionary
    distances = []
    for secondobject, secondID in ids.items():
        # index = 1
        print(firstobject, secondobject)
        editdist = levenshteinDistance(firstID, secondID)
        angledist = angledistance(firstID, secondID)
        totaldist = editdist + angledist
        distances.append(totaldist)

    # key = firstobject + secondobject + str(index)
    finaldata.update({firstobject: distances})
    # index += 1

df = pd.DataFrame(finaldata)
df.to_excel('skeleton_dists.xlsx')
