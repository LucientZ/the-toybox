"""
This is a collection of various functions that could be useful in modular arithmetic
"""


def compute_gcd(a: int, b: int) -> int:
    """
    Recursive computation of gcd. This is an implementation of the euclidean algorithm.

    If a=qb+r, then gcd(a, b) = gcd(b, r)
    """
    min: int = a if a < b else b
    max: int = a if a >= b else b

    if min == 0:
        return max
    else:
        # print(f"{max} = {max // min}*{min} + {max % min}")
        return compute_gcd(min, max % min)


def extended_euclidean(a: int, b: int) -> (int, int, int):
    """
    Recursive computation of gcd. This is an implementation of the extended euclidean algorithm.

    If a=qb+r, then gcd(a, b) = gcd(b, r)
    """

    if a == 0:
        return (b, 0, 1)  # Second row in table method
    else:
        r, u, v = extended_euclidean(b % a, a)
        q = b // a
        return (r, v - q * u, u)


def modular_inverse(a: int, b: int) -> int:
    """
    This function computes the modular inverse of a number a mod b utilizing the extended euclidean algorithm
    """
    r, u, v = extended_euclidean(a, b)

    # r == 1 means that a and b are not co-prime
    if r != 1:
        print("No Inverse")
        return -1
    else:
        return u % b


def main() -> None:
    a: int = 12
    b: int = 52384765943

    if type(a) != int or type(b) != int:
        raise Exception("a or b are not integers")

    print(f"compute_gcd({a}, {b}): {compute_gcd(a,b)}\n")
    
    print(f"extended_euclidean({a}, {b}): {extended_euclidean(a,b)}\n")

    print(f"modular_inverse({a}, {b}): {modular_inverse(a,b)}")
    print(f"modular_inverse({b}, {a}): {modular_inverse(b,a)}")


if __name__ == "__main__":
    main()
