import networkx as nx


def dfs(v, p):
    global graph
    s = 0
    for u, w in graph[v]:
        if u != p:
            s += dfs(u, v) + w
    return s


g = nx.Graph()  # новый граф
with open("edges_with_w.csv") as edges:  # достаем ребра из файла
    for i in edges.read().split('\n')[1:]:
        u = i.split(',')[0][1:-1]
        v = i.split(',')[1][1:-1]
        w = i.split(',')[2][1:-1]
        if u != 'Ireland' and v != 'Ireland':
            g.add_edge(u, v, weight=int(w))
    tree = nx.minimum_spanning_tree(g)  # находим минимальное остовное дерево с помощью библиотеки
    print(*tree.edges(data=True), sep='\n')  # выводим на экран

# поиск центроида
graph = dict()  # здесь будет список смежности остовного дерева
vertexes = set()  # мн-во вершин
for i in tree.edges(data=True):  # превращаем граф в список смежности
    u = i[0]
    v = i[1]
    w = i[2]['weight']
    vertexes.add(u)
    vertexes.add(v)
    if u in graph:
        graph[u].append((v, w))
    else:
        graph[u] = [(v, w)]
    if v in graph:
        graph[v].append((u, w))
    else:
        graph[v] = [(u, w)]
centroid = []  # мн-во для вершин центроида
cenroid_max_branch = 10**9  # max branch size вершин из мн-ва выше
for v in vertexes:   # считаем max branch size для каждой из вершин
    current_branch_size = 0
    for u, w in graph[v]:  # перебираем все возможные branch с помощью dfs
        current_branch_size = max(current_branch_size, dfs(u, v) + w)
    if current_branch_size < cenroid_max_branch:   # обновляем ответ
        centroid = [v]
        cenroid_max_branch = current_branch_size
    elif current_branch_size == cenroid_max_branch:
        centroid.append(v)
print(centroid)  # центроид найден

# код Прюфера
number = 0
new_label = dict()
for i in tree.nodes:  # перенумеровываем вершины
    new_label[i] = number
    number += 1

tree = nx.relabel_nodes(tree, new_label)  # ищем код с помощью библиотеки
print(new_label)   # выводим соответствие номеров названием
print(nx.to_prufer_sequence(tree))  # выводим код
