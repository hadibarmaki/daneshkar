class MyRange:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 2
        if self.a >= self.b:
            raise StopIteration
        return self.a


mr = MyRange(1, 23)
for i in mr:
    print(i)        
    