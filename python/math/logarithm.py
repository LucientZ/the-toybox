from typing import Union


def log(x: Union[int, float], base: Union[int, float] = 2) -> float:
    """
    This is an unconventional way of calculating a logarithm. It is not more precise than other methods and introduces a lot of error, but I just want to see if I can implement this.

    Because a logarithm is just the inverse of an exponential function, you can think of it as "The amount of times you can evenly divide a number by the base".
    This algorithm takes x as an integer and
    """
    if x < 0:
        raise ValueError(f"Invalid value passed: {x}","x cannot be negative")

    left_of_decimal = int(x)
    result: float = 0.0

    while left_of_decimal > 1:
        left_of_decimal = left_of_decimal >> 1
        result += 1

    if base != 2:
        return result / log(base)
    return result


def main():
    x = 14
    base = 7

    print(log(x, base))


if __name__ == "__main__":
    main()
