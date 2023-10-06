def is_prime(n):
    if n in primes:
        prime = True
    else:
        for i in primes:
            if n % i == 0:
                prime = False
                break
        else:
            for i in range(primes[-1]+2, n): #int(n**0.5)+1, 2):
                if is_prime(i):
                    if n % i == 0:
                        prime = False
                        break
            else:
                prime = True
                primes.append(n)
                #print('new prime:', n)
    return prime
	
def prime_factors(n):
    factors = []
    #if not is_prime(n):
    for i in primes:
        while n % i == 0:
            factors.append(i)
            n = n // i
            print(factors, n)
        if n == 1:
            break
    for i in range(primes[-1]+2, n+1, 2): #int(n/2)+1):
        if is_prime(i):
            #print(n,i)#(str(n) + '/' + str(i) + ' = ' + str(n/i))
            while n % i == 0:
                factors.append(i)
                n = n // i
                print(factors, n)
        if n == 1:
            break
    return factors

def get_factors(n):
    factors = []
    i = 2
    #print(n)
    while n > 1:
        while n % i == 0:
            n = n // i
            factors.append(i)
            #print(factors, n)
        i += 1
    return factors
		
primes = [2, 3]
#n = 600851475143
n = int(input("Introduzca un número: "))
#factors = prime_factors(n)
#factors = get_factors(n)
for i in range(2, n):
    is_prime(i)

print(primes)
