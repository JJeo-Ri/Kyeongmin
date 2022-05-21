import time

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start = time.time()
data.sort() # 입력받은 수 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하

end = time.time()
print(result) # 최종 답안 출력
print("걸린 시간 :", end - start)
# 걸린 시간 : 1.8835067749023438e-05
# 가장 빠른 방법!
