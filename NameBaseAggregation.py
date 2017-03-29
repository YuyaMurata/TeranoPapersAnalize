from pykakasi import kakasi
import difflib

import json
import re

f = open('trn_papers.json', 'r')
jsonData = json.load(f)

#Kakasi
kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

#Pattern
r = re.compile(r'^[a-zA-Z&]')
brank = re.compile(r'\(.+?\)$')
period = re.compile(r'.*\.$')
simbol = re.compile(r'[!-/:-@[-`{-~]')
space = re.compile(r'\s')

nameDict = {}

def japanese(authors):
    for author in authors:
        if r.match(author):
            continue

        author = brank.sub('', author).strip()

        orig = author
        roma = conv.do(author).lower()
        #print(orig)
        #print(roma)

        roma1 = space.sub('', roma)

        max = 0.0
        maxkey = ""
        for key in nameDict.keys():
            diffrat = difflib.SequenceMatcher(None, key, roma1).ratio()
            if diffrat > max:
                max = diffrat
                maxkey = key

        print("%s : %s : %f" %(roma1, maxkey, max))

        if max >= 0.8:
            if orig not in nameDict[maxkey]:
                nameDict[maxkey].append(orig)
        else:
             nameDict[roma1] = [orig]

def english(authors):
    for author in authors:
        if not r.match(author):
            continue

        author = brank.sub('', author).strip()

        orig = author
        roma = conv.do(author).lower()
        #print(orig)
        #print(roma)

        roma1 = simbol.sub('', space.sub('', roma))

        max = 0.0
        maxkey = ""
        for key in nameDict.keys():
            diffrat = difflib.SequenceMatcher(None, key, roma1).ratio()
            if len(roma.split(" ")) > 1:
                roma2 = simbol.sub('', roma.split(" ")[1] + roma.split(" ")[0])
                diffrat2 = difflib.SequenceMatcher(None, key, roma2).ratio()
                if diffrat < diffrat2:
                    diffrat = diffrat2
            if diffrat > max:
                max = diffrat
                maxkey = key

        print("%s : %s : %f" %(roma1, maxkey, max))

        if max >= 0.8:
            if orig not in nameDict[maxkey]:
                nameDict[maxkey].append(orig)
        else:
             nameDict[roma1] = [orig]

def formalize(data):
    str = data['author']
    authors = []

    if ' and ' in str:
        str = str.replace(' and ', ', ')

    if '.,' in str:
        authors = str.split(".,")
    else :
        if period.match(str):
            authors = [str]
        else :
            authors = str.split(",")

    return authors

for data in jsonData:
    authors = formalize(data)
    japanese(authors)

for data in jsonData:
    authors = formalize(data)
    english(authors)

print(nameDict)

#CreateJSON
f = open('trn_namebase_aggre.json', 'w')
json.dump(nameDict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
f.close()