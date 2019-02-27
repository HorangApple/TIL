class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link

def addtoFirst(data):
    global Head
    Head = Node(data,Head)

def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(data,pre.link)

def addtoLast(data):
    global Head
    if Head==None:
        Head=Node(data,None)
    else:
        p=Head
        while p.link!=None:
            p=p.link
        p.link=Node(data,None)

def delete(pre):
    if pre==None or pre.link==None:
        print('error')
    else:
        pre.link=pre.link.link