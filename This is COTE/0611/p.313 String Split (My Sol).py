# 0과 1의 갯수를 체크
# 작은 것을 큰 갯수로 replace

s = input()
count_z = s.count('0')
count_o = s.count('1')
answer = 0

print(count_z, count_o)
if count_z >= count_o:
    print('1'*count_o)
    s.replace('1'*count_o, '0'*count_o)
else:
    print('0'*count_z)
    s.replace('0'*count_z, '1'*count_z)

print(s)
