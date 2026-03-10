import random


class Kor:
    def __init__(self,sugar,kozeppont):
        self.sugar = sugar
        self.kozeppont = kozeppont
    def terulet(self):
        return self.sugar*pow(3.14,2)
    def kerulet(self):
        return self.sugar*2*3.14
kor_adatai_01 = Kor(2,(2,5))
kor_adatai_02 = Kor(2,(3,7))
print(kor_adatai_01.terulet())
print(kor_adatai_02.sugar)

korok =[]
for z in range(5):
    kor = Kor(random.randint(1,10)),random.randint(1,10)
    