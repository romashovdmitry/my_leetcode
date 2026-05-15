from typing import Optional
from time import sleep

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_and_sleep(anyfuckinkshit):
    print(anyfuckinkshit)
    sleep(1)

def print_list(node: ListNode):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print_and_sleep(f'\nRESULT -> {values}')


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head

        previous_steps: list = []

        while head:
            print_and_sleep(f'head.val -> {head.val}')
            previous_steps.append(head.val)
            head: ListNode = head.next

        print_and_sleep(f'previous_steps -> {previous_steps}')        

        return_head: ListNode = ListNode(val=previous_steps.pop())
        next_step: ListNode = ListNode()
        return_head.next = next_step

        while previous_steps:
            print_list(return_head)
            next_step.val = previous_steps.pop()
            next_step.next = ListNode() if previous_steps else None
            next_step = next_step.next

        print_and_sleep(f'return_head -> {return_head.val}')
        return return_head

print('\n')
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(Solution().reverseList(head=head))

print('\n')
head = ListNode(1, ListNode(2))
print_list(Solution().reverseList(head=head))

print('\n')
head = None
print_list(Solution().reverseList(head=head))

