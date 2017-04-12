import json
import codecs

from graphobj import GraphObj

fileName = "trn_author_graph_undirect_degree"

def main():
    #GML
    f = open("gml/"+fileName+".gml", 'r')

    graph = GraphObj()

    node_flg = 0
    edge_flg = 0

    list = []

    for data in f:
        if "node" in data:
            node_flg = 1
            continue

        if "edge" in data:
            edge_flg = 1
            continue

        if "[" in data:
            continue
        if "]" in data:
            if node_flg == 1:
                graph.addNode(int(list[0]), list[1], int(list[2]), int(list[3]))
                node_flg = 0
            if edge_flg == 1:
                graph.addEdge(int(list[0]), int(list[1]), int(list[2]))
                edge_flg = 0
            list = []
            continue

        if node_flg or edge_flg == 1:
            d = data.strip()
            if "\"" in d:
                d = d.replace("\"", "")
            list.append(d[d.find(" ")+1:len(d)])

    print(graph.toDictionary())
    f.close()

    f = codecs.open("json/"+fileName+'.json', 'w', 'utf-8')
    json.dump(graph.toDictionary(), f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()

if __name__ == '__main__':
    main()