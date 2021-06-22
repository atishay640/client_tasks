from __future__ import annotations
import operator
import itertools

"""Class to calculate the average value of the nodes in a tree"""


class Node:
    """Represents a single node in a tree structure"""

    def __init__(self, value: int):
        self.value = value
        self.children = []

    def get_value(self) -> int:
        """
        :return int value of the node
        """
        return self.value

    def get_children(self) -> list:
        """
        :return list of children this node has
        """
        return self.children

    def add_child(self, node: Node) -> None:
        self.children.append(node)

def get_sum_and_count(root: Node, node_sum=0, node_count=0) -> tuple:
    if root:
        node_count +=1
        list_of_pairs = [get_sum_and_count(child) for child in root.get_children()]
        node_sum += root.get_value() + sum(sum for sum, count in list_of_pairs)
        node_count += sum(count for sum, count  in list_of_pairs)
    return (node_sum, node_count)


def get_average(root: Node, sum=0, count=0) -> tuple:
    """
    Please implement this method to return the average of all node values (Node.getValue()) in the tree.

    :param root the root node of a tree from which to determine the average value
    :return the average of all node values in the tree
    """
    if not root:
        return 0

    sum, count = get_sum_and_count(root)
    return sum/count

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
