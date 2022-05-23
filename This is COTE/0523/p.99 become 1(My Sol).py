import time

# 나눌 수 있으면 나누고, 아니면 1을 빼는 식으로
n, k = map(int, input().split())
start = time.time()
answer = 0

while n != 1:
    if n % k == 0:
        n //= k
        answer += 1
    else:
        n -= 1
        answer += 1

end = time.time()
print(answer)
print("걸린 시간 :", end - start)
# 걸린 시간 : 1.52587890625e-05(나누기 연산) / 걸린 시간 : 6.4373016357421875e-06(몫 연산)
# 몫 연산이 나누기 연산보다 더 빠름?
