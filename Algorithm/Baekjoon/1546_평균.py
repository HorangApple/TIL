n = int(input())
lists = list(map(int, input().split()))

def fakeAverage (n, lists):
        total = 0
        maximum = max(lists)

        for i in lists :
                total += i/maximum*100

        average = total/len(lists)

        return average
print('{:0.2f}'.format(fakeAverage(n,lists)))