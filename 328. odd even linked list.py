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
    def oddEvenList(self, head):
        if not head: return None # no nodes
        if not head.next: return head # one node
        if not head.next.next: return head # two nodes
        
        # find tail and length
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        # move every even index to end
        parent = head
        curr = head.next
        n_swaps = 0
        while n_swaps != int(n / 2):
            # move node to end
            parent.next = curr.next
            curr.next = None
            tail.next = curr
            tail = curr
            parent = parent.next
            curr = parent.next
            n_swaps += 1
        return head
    
node = ListNode.from_list([1, 2, 3, 4, 5, 6])
print(Solution().oddEvenList(node))