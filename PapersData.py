import sys
from selenium import webdriver
from bs4 import BeautifulSoup

def createNetworkData(driver, p1, p2, file):
    #Get html
    driver.get(p1)
    html1 = driver.page_source
    driver.get(p2)
    html2 = driver.page_source

    hd_soup1 = BeautifulSoup(html1, 'html.parser')
    hd_soup2 = BeautifulSoup(html2, 'html.parser')

    paperList = hd_soup1.find_all("li") + hd_soup2.find_all("li")

    print(len(paperList))
    print(paperList, file=file)

def main():
    #webdriver
    driver = webdriver.PhantomJS()

    #html
    paper1 = "http://www.trn.dis.titech.ac.jp/GEAR/jp/papers.html"
    paper2 = "http://www.trn.dis.titech.ac.jp/GEAR/jp/old_papers.html"

    with open("papers.html", "w") as file:
        print("<html>", file=file)
        createNetworkData(driver, paper1, paper2, file)
        print("</html>", file=file)

    #finish
    driver.quit()

if __name__ == '__main__' :
    main()