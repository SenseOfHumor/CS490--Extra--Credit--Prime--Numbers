import sys
import string


def n_prime_numbers(n: int) -> list[int]:
    """
    Finds prime numbers ranging from 1 to n.
    
    Extended description of function:
    Uses nested loops to find n number of prime numbers starting from 2 by
    dividing a number by all the numbers before it to verify that n is a prime.

    Returns: list
    """
    prime_list = []
    j = 2
    while True:
        prime_flag = True

        for k in range (2, j):
            if j%k == 0:
                prime_flag = False
                break
        if prime_flag: prime_list.append(j)

        if len(prime_list) == n: break
            
        j += 1
    return prime_list

    
def main():
    if len(sys.argv)>1:
        user_input = (sys.argv[1])        
    else:
        print("No values were entered through command line.")
        user_input = (input("Please enter a positivethe number of primes to print: "))
    if  user_input.isdigit() and int(user_input) > 0:
        print(n_prime_numbers(int(user_input)))
    else: print("Invalid Input")

if __name__ == "__main__":
    main()
