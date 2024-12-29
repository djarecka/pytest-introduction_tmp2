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
    for i in range(3, int(n ** 0.5), 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    return factors

def test_prime_factors():
    assert prime_factors(8) == [2, 2, 2]


if __name__ == "__main__":
    test_prime_factors()