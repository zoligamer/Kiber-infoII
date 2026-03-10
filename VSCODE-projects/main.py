import random, sys



##plot: olyan kód ami roulette, és emegkérdi lősz, vagy skippelsz?
def sixshot():

    tries=6
    while tries>0:
        loves=int(input("Shoot Yourself or SKIP?: [1 or 2]"))
        numbers = random.randint(0, 1)
        print("Tries left: ", tries)
        if loves==1:
            print("You pulled the trigger!")
            if numbers == 1:
                tries==0
                print("You died brave.")
                print("Want another round?", ["Y", "N"])
                yesno = str(input())
                if yesno ==  "y" or "Y":
                    sixshot()
                elif yesno =="n" or "N":
                    print("Exit game")
                    sys.exit()
            else:
                tries-=1
                print("You live! Next round")
                continue
        else:
            print("You Coward! Get back into the game")



if __name__ == "__main__":
    sixshot()