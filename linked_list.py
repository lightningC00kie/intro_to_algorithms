class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, l):
        self.head = self.tail = None
        for i in range(len(l)-1, -1, -1):
            p = Node(l[i], self.head)
            self.head = p
        
    def to_list(self):
        head = self.head
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        return l

    def len(self):
        n = self.head
        count = 0
        while n != None:
            n = n.next
            count += 1

        return count

    def get(self, n):
        count = 0
        p = self.head
        for i in range(n):
            p = p.next
        return p.val
    
    def has(self, x):
        n = self.head
        while n != None:
            if n.val == x:
                return True
            n = n.next

        return False

    def delete(self, x):
        if self.len() >= 1:
            n = self.head
            if n.val == x:
                self.head = n.next
            else:
                for i in range(self.len()-1):
                    if n.next.val == x:
                        n.next = n.next.next
                        break
                    else:
                        n = n.next
        return

    def rotate(self):
        if self.len() >= 2:
            head = n = self.head
            
            while n.next.next != None:
                n = n.next
            
            temp = n.next 
            self.head = n.next 
            self.head.next = head
            n.next = None 

        return
        
    def starts_with(self, m):
        if m.len() > self.len():
            return False
        if m.len() == 0:
            return True
        
        n = m.head
        p = self.head
        while n.next != None:
            if n.val == p.val and n.next.val == p.next.val:
                n = n.next
                p = p.next
            else:
                return False
            return True

    def contains(self, m):
        if m.len() > self.len():
            return False
        if m.len() == 0:
            return True
        p = self

        for i in range(self.len()):
            if p.starts_with(m):
                return True
            else:
                p.head = p.head.next
        return False

    def ends_with(self, m):
        if m.len() > self.len():
            return False
        if m.len() == 0:
            return True
        p = LinkedList(self.to_list())
        for i in range(m.len()):
            p.rotate()
        return p.starts_with(m)
