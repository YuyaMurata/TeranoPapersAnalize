import json

def main():
    f = open('trn_papers.json', 'r')
    jsonData = json.load(f)

    yearDict = {}

    for data in jsonData:
        if data["year"] not in yearDict:
            yearDict[data["year"]] = 0
        yearDict[data["year"]] += 1

    for year in yearDict.keys():
        print(str(year)+","+str(yearDict[year]))

if __name__ == '__main__':
    main()