import igraph as ig
g = ig.Graph()  # новый пустой граф
with open("European_countries.txt") as countries:  # достаем вершины из списка стран
    for i in countries.readlines():
        g.add_vertex(i[:-1])
with open("list.csv") as edges:  # достаем ребра из файла
    for i in edges.readlines():
        u = i.split(',')[0][1:-1]
        v = i.split(',')[-1][1:-2]
        g.add_edge(u, v)

# maximum stable set
for vertex in g.largest_independent_vertex_sets()[0]:  # перебираем все вершины в найденном с помощью библиотеки множестве
    print(g.vs[vertex]["name"], end=', ')
print()
