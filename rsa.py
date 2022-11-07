from math import gcd


def phi(n):
  return sum(gcd(i, n) == 1 for i in range(1, n))

def find_d(e, n):
  d = 1
  while (d * e) % phi(n) != 1:
    d += 1
  return d

def get_keys(p, q):
  n = p * q
  e = 2
  while gcd(e, phi(n)) != 1:
    e += 1
  d = 1
  while (d * e) % phi(n) != 1:
    d += 1
  return (e, n), (d, n)


def encrypt(m, key): 
  e, n = key
  return pow(m, e, n)


def decrypt(c, key):
  d, n = key
  return pow(c, d, n)


def prime_factorization(n):
  factors = []
  d = 2
  while n > 1:
    while n % d == 0:
      factors.append(d)
      n //= d
    d += 1
  return factors


def check_keys(keys):
  (e, n), (d, m) = keys

  assert n == m, "The two given \"n\" in the key are not equal."
  
  # 1. Prime factors product  
  if len(prime_factorization(n)) != 2:
    return (False, "n is not the product of two primes")

  # 2. PGCD of e and phi is 1
  if gcd(e, phi(n)) != 1:
    return (False, "e and phi(n) are not coprime")

  # 3. e * d % phi = 1
  if (e * d) % phi(n) != 1:
    return (False, "e * d % phi(n) are not coprime")

  return (True, "Keys are valid.")
