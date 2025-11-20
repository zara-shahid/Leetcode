# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        fast = head
        while fast and fast.next:
            if fast.next.val==val:
                fast.next=fast.next.next
            else:
                fast = fast.next 
        return head
