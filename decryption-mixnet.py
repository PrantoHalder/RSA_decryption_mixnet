from random import randrange, random
import random
import math
_mrpt_num_trials = 5


def check_prime(n):
    assert n >= 2

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True


def public_private_key(p, q,n,r):
 number_of_mixserver = n
 for i in range(number_of_mixserver):
    if p == q:
        raise ValueError('p and q are equal!')
    if not check_prime(p):
        p = find_next_prime(p)
    if not check_prime(q):
        q = find_next_prime(q)

    print('p: ', p)
    print('q: ', q)
    print('r: ',r)
    # n = pq
    n = p * q
    print('n: ', n)
    phi = (p - 1) * (q - 1)
    e = 3
    g = gcd(e, phi)
    while g != 1:
        e = e + 1
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    print('e: ', e)
    print('d: ', d)
    print('phi: ', phi)

    return ((e, n), (d, n))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_m(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_m(b % a, a)
        return (g, x - (b // a) * y, y)


def multiplicative_inverse(a, m):
    g, x, y = gcd_m(a, m)
    if g != 1:
        raise Exception('Modular Inverse Does Not Exist')
    else:
        return x % m


def find_next_prime(number):
    """Return the next prime."""
    next_number = number + 1
    while not check_prime(next_number):
        next_number += 1
    return next_number


def encryption(m, pub_key, pri_key,r,n):
 number_of_mixserver = n
 for i in range(number_of_mixserver):
    e, n = pub_key[i]
    d, n = pri_key[i]
    R = r[i]
    print("m : ",m)
    print("e : ",e)
    print("d : ",d)
    print("r : ",R)
    print("n : ",n)
    m = m+R
    ciphertext = pow(m,e,n)
    print('Mixnet no : ',i+1," Encrypted data : ", ciphertext)
    m=ciphertext

 print("----------------------------------------")
 print("Final Cipher text : ",ciphertext)
 print("----------------------------------------")
 repr(ciphertext)
 b = int(input("If you want to decrypt press 1"))
 if b==1 :
    j = -1
    while j > -(number_of_mixserver+1):
        e, n = pub_key[j]
        d, n = pri_key[j]
        R = r[j]
        print("m : ", ciphertext)
        print("e : ", e)
        print("d : ", d)
        print("r : ", R)
        print("n : ", n)
        plaintext = pow(ciphertext,d,n)
        plaintext = int(plaintext - R)
        print('Decryption: Plaintext: ', plaintext)
        ciphertext = plaintext
        j = j-1
    print("##############################")
    print("Final Plaintext : ",plaintext)
 else :
     print(" Thank you ")
def randprime(N=10**40):
    p = 1
    while not is_prime(p):
        p = randrange(N)
    return p

def is_prime(n, k=6):
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True
pub_key = []
pri_key = []
random_string = []
if __name__ == '__main__':

 number_of_mixserver =int(input("enter the number of mixnet-router : "))
 for i in range(number_of_mixserver):
    p =randprime(2**200)
    q =randprime(2**200)
    r =randprime(2**200)
    public_key, private_key = public_private_key(p, q,number_of_mixserver,r)
    public_key = list(public_key)
    private_key = list(private_key)
    print("Public key is ", public_key)
    print("Private key is ", private_key)
    print("Random Srting is ",r)
    pub_key.append(public_key)
    pri_key.append(private_key)
    random_string.append(r)
 print("the list if public key ",pub_key)
 print("the list of private key ",pri_key)
 print("the list of random string ",random_string)
 print('Enter Message, M: ')
 m = int(input())
 print(m)
 encryption(m, pub_key, pri_key,random_string,number_of_mixserver)
