import time

n = int(input())
data = list(map(int, input().split()))
start = time.time()

data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때, 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
end = time.time()
print("걸린 시간: ", end - start)
# 걸린 시간: 6.771087646484375e-05
