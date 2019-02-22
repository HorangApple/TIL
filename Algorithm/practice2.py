import sys
sys.stdin = open("input.txt","r")

t=input()
w=input()

def fail(w):
    output=[0]
    check=0
    for i in range(1,len(w)):
        part=w[:i]
        count=0
        for j in range(len(part)-1):
            if part[0:j+1]==part[-1-j:]:
                count=len(part[0:j+1])
                check=1
            elif check==0 and not output[i-1]:
                break
            else:
                check=0
        output.append(count)
    return output

def solution(t,w):
    i=0
    start=[]
    count=0
    while i<len(t):
        j=0
        while j<len(w):
            if t[i+j]!=w[j]:
                if j==0:
                    i+=1
                    break
                elif move[j]==0:
                    i+=j
                    break
                else :
                    i=i+j-move[j]
                    break
            j+=1
        else:
            start.append(i+1)
            i+=j
            count+=1
    return [count,start]

move=[]
move=fail(w)
result=solution(t,w)
print(result[0])
for i in result[1]:
    print(i)