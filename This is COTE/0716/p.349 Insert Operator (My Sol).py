def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return int(a // b)

n = int(input())
num = list(map(int, input().split())) # 수열
sign = []
cnt = list(map(int, input().split())) # 부호

for idx in range(len(cnt)):
    if idx == 0: # +
        for _ in range(cnt[idx]):
            sign.append("+")
    elif idx == 1: # -
        for _ in range(cnt[idx]):
            sign.append("-")
    elif idx == 2: # x
        for _ in range(cnt[idx]):
            sign.append("*")
    elif idx == 3: # /
        for _ in range(cnt[idx]):
            sign.append("/")

print(num)
print(sign)

# sign에 대해서 조합 적용! combination
