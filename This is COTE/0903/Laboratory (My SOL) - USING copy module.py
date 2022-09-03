import copy
import time

n, m = map(int, input().split())
graph = []
answer = 0

start = time.time()
for _ in range(n):
    graph.append(list(map(int, input().split())))

# direction
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(count):
    global answer

    # DFS를 통해서 바이러스 퍼뜨리기
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                    temp[nx][ny] = 2
                    virus(nx, ny)

    # 안전 영역 체크
    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1

        return score
    

    # 울타리 3개인 경우
    if count == 3:
        temp = copy.deepcopy(graph)

        # 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역 계산
        answer = max(answer, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1

                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
end = time.time()
print(answer)
print("걸린 시간 :", end - start)

# 걸린 시간 : 9.648868083953857

