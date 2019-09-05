import sys
sys.stdin = open("test.txt", "r")

n = int(input())
nums =  list((map(int,input().split())))
com =list(map(int,input().split()))

mini = 99999999999999999999999999999999999999999999999999999999999
maxi = -99999999999999999999999999999999999999999999999999999999999

def sol(com, nums,result,test):
    global maxi, mini
    if len(nums) == 0:
        # print(test)
        if maxi<result:
            maxi = result
        if mini>result:
            mini = result
    else:
        next = nums[0]
        save = result
        if com[0] > 0:
            result+=next
            com[0]-=1
            sol(com,nums[1:],result,test+['+'])
            com[0] += 1
            result = save
        if com[1] > 0:
            result-=next
            com[1]-=1
            sol(com,nums[1:],result,test+['-'])
            com[1] += 1
            result = save
        if com[2] > 0:
            result*=next
            com[2]-=1
            sol(com,nums[1:],result,test+['*'])
            com[2] += 1
            result = save
        if com[3] > 0:
            if result>=0:
                result//=next
            else:
                result = -(-result//next)
            com[3]-=1
            sol(com,nums[1:],result,test+['//'])
            com[3] += 1
            result = save

k = nums[0]
sol(com,nums[1:],k,[])
print(maxi)
print(mini)