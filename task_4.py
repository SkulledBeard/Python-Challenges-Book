# primes_up_to(max_value) 

    
def primes_up_to(max_value):
    list_prime = []
    list_prime.extend(range(2,max_value + 1))
    
    for i in range(0, len(list_prime) + 1):
        for j in range (i + 1 , len(list_prime)):
            if list_prime[j] != 0:
                if list_prime[i] != 0:
                    if list_prime[j] % list_prime[i] == 0:
                        list_prime[j] = 0
                        
    final_list_prime = set(list_prime)
    final_list_prime.remove(0)
    print(sorted(final_list_prime))
    

if __name__ == "__main__":
    primes_up_to(int(input("Max number: ")))