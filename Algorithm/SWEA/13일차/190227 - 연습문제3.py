class Node:
    def __init__(self, data, link):
        self.data=data
        self.link=link

def addtoFirst(data):
    global Head
    Head = Node(data,None)

def add(pre,data):
    if pre== None:
        print('error')
    else:
        node=pre
        while node:
            if data>=node.data and (data<node.link.data if node.link else True):
                save=node.link
                node.link=Node(data,node.link)
                node.link.link=save
                break
            node=node.link

def insert(head):
    node=head
    while node:
        print(node.data)
        node=node.link

line = [1,5,2,4,3]
addtoFirst(line[0])
for i in line[1:]:
    add(Head,i)
insert(Head)
        
