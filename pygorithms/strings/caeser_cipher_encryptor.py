"""Problem Statement.

Caeser Cipher Encryptor.

Given a non-empty string of lowercase letters and a non-negative integer value representing a key,
write a function that returns a new string obtained by shifting the key, k amount in the
alphabetter (English). Note letters should wrap around. In other words the letter 'z' shifted by 1
returns the letter 'a'.
"""


def caeser_cipher_encryptor(string, k):
    """Encrypt given string.

    One-liner. Note: only works with the set {a,z}

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    return ''.join((lambda c: chr(ord('a') + ((ord(c) - ord('a') + k) % 26)))(c) for c in string)
