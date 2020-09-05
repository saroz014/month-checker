#!/usr/bin/env python3
from exceptions import *


class Node:
    def __init__(self, item):
        self.prev = None
        self.data = item
        self.next = None


class CDLL:
    def __init__(self, start, end):
        if start > end:
            raise StartIsGreaterThanEndError(start, end)
        elif start == end:
            raise StartIsEqualToEndError(start, end)

        self.start = start
        self.end = end
        self.head = Node(start)
        self.tail = Node(end)
        self.tail.next = self.head
        self.head.prev = self.tail
        self.temp_node = self.head
        for num in range(start + 1, end + 1):
            if num == end:
                self.temp_node.next = self.tail
                self.tail.prev = self.temp_node
            else:
                self.node = Node(num)
                self.temp_node.next = self.node
                self.node.prev = self.temp_node
                self.temp_node = self.node

    def is_between(self, num, initial, final):
        limit = range(self.start, self.end + 1)
        if num not in limit:
            raise NumberNotInRangeError(num, self.start, self.end)
        if initial not in limit:
            raise NumberNotInRangeError(initial, self.start, self.end)
        if final not in limit:
            raise NumberNotInRangeError(final, self.start, self.end)

        trav = self.head
        while trav.data != initial:
            trav = trav.next

        self.initial_node = trav
        self.found_num = False
        while trav.data != final:
            if trav.data == num:
                self.found_num = True
            trav = trav.next

        if self.found_num and trav.data == final:
            return True
        return False


def main():
    try:
        c = CDLL(1, 12)
    except StartIsGreaterThanEndError as e:
        print(e.message)
        return
    except StartIsEqualToEndError as e:
        print(e.message)
        return
    try:
        month_to_check = int(input('Enter the month number to check: '))
        initial_month = int(input('Enter the initial month: '))
        final_month = int(input('Enter the final month: '))
        print(c.is_between(month_to_check, initial_month, final_month))
    except NumberNotInRangeError as e:
        print(e.message)
        return


if __name__ == '__main__':
    main()

