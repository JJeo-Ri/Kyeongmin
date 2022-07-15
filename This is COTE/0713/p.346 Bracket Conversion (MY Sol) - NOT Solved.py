def check_balance(s): # 균형잡힌 괄호 문자열인지 체크
    st = [s[0]]
    
    for idx in range(1, len(s)):
        st.append(s[idx])
        
        if len(st) >= 2 and st[-2] == '(' and st[-1] == ')':
            st.pop()
            st.pop()
        
        if not st:
            return idx # 균형잡혔다면, 해당 index를 반환
        
    return False


def check_correct(s): # 올바른 괄호 문자열인지 체크!
    st = []
    
    for ss in s:
        st.append(ss)
        
        if len(st) >= 2 and st[-2] == '(' and st[-1] == ')':
            st.pop()
            st.pop()
            
    return True if not st else False

### 위의 사용자 함수까지는 잘 동작함! ###

answer = ''
def solution(p):
    global answer
    
    if not p:
        return p
    
    if check_correct(p): # 이미 올바른 괄호 문자열이라면.. 그대로 반환
        return p
    
    idx = check_balance(p)
    if idx: # 분할 가능 시 3번 수행!
        u, v = p[:idx + 1], p[idx + 1:]
        print("u :", u, "v :", v)
        answer += u
        solution(v)        
    else: # 4번 수행
        
    
    
    
    # print(check_correct(p))
    # print(check_balance(p))
    
    return answer
