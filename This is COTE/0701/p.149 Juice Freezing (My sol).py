n, m = map(int, input().split())
graph = []
answer = 0

for _ in range(n):
    graph.append(list(map(int, input())))

# print(graph)

def dfs(i, j):
    # 종료 조건 기입
    if i < 0 or j < 0 or i >= n or j >= m or graph[i][j] != 0:
        return

    graph[i][j] = -1
      
    # 동서남북
    dfs(i, j + 1)
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j - 1)

    answer += 1

for i in range(n):
    for j in range(m):
        dfs(i, j)

print(answer)
