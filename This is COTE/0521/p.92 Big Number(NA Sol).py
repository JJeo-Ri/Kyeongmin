import time

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start = time.time()
data.sort() # 입력받은 수 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면, 반복문 탈출
            break

        result += first
        m -= 1 # 더할때마다 1씩 빼기

    if m == 0: # m이 0이라면, 반복문 탈출
        break

    result += second # 두번째로 큰 수를 한 번 더하기
    m -= 1 # 더할때마다 1씩 빼기

end = time.time()
print(result) # 최종 답안 출력
print("걸린 시간 :", end - start)
# 걸린 시간 : 2.2172927856445312e-05
