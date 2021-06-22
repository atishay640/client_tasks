"""Handles palindrome operations Definition: A palindrome is a string that reads the same forward and backward.
For example, "abcba" is a palindrome, "abab" is not."""


def is_palindrome(word: str) -> bool:

    """Please implement this function to return true if the parameter is a palindrome and false otherwise.

       :param word string to determine if a palindrome
       :return true if the parameter is a palindrome and false otherwise"""

    # if word is either "" or None return false
    if not word:
      return False
    return word[::-1] == word
