#!/usr/bin/python3
"""Module for Node and SinglyLinkedList"""


class Node:
    """Represent a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """Initialize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return the string representation of the list"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
