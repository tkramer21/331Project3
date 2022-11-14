from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    def __eq__(self, other: Node):
        return self.value == other.value

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better#

    def empty(self) -> bool:
        """
        Checks the head of the DLL to see if it contains any Nodes
        :return: A Ture boolean if empty, False otherwise
        """
        if self.head is not None:
            return False
        else:
            return True

    def push(self, val: T, back: bool = True) -> None:
        """
        Adds a new node to the back or front of an existing DLL
        :param val: val of the new node to be added
        :param back: boolean indicating adding new node to front (False) or back (True)
        :returns: None
        """
        new_node = Node(val)
        if not self.empty():
            if back == True:
                if self.size == 1:
                    self.head.next = new_node
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
                self.size += 1
            else:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
                self.size += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.size = 1

    def pop(self, back: bool = True) -> None:
        """
        Removes the first or last Node from a DLL dependent on param: back
        :param back: boolean indicating removal from front (False) or back (True)
        :returns: None
        """
        if not self.empty():
            if back == True:  # remove at back
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.next = None
                self.size -= 1

                if self.size == 0:
                    self.head = None
                    self.tail = None

            else:  # remove at front
                if self.head == self.tail:
                    self.tail = None
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                self.size -= 1
        else:
            return

    def list_to_dll(self, source: List[T]) -> None:
        """
        Takes a python list and creates a DLL from its contents
        :param source: python list to be appended to
        :returns: python list containing DLL values
        """
        self.size = 0
        for i in source:
            self.push(i)

    def dll_to_list(self) -> List[T]:
        """
        Takes a DLL and creates a Python list from its contents
        :returns: DLL  containing Python list values
        """
        ptr = self.head
        new_list = []
        if ptr is not None:
            while ptr is not None:
                new_list.append(ptr.value)
                ptr = ptr.next
            return new_list
        else:
            return new_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Finds nodes from a DLL with the same value of param val; will find all nodes dependent on find-first
        :param val: the value to be found
        :param find_first: boolean indicating to find 1 Node (True) or all Nodes (False)
        :returns: a list of all the nodes, 1 Node or None (value not found)
        """
        ptr = self.head
        new_list = []
        if ptr is not None:
            while ptr is not None:
                if ptr.value == val:
                    new_list.append(ptr)
                    if find_first == True:
                        return new_list
                ptr = ptr.next

            if len(new_list) != 0:
                return new_list

        else:
            return None

    def find(self, val: T) -> Node:
        """
        Calls _find_nodes to find the first occurrence of a Node with value val
        :param val: the node value to be found
        :returns: The node found or None
        """
        value = self._find_nodes(val, True)
        if value is not None:
            return value[0]
        else:
            return None

    def find_all(self, val: T) -> List[Node]:
        """
        Finds all node instances within a DLL
        :param val: node value to be searched for
        :return: a python list containing the node objects or an empty list if not found
        """
        value = self._find_nodes(val)
        if value is not None:
            return value
        else:
            return []

    def _remove_node(self, to_remove: Node) -> None:
        """
        Removes the node passed as a param
        :param to_remove: a reference to the node to be removed
        :returns: None
        """

        if self.head == to_remove:  # remove from front
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

        elif self.tail == to_remove:  # remove from end
            self.tail = self.tail.prev
            self.tail.next = None

        elif self.size == 1 and self.head == to_remove:  # remove last el
            self.head = None
            self.tail = None

        else:
            to_remove.next.prev = to_remove.prev
            to_remove.prev.next = to_remove.next

    def remove(self, val: T) -> bool:
        """
        Removes the first instance of a node with value val
        :param val: the value to be removed from the DLL
        :return: A boolean; True if successful, False otherwise
        """
        value = self.find(val)
        if value is not None:
            self._remove_node(value)
            return True
        else:
            return False

    def remove_all(self, val: T) -> int:
        """
        Removes all node instances with the value passed to the functions
        :param val: the value to be removed from the DLL
        :return: An int representing the number of Nodes removed
        """
        value = self.find_all(val)
        size = len(value)
        for i, node in enumerate(value):
            self._remove_node(value[i])
        if size == 0:
            return 0
        else:
            return size

    def reverse(self) -> None:
        """
        Reorders a DLL in the reverse order
        :returns: None
        """
        if not self.empty():
            temp = None
            ptr = self.head
            while ptr is not None:
                next = ptr.prev
                prev = ptr.next
                ptr.next = next
                ptr.prev = prev
                ptr = prev

            temp = self.head
            self.head = self.tail
            self.tail = temp


def fix_playlist(lst: DLL) -> bool:
    """
    Checks a playlist modelded by a DLL to see if it is broken, has an improper loop, or is fixed; will fix a broken
    list, but not an improper one.
    :param lst: The DLL list to be checked
    :return: A boolean True if the playlist is functional, or it was fixed by the program, returns False if it is
    improper
    """

    def connect_list(slow, fast) -> bool:
        """
        Contains the while loop creating Floyd's Cycle Finding Algorithm, will fix a broken loop
        :param slow: a pointer to a node incremented by 1 every loop
        :param fast: a pointer to a node incremented by 2 every loop
        :return: A boolean, True if proper, False if improper
        """

        proper = False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                fix_playlist_helper()
                return True
            if fast is lst.head or fast.next is lst.head:
                return True
            if fast is slow:
                return False
        lst.head.prev = lst.tail
        lst.tail.prev = lst.head
        return True

    def fix_playlist_helper():
        """
        Sets the head and tail next/prev to the correct nodes; also handles DLL of size 1
        :returns: None
        """
        if lst.size == 1:
            lst.head.next = lst.head
            lst.head.prev = lst.head
        else:
            lst.head.prev = lst.tail
            lst.tail.next = lst.head

    if not lst.empty():
        if lst.head.next is not None and lst.head.next.next is not None:
            slow = lst.head
            fast = lst.head
            if slow == fast:
                if lst.size == 1:
                    return True
                else:
                    return connect_list(slow, fast)

            return connect_list(slow, fast)

        else:
            fix_playlist_helper()
            return True
    else:
        return True
