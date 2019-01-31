import sys
sys.stdin = open("input.txt","r")

T = int(input())

def search(str1,str2):
    str1len = len(str1)
    str2len = len(str2)

    for i in range(str2len-str1len+1) :
        for j in range(str1len) :
            if str2[i+j]!=str1[j]:
                break
        else:
            return 1
    return 0

for i in range(T):
    str1 = input()
    str2 = input()

    print(f'#{i+1} {search(str1,str2)}')

