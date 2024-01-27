# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    @classmethod
    def from_list(cls, values):
        node = ListNode()
        head = node
        for i, value in enumerate(values):
            node.val = value
            if i == len(values)-1:
                break
            node.next = ListNode()
            node = node.next
            
        return head
    
    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.val)
            node = node.next
        return values

class Solution:
    def reverseList(self, head):
        if not head or not head.next: return None # no nodes

        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

node = ListNode.from_list([1, 2, 3, 4, 5])
print(Solution().reverseList(node).get_values())