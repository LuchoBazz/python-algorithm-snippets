from itertools import combinations, combinations_with_replacement, permutations, product
from typing import List, Tuple

def gen_nCk(items: List[int], k: int) -> List[Tuple[int, ...]]:
    """
    Generate all unique combinations without repetition of a given length.

    :param items: List of items to generate combinations from.
    :param k: Length of each combination.
    :return: List of unique combinations.
    """
    return list(combinations(items, k))

def gen_nCk_rep(items: List[int], k: int) -> List[Tuple[int, ...]]:
    """
    Generate all combinations with repetition of a given length.

    :param items: List of items to generate combinations from.
    :param k: Length of each combination.
    :return: List of combinations with repetition.
    """
    return list(combinations_with_replacement(items, k))

def gen_perm(items: List[int], k: int) -> List[Tuple[int, ...]]:
    """
    Generate all unique permutations without repetition of a given length.

    :param items: List of items to generate permutations from.
    :param k: Length of each permutation.
    :return: List of unique permutations.
    """
    return list(permutations(items, k))

def gen_perm_rep(items: List[int], k: int) -> List[Tuple[int, ...]]:
    """
    Generate all permutations with repetition of a given length.

    :param items: List of items to generate permutations from.
    :param k: Length of each permutation.
    :return: List of permutations with repetition.
    """
    return list(product(items, repeat=k))

# Example usage
if __name__ == "__main__":
    items = [1, 2, 3]
    k = 2
    
    unique_comb = gen_nCk(items, k)
    comb_rep = gen_nCk_rep(items, k)
    unique_perm = gen_perm(items, k)
    perm_rep = gen_perm_rep(items, k)

    print("Unique Combinations (%s):\n%s" % (len(unique_comb), unique_comb), '\n')
    print("Combinations with Repetition (%s):\n%s" % (len(comb_rep), comb_rep), '\n')
    print("Unique Permutations (%s):\n%s" % (len(unique_perm), unique_perm), '\n')
    print("Permutations with Repetition (%s):\n%s" % (len(perm_rep), perm_rep), '\n')
