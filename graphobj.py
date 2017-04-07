class GraphObj:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.group = 0

    def __addNode(self, id):
        for node in self.nodes:
            if id in node["id"]:
                return "Exists Node!"
        self.nodes.append({"id":id, "group":self.group})
        self.group += 1

    def __addEdge(self, source, target):
        value = 1
        for edge in self.edges:
            if ((source in edge["source"]) and (target in edge["target"])):
                value = edge["value"] + 1
                self.edges[self.edges.index(edge)] = {"source":source, "target":target, "value":value}
                return

            #Undirect
            #if ((source in edge["target"]) and (target in edge["source"])):
            #    value = edge["value"] + 1
            #    self.edges[self.edges.index(edge)] = {"source": target, "target": source, "value": value}
            #    return

        self.edges.append({"source":source, "target":target, "value":value})

    def addObj(self, source, target):
        self.__addNode(source)
        self.__addNode(target)
        self.__addEdge(source, target)

    def toDictionary(self):
        dict = {"nodes":self.nodes, "edges":self.edges}
        return dict