# https://github.com/TheAlgorithms/Python/blob/master/strings/rabin_karp.py

# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003


def rabin_karp(pattern: str, text: str) -> int:
    """
    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with complexity O(nm), most efficient when it is used with multiple patterns
    as it is able to check if any of a set of patterns match a section of text in o(1)
    given the precomputed hashes.
    This will be the simple version which only assumes one pattern is being searched
    for but it's not hard to modify
    1) Calculate pattern hash
    2) Step through the text one character at a time passing a window with the same
        length as the pattern
        calculating the hash of the text within the window compare it with the hash
        of the pattern. Only testing equality if the hashes match
    """
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return -1

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    # Calculating the hash of pattern and substring of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, t_len - p_len + 1):
        if text_hash == p_hash and text[i: i + p_len] == pattern:
            return i
        if i == t_len - p_len:
            continue
        # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
        text_hash = ((text_hash - ord(text[i]) * modulus_power) * alphabet_size + ord(text[i + p_len])) % modulus
    return -1
