import pytest
from src.question1 import palindrome
from src.question2.tree_average_value import Node, get_average


def test_palindrome():
    """
    Test is_palindrome function from question1
    """
    test_str = "abcba"
    is_true = palindrome.is_palindrome(test_str)
    assert is_true

def test_not_palindrome():
    """
    Test is_palindrome function from question1 with non palindrom.
    """
    test_str = "race a car"
    is_true = palindrome.is_palindrome(test_str)
    assert not is_true
    
def test_node_average():
    """
    Test get_average function from question2. Calculate and verify the average.
    """
    root = Node(4)
    child1 = Node(3)
    child2 = Node(6)
    child3 = Node(4)

    child2.add_child(Node(4))
    child2.add_child(Node(5))

    child3.add_child(Node(2))
    child3.add_child(Node(4))

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    average = get_average(root) # 4+3+4+6+4+5+2+4/8 = 4.0
    assert average == 4.0

    