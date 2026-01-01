# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# asked Gemini to code quickly foo to create objects of ListNode
def create_linked_list(arr):

    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# again Gemini helped me to do quickly
def print_linked_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) if elements else "Empty List")


# 100% solution

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return_node = ListNode(None)
        current = return_node

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        current.next = list1 if list1 else list2

        return return_node.next


list1 = create_linked_list([2, 3, 4])
list2 = create_linked_list([1, 2])
print(Solution().mergeTwoLists(list1, list2))

list1 = create_linked_list([1, 1, 1])
list2 = create_linked_list([1, 3, 4])
print(Solution().mergeTwoLists(list1, list2))


list1 = create_linked_list([2])
list2 = create_linked_list([4])
print(Solution().mergeTwoLists(list1, list2))

list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])
solution = (Solution().mergeTwoLists(list1, list2))
print_linked_list(solution)
