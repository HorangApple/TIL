# class Q:
#     def newNode(self,count):
#         self.num=count
#         self.candy=1
#     def 
i=20
count=1
que=[[1,1]]
save=[]
print(f'{que[0][0]}번 학생 : 입장하여 줄을 선다.')
print(f'학생 줄: {que}')
while i>0:
    if i<20:
        # 다시들어온다
        print(f'==>{save[0]}번 학생 : 다시 줄을 선다.')
        que.append(save)
        print(f'학생 줄: {que}')
        count+=1
        # 추가
        print(f'{count}번 학생 : 입장하여 줄을 선다.')
        que.append([count,1])
        print(f'학생 줄: {que}')
    # 받고간다
    print(f'{que[0][0]}번 학생 : 줄에서 나와...')
    i-= que[0][1]
    que[0][1]+=1
    save=que.pop(0)
    print(f'학생 줄: {que}')
    print(f'{save[0]}번 학생 : 선생님한테 사탕 {(save[1]-1) if i>0 else i+(save[1]-1)}개를 받는다.')
    print(f'===== 남은 사탕의 개수는 {0 if i<0 else i}개다.')
    print("")