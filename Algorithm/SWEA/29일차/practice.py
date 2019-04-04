import sys
sys.stdin = open('input.txt','r')

def go(k,lenght,arr):
    if k==lenght:
        orders.append(arr)
    else:
        k+=1
        for i in range(2):
            go(k,lenght,arr+[i])

def solution():
    global maxi
    for order in orders:
        i=0
        while i<lenght:
            stair=stairs[order[i]]
            person[i]
            i+=1

TC = int(input())
for num in range(1,TC+1):
    n = int(input())
    mp=[list(map(int,input().split())) for _ in range(n)]
    stairs = []
    person = []
    orders = []
    for i in range(n):
        for j in range(n):
            if mp[i][j]==1:
                person.append([i,j])
            elif mp[i][j]>1:
                stairs.append([i,j])
    lenght=len(person)
    go(0,lenght,[])
    solution()
    # i=0
    # while i<len(person):
    #     mini=9999
    #     for j in stairs:
    #         time=abs(person[i][0]-j[0]) + abs(person[i][1]-j[1])
    #         person[i]+=[time]
    #     i+=1
    # # person=[위치 y, x, stair1시간, stair2시간]
    # print(person)