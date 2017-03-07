class PaperObj:
    def __init__(self, title, authors, year, info):
        self.title = title
        self.authors = authors
        self.year = year
        self.info = info
    def string(self):
        return format("%s:%s,%s,%s" %(self.authors, self.title, self.info, self.year))