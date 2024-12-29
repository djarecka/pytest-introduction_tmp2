def prime_factors(n):
    """
    Find all prime factors of a given number.

    Args:
        n (int): The number to factorize.

    Returns:
        list: A list of prime factors of n.
    """
    factors = []
    # Handle the factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Handle odd factors from 3 upwards
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    return factors

def test_prime_factors():
    assert prime_factors(8) == [2, 2, 2], "The prime factors of 8 are [2, 2, 2]"
    assert prime_factors(18) == [2, 3, 3], "The prime factors of 18 are [2, 3, 3]"
    assert prime_factors(108) == [2, 2, 3, 3, 3], "The prime factors of 108 are [2, 2, 3, 3, 3]"

if __name__ == "__main__":
    test_prime_factors()
    print("Everything passed")