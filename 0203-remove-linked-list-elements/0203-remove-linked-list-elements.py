class Solution:
    def removeElements(self, head, val):
        curr = head
        prev = None

        while curr:

            if curr.val == val:

                if prev is None:
                    head = curr.next

                else:
                    prev.next = curr.next

            else:
                prev = curr

            curr = curr.next

        return head