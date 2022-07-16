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

# print(num)
# print(sign)

# sign에 대해서 조합 적용! permutaions
from itertools import permutations
import copy

sign_list = list(permutations(sign, len(sign)))
print(sign_list)

answer_list = []
for s in sign_list:
    iter_num = copy.deepcopy(num)
    iter_op = list(copy.deepcopy(s))
    answer = iter_num.pop(0)
  
    while iter_num:
        print(iter_num)
        print(s)
        next_num = iter_num.pop(0)
        print(answer, next_num)

        op = iter_op.pop(0)
        if op == "+":
            answer = sum(answer, next_num)
        elif op == "-":
            answer = subtract(answer, next_num)
        elif op == "*":
            answer = multi(answer, next_num)
        elif op == "/":
            answer = divide(answer, next_num)
      
        print(answer)
      
    print("answer: ", answer)
    answer_list.append(answer)


print(max(answer_list), min(answer_list))
