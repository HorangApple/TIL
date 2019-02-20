import sys
sys.stdin = open("input.txt","r")

for num in range(1,11):
    length=int(input())
    nsMap=[input() for _ in range(length)]
    count=0
    for i in range(length):
        before=0
        for j in range(length):
            if nsMap[j][2*i]=='1':
                before=1
            elif nsMap[j][2*i]=='2' and before==1:
                before=0
                count+=1
    print(f'#{num} {count}')

# split을 사용하는데도 속도에 영향이 미친다