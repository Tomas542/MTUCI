class Graph:
    #при создание объекта класса граф мы передаём в него количество вершин и создаём пустой массив
    def __init__(self, vertices:int) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, u:int, v:int) -> None:
        self.graph.append([u, v])
 
# n = input()
# s = input()

n = 5
s = "2 3 5 3 -1"

#сплитим числа из второй строчки
nums = [int(n) for n in s.split(" ")]
g = Graph(n)

#проходимся по всем npc и создаём рёбра
for i in range(int(n)):
    #поскокльку в примере на листочке ребёра с 1 начинаются, то прибавляем к i единичку, чтобы сместить массив nums по индексу
    simp = i + 1

    #если npc отдаёт предмет, мы записываем его связь с 0 вершиной, которая и отвечает за отданный предмет и от которой мы будем всё проверять
    if nums[i] == -1:
        g.add_edge(0, simp)

    else:
        g.add_edge(nums[i], simp)

def bellman_ford(gr) -> list[int]:
    #по алгоритму заполняем расстояния до всех вершин в бесконечность, кроме стартовой 0 вообще, можно любое значение, кроме -1
    dist = [float("inf")] * (gr.V + 1)
    dist[0] = -1

    for _ in range(gr.V - 1):
        for u, v in gr.graph:
            #если мы добрались до npc u за -1, значит он тоже отдаёт нам предмет
            if dist[u] == -1:
                #и мы можем идти к npc v, чтобы завершить его квест
                dist[v] = -1
                print(f"Dist array = {dist}")

    return dist

#создаём множество
check = set(bellman_ford(g))
print(f"check_set = {check}")

#если во множестве check только 1 элемент (-1), значит все квесты выполнены
if len(check) == 1:
    print("Yes")
    
else:
    print("No")
