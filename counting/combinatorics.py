from math import factorial

def nCk(n: int, k: int) -> int:
    """
    Count the number of combinations without repetition.

    Formula: C(n, k) = n! / (k! * (n - k)!)

    :param n: Total number of items.
    :param k: Number of items to choose.
    :return: Number of combinations.
    """
    if n < k:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def nCk_rep(n: int, k: int) -> int:
    """
    Count the number of combinations with repetition.

    Formula: C(n + k - 1, k) = (n + k - 1)! / (k! * (n - 1)!)

    :param n: Total number of items.
    :param k: Number of items to choose.
    :return: Number of combinations with repetition.
    """
    return nCk(n + k - 1, k)

def perm(n: int, k: int) -> int:
    """
    Count the number of permutations without repetition.

    Formula: P(n, k) = n! / (n - k)!

    :param n: Total number of items.
    :param k: Number of items to choose.
    :return: Number of permutations.
    """
    if n < k:
        return 0
    return factorial(n) // factorial(n - k)

def perm_rep(n: int, k: int) -> int:
    """
    Count the number of permutations with repetition.

    Formula: n^k

    :param n: Total number of items.
    :param k: Number of items to choose.
    :return: Number of permutations with repetition.
    """
    return n ** k

# Example usage
if __name__ == "__main__":
    n = 5
    k = 3

    print("Combinations (no repetition):", nCk(n, k))
    print("Combinations (with repetition):", nCk_rep(n, k))
    print("Permutations (no repetition):", perm(n, k))
    print("Permutations (with repetition):", perm_rep(n, k))
