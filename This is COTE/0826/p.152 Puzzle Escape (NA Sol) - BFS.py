from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    # deque로 큐 생성
    queue = deque()
    queue.append((i, j))

    # 큐가 빌 때 까지 계속 수행!
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            # 다음 x, y 좌표 수행(dx, dy 값을 더해서)
            nx = x + dx[i]
            ny = y + dy[i]

            # 수행할 수 없는 위치이면 PASS
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 처음 방문했을 때..
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
