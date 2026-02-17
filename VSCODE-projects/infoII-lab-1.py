import time, random

def is_prime(number: int) -> bool: ## 
    if not isinstance(number, int):
        return False
    
    if number < 2:
        return False
    for divider in range(2,number):
        print(divider)
        if number% divider == 0:
            return False                                                   # % maradekos osztas
    return True






if __name__ == "__main__":      ### Másik python script hivatkozás, ha más importálja, nem fut le az IF ben lévő kód. csak ha az fő fájlból indul.
    var_int = (1)           # Integer szám deklarálás
    var_float = (1.0)       # Float lebegőpontos szám deklarálás
    result = 4 // 3         # Egész osztás // használata        integerre konvertál / az marad


    ####

    print(type(var_float))      # Típus, class kiíratása.
    print(type(var_int))        
    print(type(4/2))            # tört ösztás / float-ra konvertál
    print("Result", type(result), result, end="")       # 
    print("!")

    """
    prompt = "Steps"
    print(prompt)

    for i in range(2):  #ismétlés
        print("\r", end="")
        print(i, end="")
        time.sleep(1)
    print
    print(type(prompt))

    """

    numbers = [1,2,3,4,15]      #lista

    print(numbers)

    numbers.append(16)      #tömb/lista bővítés
    print(type(numbers))



    """
    items = {'a':1, 'b':2}      # szótár

    print(items)
    print(type(items))
    print(items('b'))
    
    """
    elements = {'asd', 1, 1.3}

    print(elements)
    print(type(elements))



    #############x FÜGGVÉNYEK ############

print(is_prime)
print(is_prime("asef"))
print(is_prime(23))
print(is_prime(100))
    