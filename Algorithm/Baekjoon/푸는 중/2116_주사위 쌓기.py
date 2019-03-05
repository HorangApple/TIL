import sys
sys.stdin = open("input.txt","r")

def solution(top,total,num):
    while True:
        if num==diceCnt:
            return total
        temp=[]
        for i in dices[num]:
            if top in i:
                if top==i[0]:
                    top=i[1]
                else:
                    top=i[0]
            else:
                temp+=i
        total+=max(temp)
        num+=1
    
diceCnt=int(input())
dices=[]
result=[]
for _ in range(diceCnt):
    dice=list(map(int,input().split()))
    dice=[[dice[0],dice[5]],[dice[1],dice[3]],[dice[2],dice[4]]]
    dices.append(dice)
for i in range(3):
    total=[]
    surface=dices[0][i]
    for j in dices[0]:
        if j !=surface:
            total+=j
    total=max(total)
    result.append(solution(surface[0],total,1))
    result.append(solution(surface[1],total,1))
print(max(result))

# 재귀로 하면 최대깊이까지 도달해 런타임 에러가 뜬다