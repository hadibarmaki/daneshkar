#!/usr/bin/python3
def sinpput(item, stack):
    stack.append(item)

def soutput(stack):
    stack.pop()


s = []
sinpput(1, s)
sinpput(2, s)
sinpput(3, s) 
soutput(s)
sinpput(4, s) 
print(s)      