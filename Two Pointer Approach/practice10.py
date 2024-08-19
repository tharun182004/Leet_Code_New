                                        #Medium

'''
Given a number N, calculate the prime numbers up to N using Sieve of Eratosthenes.  

Example 1:
Input:
N = 10
Output:
2 3 5 7

Explanation:
Prime numbers less than equal to N 
are 2 3 5 and 7.
'''

def func(N):
    is_prime=[True]*(N+1)

    is_prime[0]=is_prime[1]=False
    p=2

    while p*p<=N:
        if is_prime[p]==True:
            for i in range(p*p,N+1,p):
                is_prime[i]=False
        p+=1

    primes=[p for p in range(2,N+1) if is_prime[p]]
    return primes



N=25
print(func(N))



