# stc = input()
# sch = input()

stc = 'kㅎk'
sch = 'kㅎㅎ'

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

