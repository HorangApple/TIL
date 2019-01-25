def triangle (n, k, spacestart, nextspace):
    if n!=1 :
        spacestart, nextspace = triangle (n-1,k,spacestart,nextspace)
    array=[1,2,2,4]

    if n == spacestart :
        spacestart = 2*(spacestart-1)+1
        nextspace = spacestart-2
    else :
        nextspace-=2

    if (n+2)%3 == 0 :
        print((" "*(k-n))+("*"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4])
    elif (n+1)%3 == 0 :
        print((" "*(k-n))+("* *"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4])
    elif n%3 ==0 :
        print((" "*(k-n))+("*****"+" "*nextspace)*((n-1)//12+1)*array[((n-1)//3)%4])

    return (spacestart,nextspace)

n = int(input())

triangle(n,n,4,-1)


# #####* 5
# ####* *
# ###*****
# ##*#####* 2
# #* *###* *  
# ***** *****
