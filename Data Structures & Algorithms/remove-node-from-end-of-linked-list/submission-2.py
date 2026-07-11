# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        counter -= n + 1
        curr = head
        if counter < 0:
            return head.next
        while counter > 0:
            curr = curr.next
            counter -= 1
        curr.next = curr.next.next
        return head