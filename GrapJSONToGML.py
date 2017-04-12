import json
import codecs

fileName = "trn_author_graph_seq_out"

def nodes(data):
    node = ""

    for n in data:
        node = node + "\tnode\n\t[\n"
        node = node + "\t\tid "+ str(n['id'])+"\n"
        node = node + "\t\tlabel \"" + n['label'] + "\"\n"
        node = node + "\t\tcolor " + str(n['group']) + "\n"
        node = node + "\t\tsize " + str(n['size']) + "\n"
        node = node + "\t]\n"
        #print(node)

    return node

def edges(data):
    edge = ""

    for e in data:
        edge = edge + "\tedge\n\t[\n"
        edge = edge + "\t\tsource " + str(e['source']) + "\n"
        edge = edge + "\t\ttarget " + str(e['target']) + "\n"
        edge = edge + "\t\tvalue " + str(e['value']) + "\n"
        edge = edge + "\t]\n"
        #print(edge)

    return edge

def main():
    #JSON Data
    f = codecs.open("json/"+fileName+".json", 'r', "utf-8")
    gjson = json.load(f)
    f.close()

    gml = "graph\n[\n"
    gml = gml + nodes(gjson['nodes'])
    gml = gml + edges(gjson['links'])
    gml = gml + "]\n"

    print(gml)

    with open("gml/"+fileName+".gml", "w") as file:
        print(gml, file=file)

if __name__ == '__main__':
    main()