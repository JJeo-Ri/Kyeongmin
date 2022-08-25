n, m = map(int, input().split())
graph = []
answer = 0

for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)
def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] != 0:
        return

    graph[i][j] = -1

    # 동, 서, 남, 북
    dfs(i - 1, j)
    dfs(i, j - 1)
    dfs(i + 1, j)
    dfs(i, j + 1)

    return True

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)
