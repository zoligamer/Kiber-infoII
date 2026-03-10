import random


def dice():
    dobas=random.randint(1,6)






if __name__ == "__main__":
    numbers= {1:0,2:0,3:0,4:0,5:0,6:0}
    for _ in range(100):
        n = dice()
        numbers[n]+=1
    print(numbers)