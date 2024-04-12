"""
Write a function that takes two words and returns True if they are anagrams.
Test your function with the examples below.
"""


def is_anagram(word1, word2):
    """
    parametres
    ---------
    word : str
        The first word
    word1 : str
        the second word
    returns
    --------
    bool
        True if the two words are anagrams, False
    """
    # Convert both words to lowercase and sort their letters.
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())

    # check if the sorted words are equal
    results = sorted_word1 == sorted_word2
    return results


print(is_anagram("tachymetric", "mccarthyite"))
