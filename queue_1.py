def qinput(item, queue):
    queue.append(item)

def qoutput(queue):
    queue.pop(0)

q = []
qinput(1, q)
qinput(2, q)
qinput(3, q)
qoutput(q)
qinput(4, q)
print(q)
