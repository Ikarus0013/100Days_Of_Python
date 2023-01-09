
def prime_checker(number):
    # if number % 2 == 0:
    #     print("It is not a Prime Number")

    # else:
    #     print("It is a Prime Number")
    
    for i in range(2, number):
        is_prime = True
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a Prime Number")
    else:
        print("it is not a prime number")

n = int(input("Check this Number: "))
prime_checker(number=n)
