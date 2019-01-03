import requests
import json
import time

def get_total_info() :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date':'2018/12/21'
    }
    
    response = requests.get(url, params=params).text
    document = json.loads(response)
    # area = ['홍대1호점','홍대2호점','강남1호점','강남2호점','인천 부평점','부산 서면점']
    
    # lists=[]
    
    # for i in area :
    #     for j in range(len(document['bookList'])):
    #         if(document['bookList'][j]['branch']==i) :
    #             li={
    #                 'area' : i,
    #                 'time' : document['bookList'][j]['hour'],
    #                 'room' : document['bookList'][j]['room'],
    #                 'reservation' : document['bookList'][j]['booked'] #예약완료이면 true
    #             }
    #             lists.append(li)
            
    # print(lists[0]['area'])
    
    cafe_code = {
        '홍대1호점':1,
        '홍대2호점':10,
        '강남1호점':3,
        '강남2호점':11,
        '인천 부평점':4,
        '부산 서면점':5
    }
    total = {}
    game_room_list = document["gameRoomList"] # 기본 틀 잡기
    for cafe in cafe_code :
        total[cafe] = []
        for room in game_room_list:
            if(cafe_code[cafe] == room["branch_id"]) :
                total[cafe].append({"title":room["room_name"], "info" :[]})
    
    print(total)
    book_list = document["bookList"] # 앞에서 만든 틀에 데이터 집어넣기
    for cafe in total :
        print(cafe)
        for book in book_list:
            if(cafe==book["branch"]):
                for theme in total[cafe]:
                    if(theme["title"]==book["room"]) :
                        if(book["booked"]):
                            booked = "예약완료"
                        else:
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"],booked))
    return total
    
def seoul_escape_list() :
    total = get_total_info()
    return total.keys()

def seoul_escape_info(cd) :
    total = get_total_info()
    cafe = total[cd]
    tmp = []
    for theme in cafe :
        tmp.append("{}\n {}".format(theme["title"], '\n'.join(theme["info"])))
    return tmp
    
