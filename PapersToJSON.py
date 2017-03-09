import re
import json

import pandas as pd
from bs4 import BeautifulSoup

from paperobj import PaperObj

def main():
    #html
    f = open("trn_papers.html", "r")
    soup = BeautifulSoup(f, 'html.parser')

    #CSV
    #df = pd.DataFrame(columns=['author', 'title', 'info', 'year', 'tag'])
    list = []
    i = 0
    for line in soup.find_all("li"):
        str = line.string
        str = str.replace('\n', ' ')
        str = str.replace('\r', ' ')
        str = str.replace('：', ':')
        str = str.replace('，', ',')
        str = str.replace('．', '.')

        authors = str[0:str.find(':')]
        str = str.replace(authors + ":", '')
        r = re.compile('\s+')
        authors = r.sub('', authors)
        #print(authors)

        #title抽出　整形
        title = str[0:str.find('.')]
        str = str.replace(title + ".", '')
        title = title.replace('"','').strip()
        r = re.compile('\s\s*')
        title = r.sub(' ', title)
        #print(title)

        info = str[0:str.rfind(',')]
        str = str.replace(info+",", '')
        info = r.sub(' ', info)
        #print(info)

        year = str
        r = re.findall('(\d{4})', year)
        year = r[0]
        #print(year)

        obj = PaperObj(authors, title, info, year)
        list.append(obj.toDictionary())

        print(obj.toDictionary())

        #CSV
        #se = pd.Series([authors, title, info, year, ""], index=['author', 'title', 'info', 'year', 'tag'])
        #df = df.append(se,  ignore_index=True)

        #print("%d %s" % (i, obj.string()))
        i = i+1

    #Create CSV
    #print(df)
    #df.to_csv('trn_papers.csv')

    #CreateJSON
    #print(list)
    f = open('trn_papers.json', 'w')
    json.dump(list, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()


if __name__ == '__main__':
    main()