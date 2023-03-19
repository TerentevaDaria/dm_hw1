import networkx as nx
g = nx.Graph()  # новый граф
with open("list.csv") as edges:  # достаем ребра из файла и записываем в граф
    for i in edges.readlines():
        u = i.split(',')[0][1:-1]
        v = i.split(',')[-1][1:-2]
        g.add_edge(u, v)
print(len(nx.max_weight_matching(g)))
print(*nx.max_weight_matching(g), sep='\n')  # функция ищет matching с максимальным весом. так как у нас все веса равны 1, то найденное мн-во совпадает с maximum matching
