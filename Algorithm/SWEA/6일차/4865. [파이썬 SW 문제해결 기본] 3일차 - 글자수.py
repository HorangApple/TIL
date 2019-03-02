import sys
sys.stdin = open("input.txt","r")

T = int(input())

def solution(str1,str2) :
    str1len=len(str1)
    # '문자:index'형식으로 딕셔너리 생성
    str1dict = {str1[i] : i for i in range(str1len)}
    cnt = [0 for i in range(str1len)]
    for i in str2:
        # str2의 문자가 str1에도 있는 문자이면 해당하는 index로 cnt에 +1씩 저장
        if i in str1:
            cnt[str1dict[i]] +=1
    maxnum =0
    # 가장 많이 나타난 수를 뽑음
    for i in cnt :
        if maxnum < i :
            maxnum = i
    return maxnum

for i in range(T):
    str1 = input()
    str2 = input()
    print(f'#{i+1} {solution(str1,str2)}')

