class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        prev, curr = None, head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(3)
    head.next.next = ListNode(4)

    sol = Solution()
    print(sol.reverseList(head))
        