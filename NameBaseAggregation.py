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

nameDict = {}

for data in jsonData:
    authors = data['author'].split(",")
    for author in authors:
        author = brank.sub('', author).strip()
        if not r.match(author):
            orig = author
            roma = conv.do(author)
            print(orig)
            print(roma)

            max = 0.0
            maxkey = ""
            for key in nameDict.keys():
                diffrat = difflib.SequenceMatcher(None, key, roma).ratio()
                if diffrat > max:
                    max = diffrat
                    maxkey = key

            print("%s : %s : %f" %(roma, maxkey, max))

            if max >= 0.8:
                if maxkey not in nameDict[maxkey]:
                    nameDict[maxkey].append(roma)
            else:
                 nameDict[roma] = [orig]

print(nameDict)