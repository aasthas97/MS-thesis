import re
import os.path
import collections
import pandas as pd
import string


"""Format raw txt files to get IDs in the desired format"""

def ChangeFiles1(filename):
    """Find number, angle pairs. Replace with number[angle]"""
    pattern = re.compile("(\d+)\s+ans =\s+(\d+.?\d*)")
    with open(filename, 'r') as f:
        content = f.read()
        with open(filename, 'w') as f:
            f.write(pattern.sub(r"\1[\2]", content))

def ChangeFiles2(filename):
    """Find PP.nwalks, ans = <number of walks>. Replace with (Number of walks: <number of walks>)"""
    pattern = re.compile("(PP.nwalks\s+ans =\s+)(\d+)")
    with open(filename, 'r') as f:
        content = f.read()
        with open(filename, 'w') as f:
            f.write(pattern.sub(r"(Number of walks: \2)", content))
            
def ChangeFiles3(filename):
    pattern = re.compile("(\])\s+(\d)")
    with open(filename, 'r') as f:
        content = f.read()
        with open(filename, 'w') as f:
            f.write(pattern.sub(r"\1\2", content))

def ChangeFiles4(filename):
    """Remove stray commas"""
    pattern = re.compile("\d+,")
    with open(filename, 'r') as f:
        content = f.read()
        with open(filename, 'w') as f:
            f.write(pattern.sub("", content))


"""Replace 'matches best walk with score' with 'matches best walk <number>'.
Combines walk IDs spanning multiple lines."""

to_keep = re.compile('^\d+.+', re.MULTILINE)
pattern0 = re.compile("(new walk)\s+((Walk number:\d+\s+Score = \d+\s+Matches best walk with score \d+\s+Average distance: .+\s+){1,})")
pattern1 = re.compile('best walk')
pattern2 = re.compile('\](e(-|\+)\d+)') #angle scientific notation
pattern3 = re.compile('(\d+|\])\s+(\d+)')
pattern4 = re.compile(r'(.+)\(Number of walks: (\d+)\)((\s+.+\(Number of walks: \2\)){1,})') # same ID spanning multiple lines and ending in (Number of walks)
pattern5 = re.compile('\(Number of walks: \d+\)')

def partOne(filename):
    with open(filename, 'r') as f:
        content = f.read()
        keep_this = re.findall(to_keep, content)
        found = re.findall(pattern0, content)

        newwalkcount = 1
        for item in found:
            keep_this.append(pattern1.sub(f'best walk {newwalkcount}', item[1]))
            newwalkcount += 1

        write_this = '\n'.join(keep_this)

    return write_this

def partTwo(string_to_alter):
    string_to_alter = pattern2.sub(r'\1]', string_to_alter)
    string_to_alter = pattern3.sub(r'\1\2', string_to_alter)
    return string_to_alter

def partThree(foo):
    found = re.findall(pattern4, foo)
    foo = pattern4.sub('', foo) # remove the stuff that has been found from the string
    allIDs = []
    for item in found:
        new_ID = pattern5.sub('', item[0]) + pattern5.sub('', item[2]) + '(Number of walks: ' + str(item[1]) + ')' # combine IDs spanning multiple lines into single ID
        allIDs.append(new_ID)

    allIDs = [id.replace('\n', '') for id in allIDs] # list of all IDs that spanned multiple lines
    allIDs = '\n'.join(allIDs) # create one big string of IDs from list
    foo = allIDs + foo
    return foo

def WriteToFile(filename, string):
    with open(filename, 'w') as writefile:
        writefile.write(string)  
        
# COMBINE IDs

def MakeDict(filename):
    """returns dicts for each best walk
    best<walknumber> = {matchingwalknumber: score, avdist}"""

    pattern = re.compile("Walk number:(\d+)\s+Score = \d+\s+Matches best walk (\d+) with score (\d+)\s+Average distance: ([0-9e+-\.]+)")
    best1 = {}
    best2 = {}
    best3 = {}
    best4 = {}
    best5 = {}
    best6 = {}
    best7 = {}
    best8 = {}
    best9 = {}
    best10 = {}

    with open(filename, 'r') as filetoread:
        found = re.findall(pattern, filetoread.read())
        for item in found:
            item = [float(str) for str in item]
            if item[1] == 1: # matches best walk 1
                best1[item[0]] = [item[2], item[3]]
            elif item[1] == 2:
                best2[item[0]] = [item[2], item[3]]
            elif item[1] == 3:
                best3[item[0]] = [item[2], item[3]]
            elif item[1] == 4:
                best4[item[0]] = [item[2], item[3]]
            elif item[1] == 5:
                best5[item[0]] = [item[2], item[3]]
            elif item[1] == 6:
                best6[item[0]] = [item[2], item[3]]
            elif item[1] == 7:
                best7[item[0]] = [item[2], item[3]]
            elif item[1] == 8:
                best8[item[0]] = [item[2], item[3]]
            elif item[1] == 9:
                best9[item[0]] = [item[2], item[3]]
            elif item[1] == 10:
                best10[item[0]] = [item[2], item[3]]

    return [best1, best2, best3, best4, best5, best6, best7, best8, best9, best10]

def GetFinalGoodWalks(listofdicts):
    '''Input: List of dicts for all best walks (pass output of MakeDict as input)
    Returns list of walk numbers of best walks'''

    finalgoodwalks = []
    for opendict in listofdicts:
        if bool(opendict) == False: #dict is empty
            pass
        else:
            # print(opendict)

            scores = []
            foundgoodwalk = []
            avdist = []
            for walknum, score in opendict.items():
                if walknum <= 5: # do not include walks with index less than 5
                    pass
                else:
                    scores.append(score[0])
                    avdist.append(score[1])

            try: # scores and avdist may be empty if walknum was < 5. If so, do nothing
                maxscore = max(scores)
                mindist = min(avdist)

                for walknum, score in opendict.items():
                    if maxscore in score:
                        if walknum <= 5:
                            pass
                        else:
                            foundgoodwalk.append(walknum)

                if len(foundgoodwalk) > 1:
                    for everywalk in foundgoodwalk:
                        if mindist in opendict[everywalk]:
                            finalgoodwalks.append(everywalk)
                else:
                    finalgoodwalks.append(foundgoodwalk[0])

            except:
                pass

    return finalgoodwalks

def FinalWalkID(finalgoodwalklist, filename, newfilename):
    for walk in finalgoodwalklist:
        with open(filename, 'r') as openfile:
            IDentries = re.findall(f"[0-9\-e\.\[\]]+\(Number of walks: {walk}\)", openfile.read())
        with open(newfilename, 'a') as newfile:
            for entry in IDentries:
                towrite = entry + "\n"
                newfile.write(towrite)
                
def writeToExcel(filename, key):
    with open(filename) as f:
        allids = re.findall(".+", f.read())
    s = pd.Series(allids, name = key)
    return s
  

  
# MAIN DRIVER
allinfo = []

for idx1 in range(1, 51):
    for idx2 in range(1, 11):
        filename = '.\\Data\\bpldata' + str(idx1) + '_' + str(idx2) + '.txt'
        newfilename = '.\\Data\\bplprocess\\' + str(idx1) + '_' + str(idx2) + '.txt'
        if os.path.isfile(filename):
            ChangeFiles1(filename)
            ChangeFiles2(filename)
            ChangeFiles3(filename)
            ChangeFiles4(filename)
            change_this = partOne(filename)
            changed_once = partTwo(change_this)
            final = partThree(changed_once)
            WriteToFile(filename, final)
            finallist = [int(number) for number in GetFinalGoodWalks(MakeDict(filename))]
            finallist = list(dict.fromkeys(finallist))
            FinalWalkID(finallist, filename, newfilename)
            key = str(idx1) + '_' + str(idx2)
            allinfo.append(writeToExcel(filename, key))
            print(filename, 'done.\n')
    
        else:
            print(filename, 'does not exist.')

df = pd.concat(allinfo, axis = 1)
df.to_excel('skeletonID.xlsx')
