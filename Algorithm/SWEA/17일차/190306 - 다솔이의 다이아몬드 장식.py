import sys
sys.stdin = open("input.txt","r")

TC=int(input())
for num in range(1,TC+1):
    char=input()
    length=len(char)
    a=(5+4*(length-1))
    mp = ["" for _ in range(5)]
    for i in range(5):
        if i==0:
            mp[i]+="..#.."
        elif i==1:
            mp[i]+=".#.#."
        elif i==2:
            mp[i]+="#.{}.#".format(char[0])
        elif i==3:
            mp[i]+=".#.#."
        elif i==4:
            mp[i]+="..#.."

    if length>1:
        for j in char[1:]:
            for i in range(5):
                if i == 0:
                    mp[i] += ".#.."
                elif i == 1:
                    mp[i] += "#.#."
                elif i == 2:
                    mp[i] += ".{}.#".format(j)
                elif i == 3:
                    mp[i] += "#.#."
                elif i == 4:
                    mp[i] += ".#.."

    for i in mp:
        print(i)