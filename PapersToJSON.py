import re
from bs4 import BeautifulSoup
from paperobj import PaperObj


def main():
    #html
    f = open("papers.html", "r")
    soup = BeautifulSoup(f, 'html.parser')

    i = 0
    for line in soup.find_all("li"):
        str = line.string
        str = str.replace('\n', '')
        str = str.replace('\r', '')
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
        print(title)
        if title.find(',') > -1:
            title = str[0:str.rfind(',')]
            str = str.replace(title + ".", '')
        else:
            str = str.replace(title + ",", '')
        title = title.replace('"','').strip()
        r = re.compile('\s\s+')
        title = r.sub(' ', title)
        print(title)

        info = str[0:str.rfind(',')]
        str = str.replace(info+",", '')

        year = str
        r = re.findall('(\d{4})', year)
        year = r[0]
        #print(year)

        obj = PaperObj(title, authors, info, year)
        #print("%d %s" % (i, obj.string()))
        i = i+1

if __name__ == '__main__':
    main()