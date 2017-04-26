class GraphObj:
    def __init__(self):
        self.nodes = []
        self.links = []
        self.group = 0
        self.size = 20
        self.id_dict = {}

    def __addNode(self, label):
        for node in self.nodes:
            if label == node["label"]:
                return "Exists Node!"
        self.nodes.append({"id":self.group, "label":label, "group":self.group, "size":self.size})
        self.id_dict[label] = self.group
        self.group += 1

    def __addEdge(self, source, target):
        value = 1
        src_id = self.id_dict[source]
        trg_id = self.id_dict[target]

        for edge in self.links:
            if ((src_id == edge["source"]) and (trg_id == edge["target"])):
                value = edge["value"] + 1
                self.links[self.links.index(edge)] = {"source":src_id, "target":trg_id, "value":value}
                return

        self.links.append({"source":src_id, "target":trg_id, "value":value})

    def addBidEdge(self, source, target):
        value = 1
        src_id = self.id_dict[source]
        trg_id = self.id_dict[target]

        for edge in self.links:
            if ((src_id == edge["source"]) and (trg_id == edge["target"])):
                value = edge["value"] + 1
                self.links[self.links.index(edge)] = {"source": src_id, "target": trg_id, "value": value}
                return

            # Undirect
            if ((src_id == edge["target"]) and (trg_id == edge["source"])):
                value = edge["value"] + 1
                self.links[self.links.index(edge)] = {"source": trg_id, "target": src_id, "value": value}
                return

        self.links.append({"source": src_id, "target": trg_id, "value": value})

    def addNode(self, id, label, group, size):
        for node in self.nodes:
            if id == node["id"]:
                return "Exists Node!"
        self.nodes.append({"id":id, "label":label, "group":group, "size":size})

    def addEdge(self, source, target, value):
        self.links.append({"source": source, "target": target, "value": value})

    def addDirectObj(self, source, target):
        self.__addNode(source)
        self.__addNode(target)
        self.__addEdge(source, target)

    def addUndirectObj(self, source, target):
        self.__addNode(source)
        self.__addNode(target)
        self.__addBidEdge(source, target)

    def toDictionary(self):
        dict = {"nodes":self.nodes, "links":self.links}
        return dict