# NOT Solved
n, k = map(int, input().split())
graph = []
order = set([])

for _ in range(n):
    temp = input().split()  
    graph.append(list(map(int, temp)))
    order.update(temp)

s, x, y = map(int, input().split())
# print(graph)
# print(order)
order = sorted(order)
# print(order)

for i in range(n):
    for j in range(k):
        for o in order[1:]:
            print(o)
            if graph[i][j] == o:
                # 동, 서, 남, 북 감염
                try:
                    if graph[i - 1][j] == 0:
                        graph[i - 1][j] = o
                except:
                    pass

                try:
                    if graph[i][j - 1] == 0:
                        graph[i][j - 1] = o
                except:
                    pass

                try:
                    if graph[i + 1][j] == 0:
                        graph[i + 1][j] = o
                except:
                    pass

                try:
                    if graph[i][j + 1] == 0:
                        graph[i][j + 1] = o
                except:
                    pass
                print(graph)

print(graph[x-1][y-1])
