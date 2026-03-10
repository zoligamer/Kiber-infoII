import random
import sys

from sepolgen.classperms import result


def start_game(max_num = 100, remaining_attempt = 8, prompt="Melyik szám?: "):
    print("hello")
    print("Gondoltam egy szamra találd ki.")

    num = random.randint(1,max_num)
    while remaining_attempt > 0:
        print(prompt, end="")
        str_num = input()
        t = int(str_num)
        if t == num:
            print("nyertél")
            return True
        else:
            if t>num:
                print("kisebb")
            else:
                print("Nagyobb")
        remaining_attempt -= 1
    print("vesztettél.")
    return False



def select(label,menu):
    print(label)
    for item in menu:
        print(f" -{menu.index(item)}: {item}")



def get_int(prompt = "> ", min=0, max=None):
    while True:
        result=input(prompt).strip()
        if result=="exit":
            sys.exit(0)
        try:
            value = int(result)
            if value < min:
                print(f"A szám nem lehet kisebb mint {min}!")
                continue
            if max is not None:
                if value > max:
                    print(f"A szám nem lehet nagyobb mint {max}!")
                    continue
            return value
        except:
            print("nem érvényes szám")
            continue



if __name__ == "__main__":
    print("hello")
    while True:
        start_game(remaining_attempt=5)
        result = select("szeretnél még játszani?", ["igen","nem"])
        if result ==1:
            sys.exit(0)