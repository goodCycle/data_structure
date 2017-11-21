# Linked List implemented by Python(2.x)
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        current = self.head
        if current:
            for i in range(1,position):
                if current.next:
                    current = current.next
                else:
                    print("The given position is out of the range of linked list!!")
                    return None
            return current

        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head # head is position 1
        if current and new_element:
            if position < 1:
                return None
            elif position == 1:
                self.head = new_element
                self.head.next = current
            else:
                for i in range(2,position): # move the current to position-1
                    if current.next:
                        current = current.next
                    else:
                        return None
                origin_next = current.next
                current.next = new_element
                new_element.next = origin_next
        elif new_element == None:
            return None
        else: # if lst has no element
            self.append(new_element)

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value and current.next:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        else:
            print("no value in this linked list")
            return None



a = Element(1)
b = Element(2)
c = Element(3)
lst = LinkedList()
lst.append(a)
lst.append(b)
lst.append(c)
print("insert =======")
lst.insert(Element(4),1)
lst.insert(None, 1)
print(lst.head.value)
print(lst.head.next.value)
print(lst.head.next.next.value)
print("get position ====")
if lst.get_position(3):
    print(lst.get_position(3).value)
if lst.get_position(4):
    print(lst.get_position(4).value)
if lst.get_position(5):
    print(lst.get_position(5).value)
print("delete =====")
lst.insert(Element(4),1)
lst.delete(4)
if lst.get_position(1):
    print(lst.get_position(1).value)
lst.delete(1)
if lst.get_position(2):
    print(lst.get_position(2).value)

lst.delete(5)
