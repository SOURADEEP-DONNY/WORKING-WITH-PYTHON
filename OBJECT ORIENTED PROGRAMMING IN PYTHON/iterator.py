class ITERATOR:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):

        if self.num<=10:
            val=self.num
            self.num=self.num+1
            return val
        else:
            raise StopIteration
values=ITERATOR()
for i in values:
    print(i)
