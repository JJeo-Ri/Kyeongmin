import time

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

start = time.time()

def dfs(i, j, t): # 행 / 열 / track
    if i < 0 or j < 0 or i >= n or j >= m or graph[i][j] != 1:
        return

    if graph[i][j] > 1: # 이미 1번 이상 방문한 경우
        pass
    else:
        graph[i][j] = t
        t += 1

    # 상, 하, 좌, 우
    dfs(i + 1, j, t)
    dfs(i, j + 1, t)
    dfs(i - 1, j, t)
    dfs(i, j - 1, t)

tracking = 1
dfs(0, 0, tracking)
print(graph[n - 1][m - 1])
# print(graph)
end = time.time()

print("걸린 시간 :", end - start)
# 걸린 시간 : 0.00013947486877441406
'''
위의 풀이는 운좋게 얻어걸린 것! (왼쪽 먼저 수행하게 하면 답이 틀리게 된다)
우측 아랫방향에 도달하는 것이 목적이므로 여기에만 초점을 맞추면 상관은 없지만,
솔루션은 아님!
'''
    
