def solution(num,triangle):
    n=int((num/3)//2)
    if n==0 :
        return triangle
    else :
        triangle=solution(num//2,triangle)
    for i in range(num//2):
        triangle.append(triangle[i]+" "+triangle[i])
        triangle[i]=" "*(num//2)+triangle[i]+" "*(num//2)
    return triangle
        
triangle=["  *  "," * * ","*****"]# 각각 " "*n+triangle+triangle+" "*(num-1-2*줄수)+triangle
num = int(input())
for i in solution(num,triangle):
    print(i)


# 어떤 입력이 주어지는지 확인하고 문제를 풀어야 한다.
# 나는 입력이 3*2^k가 아닌 정수를 받아 그 수만큼 출력하는 줄 알고 풀었다. 덕분에 많은 시간을 소요했다.
# 그 개고생이 바로 밑의 코드이다.

# def triangle (n, k, spacestart, nextspace):
#     if n!=1 :
#         spacestart, nextspace = triangle (n-1,k,spacestart,nextspace)
#     array=[1,2,2,4]

#     if n == spacestart :
#         spacestart = 2*(spacestart-1)+1
#         nextspace = spacestart-2
#     else :
#         nextspace-=2

#     # if (n+2)%3 == 0 :
#     #     f.write((" "*(k-n))+("*"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
#     # elif (n+1)%3 == 0 :
#     #     f.write((" "*(k-n))+("* *"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
#     # elif n%3 ==0 :
#     #     f.write((" "*(k-n))+("*****"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
#     print(" "*(k-n), end=" ")
#     quarter=(n-1)//12+1
#     if (n+2)%3 == 0 :
#         for i in range(quarter):
#             print(("*"+" "*(nextspace if quarter%2!=0 or n<=12 else nextspace-12*(quarter-1)))*array[((n-1)//3)%4],end="")
#         print("")
#     elif (n+1)%3 == 0 :
#         for i in range(quarter):
#             print(("* *"+" "*nextspace)*array[((n-1)//3)%4],end="")
#         print("")
#     elif n%3 ==0 :
#         for i in range(quarter):
#             print(("*****"+" "*nextspace)*array[((n-1)//3)%4],end="")
#         print("")
#     return (spacestart,nextspace)

# n = int(input())
# # f = open("output.txt", 'w')
# # triangle(n,n,4,-1,f)
# # f.close()
# triangle(n,n,4,-1)
