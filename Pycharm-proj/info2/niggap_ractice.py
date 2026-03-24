import random
from typing import Protocol

class GetNumberProtocol(Protocol):
    def get_number(self)->float:
        ...
    def __next__(self)->float:
        ...
    def __iter__(self)->float:
        ...



class RandomNumber(GetNumberProtocol):
    def get_number(self) ->float:
        return random.random()
    def __next__(self)->float:
        return self.get_number()

class EvenNumber(GetNumberProtocol):
    def __init__(self,max=None):
        self.max=max
        self.actual=0
    def get_number(self) ->float:
        self.actual+=2
        if self.max is not None and self.actual > self.max:
            raise StopIteration
        return float(self.actual)
    def __next__(self)->float:
        return self.get_number()
    def __iter__(self)->float:
        return self

class FileNumbers(GetNumberProtocol):
    def __init__(self,filename:str):
        self.filename=filename
        self.numbers=[]
        self.actual_index=0
        with open(self.filename,"r",encoding="utf-8") as f:
            text=f.read()
            lines=text.split("\n")
            for line in lines:
                token=line.split(",")
                for t in token:
                    self.numbers.append(float(t))


    def get_number(self) ->float:
        if self.actual_index>=len(self.numbers):
            raise StopIteration
        actual=self.numbers[self.actual_index]
        self.actual_index+=1
        return actual

    def __next__(self)->float:
        return self.get_number()
    def __iter__(self):
        return self