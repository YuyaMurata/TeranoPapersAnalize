import json
import re

from graphobj import GraphObj

#Name Dictionary
fname = open('trn_namebase_aggre.json', 'r')
jsonNameData = json.load(fname)
fname.close()

#Pattern
period = re.compile(r'.*\.$')

#著者の抽出と変換
def extractAuthor(str):
    authors = []

    if ' and ' in str:
        str = str.replace(' and ', ', ')

    if '.,' in str:
        authors = str.split(".,")
    else:
        if period.match(str):
            authors = [str]
        else:
            authors = str.split(",")

    #null
    authors = list(filter(lambda s:s != '', authors))

    for i in range(len(authors)):
        author  = authors[i].strip()

        for nameList in jsonNameData.values():
            if author in nameList:
                author = nameList[0]
                break

        authors[i] = author

    return authors

def main():
    #Paper Data
    fpaper = open('trn_papers.json', 'r')
    jsonData = json.load(fpaper)
    fpaper.close()

    graph = GraphObj()

    for paper in jsonData:
        authors = extractAuthor(paper['author'])
        print(authors)

        #add node and edge Authors All link
        #for i in range(len(authors)-1):
        #    for j in range(i+1, len(authors)):
        #        graph.addObj(authors[i], authors[j])

        # add node and edge Author Sequential Link
        for i in range(len(authors)-1):
            graph.addObj(authors[i], authors[i+1])


    # Graph Data
    f = open('trn_author_graph.json', 'w')
    json.dump(graph.toDictionary(), f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()

if __name__ == '__main__':
    main()