from py2neo import Graph, Node, Relationship,NodeMatch
from config import graph
with open("../raw_data/relation.txt",encoding='utf-8') as f:
    for line in f.readlines():
        #将文件中取出的每行字符串以逗号为分界符转化成列表
        rela_array=line.strip("\n").split(",")
        print(rela_array)
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})"%(rela_array[3],rela_array[0]))
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[1]))
        graph.run(
            "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[1], rela_array[2],rela_array[2])

        )

# from py2neo import Node, Relationship, Graph
#
# a = Node('Person', name='Alice')
# b = Node('Person', name='Bob')
# r = Relationship(a, 'KNOWS', b)
# s = a | b | r
# graph = Graph(password='123456')
# graph.create(s)
