def push(i):
    global top
    top=Node(i,top)

def pop():
    global top
    if top==None:
        print("error")
    else:
        data=top.data
        top=top.link
        return data