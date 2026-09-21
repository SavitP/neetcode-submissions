"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        if head == None:
            return None
        curr = head
        while curr != None:
            m[curr] = Node(curr.val)
            curr = curr.next
        toReturn = m[head]
        curr1 = head
        curr2 = toReturn
        while curr1 != None:
            if curr1.next != None:
                curr2.next = m[curr1.next]
            if curr1.random != None:
                curr2.random = m[curr1.random]
            curr1 = curr1.next
            curr2 = curr2.next
        return toReturn