# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        toReturn = ListNode(0)
        curr3 = toReturn
        carry = 0
        while curr1 and curr2:
            curr3.next = ListNode((curr1.val + curr2.val + carry) % 10)
            if ((curr1.val + curr2.val + carry) // 10) == 1:
                carry = 1
            else:
                carry = 0
            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next
        if not curr1:
            while curr2:
                curr3.next = ListNode((curr2.val + carry) % 10)
                if ((curr2.val + carry) // 10) == 1:
                    carry = 1
                else:
                    carry = 0
                curr2 = curr2.next
                curr3 = curr3.next
        else:
            while curr1:
                curr3.next = ListNode((curr1.val + carry) % 10)
                if ((curr1.val + carry) // 10) == 1:
                    carry = 1
                else:
                    carry = 0
                curr1 = curr1.next
                curr3 = curr3.next
        if carry == 1:
            curr3.next = ListNode(1)
        return toReturn.next