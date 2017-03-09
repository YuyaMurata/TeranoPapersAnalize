class PaperObj:
    def __init__(self, authors, title, info, year):
        self.authors = authors
        self.title = title
        self.info = info
        self.year = year

    # Mapを作成
    def toDictionary(self):
        jsonDict = {"author":self.authors, "title":self.title, "info":self.info, "year":self.year}
        return jsonDict

    def string(self):
        return format("%s:%s,%s,%s" %(self.authors, self.title, self.info, self.year))