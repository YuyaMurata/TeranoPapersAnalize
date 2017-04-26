import json
import re
import codecs

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

def undirect(authors, graph):
    for i in range(len(authors) - 1):
        for j in range(i + 1, len(authors)):
            graph.addUndirectObj(authors[i], authors[j])

def direct(authors, graph, inout):
    for i in range(len(authors)-1):
        if 'in' in inout:
            graph.addDirectObj(authors[i], authors[i + 1])
        elif 'out' in inout:
            last = len(authors)-1
            graph.addDirectObj(authors[last-i], authors[last-(i+1)])

def main():
    #Paper Data
    fpaper = open('trn_papers.json', 'r')
    jsonData = json.load(fpaper)
    fpaper.close()

    undirect_graph = GraphObj()
    direct_graph = GraphObj()

    for paper in jsonData:
        authors = extractAuthor(paper['author'])
        print(authors)

        #add node and edge Authors All link. need to change graphobj
        undirect(authors, undirect_graph)

        # add node and edge Author Sequential Link
        direct(authors, direct_graph, 'in')


    # Undirect Graph Data
    f = codecs.open('json/trn_author_undirectgraph.json', 'w', 'utf-8')
    json.dump(undirect_graph.toDictionary(), f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()

    # Direct Graph Data
    f = codecs.open('json/trn_author_directgraph.json', 'w', 'utf-8')
    json.dump(direct_graph.toDictionary(), f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()

if __name__ == '__main__':
    main()