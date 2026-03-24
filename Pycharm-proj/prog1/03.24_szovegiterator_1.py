def prim(n):
    if n <2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def prim_steve():
    num=2
    while True:
        if prim(num):
            yield num
        num+=1