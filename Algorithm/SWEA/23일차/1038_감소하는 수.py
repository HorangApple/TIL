import sys
sys.stdin = open('input.txt','r')

def solution(n,cnt,length,target):
    one=[]
    for i in range(length):
        for j in range(10):
            if int(target[i][-1])>j:
                value = target[i]+str(j)
                one.append(value)
                if cnt == n :
                    return value
                cnt+=1
            else:
                break
    return solution(n,cnt,len(one),one)


n= int(input())
target=['0','1','2','3','4','5','6','7','8','9']
if n<10:
    print(n)
elif n>1022:
    print(-1)
else:
    print(solution(n,10,10,target))
    
