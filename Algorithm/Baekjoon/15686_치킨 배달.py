import sys
sys.stdin = open("test.txt", "r")

import itertools
n,m = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(n)]
houses = []
stores = []
storesCnt = len(stores)

for i in range(n):
    for j in range(n):
        if mp[i][j] == 1:
            houses.append([i,j])
        elif mp[i][j] == 2:
            stores.append([i,j])

def sol():
    resultMini = 9999999999
    for case in itertools.combinations(stores,m):
        total = 0
        for house in houses:
            mini = 99999999999
            for store in case:
                length = abs(house[0]-store[0]) + abs(house[1]-store[1])
                if mini>length:
                    mini=length
            total+=mini

        if resultMini > total:
            resultMini = total
    print(resultMini)

sol()