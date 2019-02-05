stc = input()
sch = input()

def mu_sic (stc, sch):
    stclen = len(stc)
    schlen = len(sch)
    for i in range(stclen-schlen):
        for j in range(schlen):
            if stc[i+j] != sch[j] :
                break
        else :
            return f'{i+1} 번째부터 같습니다.'
    return f'일치하는 문자가 없습니다.'
print(mu_sic(stc, sch))

# 선생님 코드
def BruteForce(t, p) :
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    while j < M and i < N :
        if t[i] != p[j] :
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M : return i - M
    else: return i


T = "abcabcdefdadddddgdsasdfesdfkasdf"
P = "ddddd"
print(T[ BruteForce(T, P):] )