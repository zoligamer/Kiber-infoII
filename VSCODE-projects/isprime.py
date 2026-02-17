def is_prime(number: int) -> bool: ## 
    if not isinstance(number, int):
        return None
    
    if number < 2:
        return False
    for divider in range(2,number):
        print(divider)
        if number% divider == 0:
            return False                                                   # % maradekos osztas
    return True






print(is_prime)
print(is_prime("asef"))
print(is_prime(23))
print(is_prime(100))
    