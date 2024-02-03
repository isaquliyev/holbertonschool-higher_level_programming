#!/usr/bin/python3
"""This file contains Node and Singly linked list class"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initialize data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """Initialize head and values"""
        self.__head = None
        self.__values = []

    def __str__(self):
        """Material for print"""
        res = ""
        while self.__head is not None:
            res = res + str(self.__head.data) + '\n'
            self.__head = self.__head.next_node
        return res[:-1]

    def sorted_insert(self, value):
        """Inserts new element appropiate order."""
        self.__values.append(value)
        self.__values.sort()
        self.__values.reverse()
        length = len(self.__values)
        for i in range(length):
            new_node = Node(self.__values[i])
            if 'temp' in locals():
                new_node.next_node = temp
            temp = new_node
            if i == length - 1:
                self.__head = new_node
        return
