def backtrack(a,k,inp,result,total):
    c=[False]*2
    if k==inp:
        print(result)
        results.append(result)
    else:
        k+=1
        ncandidates=construct_candidates(c)
        for i in range(ncandidates):
            if c[i]:
                result.append(a[k])
                total+=a[k]
            else:
                result.pop()
            backtrack(a,k,inp,result,total)


def construct_candidates(c):
    c[0]=True
    c[1]=False
    return 2
a=[1,2,3,4,5,6,7,8,9,10]
result=[]
results=[]
backtrack(a,-1,9,result,0)
print(len(results))

# def partition (a, begin,end):
#     pivot = (begin+end)//2
#     l=begin
#     r=end
#     while l<r:
#         while(a[l]<a[pivot] and l<r):l+=1
#         while(a[r]>=a[pivot] and l<r):r-=1
#         if l<r:
#             if l==pivot:pivot=r
#             a[l],a[r]=a[r],a[l]
#     a[pivot],a[r]=a[r],a[pivot]
#     return r

# def quickSort(a,begin,end):
#     if begin<end:
#         p=partition (a,begin,end)
#         quickSort(a,begin,p-1)
#         quickSort(a,p+1,end)
# a=[69,10,30,2,16,8,31,22]
# quickSort(a,0,7)
# print(a)