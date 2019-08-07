# movies = ['말모이','랄프','짱구']
# f =  open('movie.txt','w')
# for movie in movies:
#     f.write(movie+',')
# f.close()


f =  open('movie.txt','r')
movies = f.read().split(",")
f.close()

print(movies[0])