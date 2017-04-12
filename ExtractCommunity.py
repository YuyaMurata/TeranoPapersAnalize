import json
import codecs

def main():
    f = codecs.open('json/trn_author_graph_undirect_edgebetweenes_com.json', 'r', "utf-8")
    jsonData = json.load(f)

    groupDict = {}

    for data in jsonData["nodes"]:
        print(data)
        if str(data["group"]) not in groupDict:
            groupDict[str(data["group"])] = []
        groupDict[str(data["group"])].append(data["label"])

    print(groupDict)

    #for group in groupDict.keys():
    #    print(group+":"+groupDict[group])

if __name__ == '__main__':
    main()