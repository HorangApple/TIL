import csv

lunch = {
    '김밥카페':'02-1234-1234',
    '양자강':'02-2345-6803',
    '순남시레기':'02-2322-2324'
}

lunch2 = [
    {
        '상호명':'양자강',
        '전화번호':'02-2345-6803'
    },
    {
        '상호명':'김밥카페',
        '전화번호':'02-1234-1234'
    },
    {
        '상호명':'순남시레기',
        '전화번호':'02-2322-2324'
    }
]

menu = ['김밥','탕수육','시레기']

# # 리스트를 인자로 받는 방식
# with open('lunch.csv','w') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(menu)

# 딕셔너리를 인자로 받는 방식
with open('lunch.csv','w', newline="") as f: # 윈도우에서는 newline을 매개변수로 보내야 개행이 이루어지지 않는다.
    field = ('상호명','전화번호')
    csv_writer = csv.DictWriter(f,fieldnames=field) 
    # 파일 변수, 필드네임(튜플)을 인자로 받음
    csv_writer.writeheader() # fieldnames도 파일에 저장
    for l in lunch2:
        csv_writer.writerow(l) # 딕셔너리 값 입력

# with open('lunch.csv',newline='\n') as f: # 
#     reader = csv.reader(f)
#     for row in reader :
#         print(row)