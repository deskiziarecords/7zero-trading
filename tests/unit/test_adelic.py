import pytest
from aegis.zeta_flux.reverse_period.core.adelic import padic_valuation, adelic_check
from fractions import Fraction

def test_padic_valuation():
    assert padic_valuation(12, 2) == 2   # 12 = 2^2 * 3
    assert padic_valuation(12, 3) == 1   # 12 = 2^2 * 3^1
    assert padic_valuation(Fraction(1, 4), 2) == -2 # 4 = 2^2 in denominator

def test_adelic_manifold():
    # Rational number with finite support
    assert adelic_check(Fraction(15, 8), primes=[2,3,5,7,11,13], max_nonzero=3) == True
    
    # Too many nonzero valuations: 2, 3, 5, 7, 11, 13 are all factors/divisors
    x = Fraction(2*3*5*7*11, 13)
    # v2=1, v3=1, v5=1, v7=1, v11=1, v13=-1 -> 6 nonzero valuations
    assert adelic_check(x, primes=[2,3,5,7,11,13], max_nonzero=3) == False
