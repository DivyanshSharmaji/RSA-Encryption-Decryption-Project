import random
import math

def is_prime(number):
    if number<2:
        return False
    
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    else:
        return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e)%phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

def get_keys():
    # STEP-1
    p,q = generate_prime(1000, 5000), generate_prime(1000, 5000)
    while p==q:
        q = generate_prime(1000, 5000)

    # STEP-2
    n = p*q

    # STEP-3
    phi = (p-1)*(q-1)

    # STEP-4
    e = random.randint(3, phi-1)
    while math.gcd(e, phi)!=1:
        e = random.randint(3, phi-1)

    d = mod_inverse(e,phi)

    return e,d,n