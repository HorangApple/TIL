import sys
sys.stdin=open('input.txt','r')

def go(k,lenght,arr):
    if k==lenght:
        orders.append(arr)
    else:
        k+=1
        for i in range(2):
            if i==1:
                go(k,lenght,arr+[k-1])
            else:
                go(k,lenght,arr)
 
def detect(mp):
    for x in range(w):
        one=[]
        for y in range(d):
            if not one:
                one+=[mp[y][x]]
                continue
            else:
                if one[-1]!=mp[y][x]:
                    one=[mp[y][x]]
                else:
                    one+=[mp[y][x]]
                    if len(one)==k:
                        break
        else:
            return False
    else:
        return True
 
def loop(dp,length,order,mp):
    global answer
    if answer>-1:
        pass
    elif dp==length:
        if detect(mp):
            answer=length
    else:
        dp+=1
        for j in range(2):
            i=0
            while i<w:
                mp[order[dp-1]][i]=j
                i+=1
            loop(dp,length,order,mp)
 
def solution(mp):
    for order in orders:
        save=[]
        for i in order:
            save.append(mp[i][:])
        loop(0,len(order),order,mp)
        i=0
        while i<len(order):
            mp[order[i]]=save[i]
            i+=1
        if answer > -1:
            break
         
TC = int(input())
for num in range(1,TC+1):
    d,w,k= map(int,input().split())
    mp=[list(map(int,input().split())) for _ in range(d)]
    # 0은 A, 1은 B
    orders=[]
    answer=-1
    if k!=1:
        go(0,d,[])
        orders=sorted(orders,key=lambda x:len(x))
        solution(mp)
    else:
        answer=0
    print(f'#{num}',answer)