# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return
        mid = head
        fast = head
        while fast and fast.next != None:
            mid = mid.next
            fast = fast.next.next
        list2 = mid.next
        mid.next = None
        prev = None
        curr = list2
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        list2 = prev
        curr = head
        while list2 != None:
            temp = curr.next
            curr.next = list2
            list2 = list2.next
            curr = curr.next
            curr.next = temp
            curr = curr.next
        
        
            