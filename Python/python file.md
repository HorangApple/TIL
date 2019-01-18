# 파일

변수와 가장 큰 차이점은 물리 저장 매체에 영구적으로 저장을 한다는 점이다.

```python
f =  open('a.txt','w')
f.write("wow this if file!"+"\n") # 쓰기, 기본적으로 줄바꿈은 없다.
f.close()
```

우리가 주로 자주쓰는 열기모드는 'a'이다. 'a'는 'append'의 약자이며 기존 파일 내용에 이여서 입력된다.

`f` 변수을 `dir`로 조사를 하면 다음을 사용할 수 있다.

```python
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
```

`read` 메서드를 이용해 파일의 내용을 읽어올 수 있다. 이때 열기모드를 'r'로 설정하고 나서 수행해야 한다.

```python
movies = ['말모이','랄프','짱구']
f =  open('a.txt','r')
print(f.read())
f.close()
```



```python
movies = ['말모이','랄프','짱구']
f =  open('movie.txt','a')
for movie in movies:
    f.write(movie+',')
f.close()
```

```python
f =  open('movie.txt','r')
print(f.read().split(","))
f.close()
```

```python
f =  open('movie.txt','r')
movies = f.read().split(",")
f.close()

print(movies[0])
```

csv는 엑셀과 비슷한데 콤마로 나누어진 데이터를 저장하는 확장자이다. 콤마로 사용하기에 데이터를 쉽게 다룰 수 있다.

```python
lunch = {
    '김밥카페':'02-1234-1234',
    '양자강':'02-2345-6803',
    '순남시레기':'02-2322-2324'
}

with open('lunch.csv','w') as f:
    for name in lunch:
        f.write(f'{name},{lunch[name]}\n')
        # f.write(", ".join([name,lunch[name]])+'\n')도 같다.

```
하지만 이렇게 적기엔 귀찮으니 `csv`모듈을 사용하자

```python
import csv

lunch = {
    '김밥카페':'02-1234-1234',
    '양자강':'02-2345-6803',
    '순남시레기':'02-2322-2324'
}
menu = ['김밥','탕수육','시레기']

# 리스트를 인자로 받는 방식
with open('lunch.csv','w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(menu) 
    
# 딕셔너리를 인자로 받는 방식
with open('lunch.csv','w') as f:
	field = ('상호명','전화번호')
    csv_writer = csv.DictWriter(f,fieldnames=field) # 파일 변수, 필드네임(튜플)을 인자로 받음
    csv_writer.writerow(lunch) 
