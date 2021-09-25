class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes: data and link to the next node in the link
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


"""
To Run Program till here:

$ python -i linked_list.py
>>>N1 = Node(10)
>>>N1
<Node data: 10>
>>>N2 = Node(20)
>>>N1.next_node() = N2
>>>N1.next_node()
<Node data: 20>
>>>exit()
"""


class LinkedList:
    # head = None
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None   # If true = List is empty

    def size(self):
        """
        Take the number of nodes in list
        Takes O(n) time 
        """
        current = self.head
        count = 0

        while current:           # till the end
            count += 1
            current = current.next_node

        return count     


        """
        To Run Program till here:

        $ python -i linked_list.py
        >>>l = LinkedList()
        >>>N1 = Node(10)
        >>>l.head = N1
        >>>l.size() 
        1
        >>>exit()
        """

    def add(self, data):
        """
        This adds a new node with data at the head of linked list
        Time O(1) complexity
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

        """
            To Run Program till here:

            $ python -i linked_list.py
            >>>l = LinkedList()
            >>>l.add(1)
            >>>l.size()
            >>>1
            >>>l.add(2)
            >>>l.add(3)
            >>>l.add(4)
            >>>l.size() 
            4
            >>>exit()
        """

    def search(self, key):
        """ 
        Search for first node containing data that matches key
        Return node or 'None' if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None        

    """
         Running Search
            PS C:\Users\User\PycharmProjects\Linked_List> python -i linked_list.py
            >>> l = LinkedList()
            >>> l.add(10)
            >>> l.add(2)
            >>> l.add(45)
            >>> l.add(35)
            >>> n = l.search(45)
            >>> n
            <Node data: 45>
            >>> l
            [Head: 35]-> [45]-> [2]-> [Tail: 10]
        
    """

    def insert(self, data, index):
        """
        Inserts a new node at index position 
        Insersion takes O(1) time but
        finding the node at insertion point takes O(n) time

        Overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1 

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            next.next_node = next_node   

    def remove(self, key):
        """
        Removes node containing data matching the key
        Return nodes or None if DNE
        Takes O(n) time 
        """
        
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current        


    
    def __repr__(self):
        """
        Returns a string representation of the list
        Time O(n) complexity: Since Traversing list 
        """    
        
        nodes = []  # empty node
        current = self.head  # pointing to head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)


    """
            To Run Program till here:

            $ python -i linked_list.py
            >>> l = LinkedList()
            >>> l.add(1)
            >>> l.add(2)
            >>> l.add(3)
            >>> l
            [Head: 3]-> [2]-> [Tail: 1]
            >>> l        
    """

