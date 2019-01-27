def triangle (n, k, spacestart, nextspace):
    if n!=1 :
        spacestart, nextspace = triangle (n-1,k,spacestart,nextspace)
    array=[1,2,2,4]

    if n == spacestart :
        spacestart = 2*(spacestart-1)+1
        nextspace = spacestart-2
    else :
        nextspace-=2

    # if (n+2)%3 == 0 :
    #     f.write((" "*(k-n))+("*"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
    # elif (n+1)%3 == 0 :
    #     f.write((" "*(k-n))+("* *"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
    # elif n%3 ==0 :
    #     f.write((" "*(k-n))+("*****"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4]+"\n")
    print(" "*(k-n), end=" ")
    quarter=(n-1)//12+1
    if (n+2)%3 == 0 :
        for i in range(quarter):
            print(("*"+" "*(nextspace if quarter%2!=0 or n<=12 else nextspace-12*(quarter-1)))*array[((n-1)//3)%4],end="")
        print("")
    elif (n+1)%3 == 0 :
        for i in range(quarter):
            print(("* *"+" "*nextspace)*array[((n-1)//3)%4],end="")
        print("")
    elif n%3 ==0 :
        for i in range(quarter):
            print(("*****"+" "*nextspace)*array[((n-1)//3)%4],end="")
        print("")
    return (spacestart,nextspace)

n = int(input())
# f = open("output.txt", 'w')
# triangle(n,n,4,-1,f)
# f.close()
triangle(n,n,4,-1)
# #####* 5
# ####* *
# ###*****
# ##*#####* 2
# #* *###* *  
# ***** *****
