import json
import re

def main():
    f = open('trn_papers.json', 'r')
    jsonData = json.load(f)

    #Pattern
    r = re.compile(r'^[a-zA-Z&]')
    brank = re.compile(r'\(.+?\)$')

    for data in jsonData:
        authors = data['author'].split(",")
        for author in authors:
            author = brank.sub('', author).strip()
            if not r.match(author):
                print(author)

if __name__ == '__main__':
    main()