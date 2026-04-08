from fractions import Fraction

def padic_valuation(x, p):
    """
    Compute p-adic valuation v_p(x) for a rational number x.
    v_p(x) = k such that x = p^k * (a/b) and p does not divide a or b.
    """
    if x == 0:
        return float('inf')

    x = Fraction(x)
    num, den = x.numerator, x.denominator

    v = 0
    while num % p == 0:
        v += 1
        num //= p

    while den % p == 0:
        v -= 1
        den //= p

    return v

def adelic_check(x, primes, max_nonzero):
    """
    Checks if a rational number has at most `max_nonzero` nonzero p-adic valuations
    across the given set of primes.
    """
    nonzero_count = 0
    for p in primes:
        if padic_valuation(x, p) != 0:
            nonzero_count += 1

    return nonzero_count <= max_nonzero
