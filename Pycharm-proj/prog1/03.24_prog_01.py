class EvenNumbers:
    def __init__(self,start,end):
        self.current=start
        self.end=end
        if self.current%2!=0:
            self.current+=1

    def __iter__(self):
        return self


    def __next__(self):
        if self.current>self.end:
            raise StopIteration
        value=self.current
        self.current+=2
        return value


for x in EvenNumbers(5,20):
    print(x)
