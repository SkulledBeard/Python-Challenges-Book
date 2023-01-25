# primenumberpairs => 2 twin, 4 cousin, 6 sexy => isPrime(n) && isPrime(n + 2)

    
def primes_up_to(max_value):
    numbers = set(range(max_value, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, max_value+1, p)))
        
    twin : dict = {}
    cousin : dict = {}
    sexy : dict = {}
    
    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            if (primes[j] - primes[i]) == 2:
                twin[primes[i]] = primes[j]
                
            if (primes[j] - primes[i]) == 4:
                cousin[primes[i]] = primes[j]
                
            if (primes[j] - primes[i]) == 6:
                sexy[primes[i]] = primes[j]
    
    print("Twin:   " , twin)
    print("Cousin: " , cousin)
    print("Sexy:   " , sexy)
    

if __name__ == "__main__":
    primes_up_to(int(input("Max number: ")))