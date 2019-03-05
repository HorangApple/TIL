import sys
sys.stdin = open("input.txt","r")

switchCnt=int(input())
switch=[0]
switch+=list(map(int,input().split()))
studentCnt=int(input())
students=[]
for _ in range(studentCnt):
    students.append(list(map(int,input().split())))
result=switch[:]
for student in students:
    if student[0]==1:
        i=student[1]
        while i<=switchCnt:
            result[i]=result[i]^1
            i+=student[1]
    else:
        middle=student[1]
        i=0
        while middle-i>0 and middle+i<=switchCnt:
            if result[middle-i]==result[middle+i]:
                result[middle-i]=result[middle-i]^1
                if i!=0:
                    result[middle+i]=result[middle+i]^1
            else:
                break
            i+=1
result.pop(0)
i=0
while len(result):
    if len(result)!=0:
        print(result.pop(0),end=" ")
        i+=1
        if i>19:
            print()
            i=0