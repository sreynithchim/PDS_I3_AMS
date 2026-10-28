"""(a) Write is_prime(n). A prime is a whole number ≥ 2 whose only divisors are 1 and itself. For
speed, only test divisors d while d * d <= n."""
def is_prime(n):
    if n <2:
        return False
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True

"""(b) Print all primes below 50 on one line (use print(..., end=" ")), then count the primes below
100."""
for n in range(2,50):
    if is_prime(n):
        print(n,end=" ")
        
print()

count=0
for n in range(2,100):
    if is_prime(n):
        count+=1
print("Total prime numbers between 2 and 100:", count)
        
"""(c) Goldbach's conjecture says every even number ≥ 4 is the sum of two primes. Write
goldbach(n) that returns the first pair (p, q) with p + q == n, and print the pairs for 4, 6, …,
30."""
def goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)
    return None

for n in range(4, 31, 2):
    p,q=goldbach(n)
    print(f"{n} = {p} + {q}")
    
"""(d) Use a loop with break to check the conjecture for every even number from 4 to 10,000."""
holds=True
for n in range(4,10000):
    if goldbach(n) is None:
        holds=False
        break

print("Goldbach holds for every even number from 4 to 10000:", holds)