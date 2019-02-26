import sys
sys.stdin = open("input.txt","r")

def solution(start,length):
    que=[start]
    visited=[False]*length
    # 깊이를 인덱스로 삼아 같은 깊이끼리 노드 저장
    deepList=[[] for _ in range(50)]
    while que:
        # 출발지와 깊이를 초기화
        go,deep=que.pop(0)
        nextNod=[] # 다음 깊이의 노드 리스트
        for i in mp[go]:
            # 0보다 크고 방문하지 못한 곳, 큐에 없는 곳(중복 방지)만 추가
            if i>0 and not visited[i] and i not in que:
                que.append([i,deep+1])
                nextNod.append(i)
        # 다음에 갈 곳이 없고 방문하지 않았던 곳을 추가
        if 0==len(nextNod) and not visited[go] :
            deepList[deep+1].append(go)
        # 방문한 것을 표시
        visited[go]=True
    return deepList          

TC=10
for num in range(1,TC+1):
    length,start=map(int,input().split())
    inp=list(map(int,input().split()))
    mp=[[0]*length for _ in range(length)]
    for i in range(len(inp)//2):
        mp[inp[2*i]][inp[2*i+1]]=inp[2*i+1]
    result=solution([start,0],length)
    # []과 함께 요소가 존재하는 result에서 마지막 리스트만 추출
    for i in range(49,-1,-1):
        if result[i]!=[]:
            result=result[i]
            break
    # 그 마지막 리스트의 최대값만 출력
    print(f'#{num} {max(result)}')