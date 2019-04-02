import sys
sys.stdin = open('input.txt','r')


TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    inp = list(map(int,input().split()))
    line = [-1]*(sum(inp)+1)
    line[0] = 0
    for i in inp:
        temp = line[:]
        print(temp)
        for j in temp:
            if j>=0:
                line[j+i]=j+i
        print(line)

    cnt=0
    for i in line:
        if i>-1:
            cnt+=1
    print(f'#{num}',cnt)

# 같은 크기의 리스트를 하나 더 만들어서 그걸 이용해 값을 계산하고 풀어나간다.