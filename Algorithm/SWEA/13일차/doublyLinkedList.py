class Node:
    def __init__(self, pre, data, link):
        self.pre=pre
        self.data=data
        self.link=link

def addtoFirst(data):
    global Head
    Head = Node(None,data,Head)

def add(pre,data):
    if pre== None:
        print('error')
    else:
        pre.link=Node(pre.data,data,pre.link)

def addtoLast(data):
    global Head
    if Head==None:
        Head=Node(None,data,None)
    else:
        p=Head
        while p.link!=None:
            p=p.link
        p.link=Node(p.data,data,None)

def delete(pre):
    if pre==None or pre.link==None or pre.pre==None:
        print('error')
    else:
        pre.link.pre=pre.data
        pre.link=pre.link.link