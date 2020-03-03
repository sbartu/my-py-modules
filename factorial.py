from functools import reduce as red


def factorial(n):
    """Calculate n! from n."""
    return red(
        lambda x, y: x * y,
        range(1, n + 1)
    )
