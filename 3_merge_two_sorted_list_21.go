// https://leetcode.com/problems/merge-two-sorted-lists/
package main

import (
	"fmt"
	"strconv"
	"strings"
)

// https://leetcode.com/problems/merge-two-sorted-lists/

type ListNode struct {
	Val  int
	Next *ListNode
}

// asked Gemini to code quickly foo to create objects of ListNode
func createLinkedList(arr []int) *ListNode {
	if len(arr) == 0 {
		return nil
	}
	head := &ListNode{Val: arr[0]}
	current := head
	for _, val := range arr[1:] {
		current.Next = &ListNode{Val: val}
		current = current.Next
	}
	return head
}

// again Gemini helped me to do quickly
func printLinkedList(head *ListNode) {
	var elements []string
	for head != nil {
		elements = append(elements, strconv.Itoa(head.Val))
		head = head.Next
	}
	if len(elements) == 0 {
		fmt.Println("Empty List")
	} else {
		fmt.Println(strings.Join(elements, " -> "))
	}
}

// 100% solution
type Solution struct{}

func (s Solution) mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	returnNode := &ListNode{}
	current := returnNode

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			current.Next = list1
			list1 = list1.Next
		} else {
			current.Next = list2
			list2 = list2.Next
		}
		current = current.Next
	}

	if list1 != nil {
		current.Next = list1
	} else {
		current.Next = list2
	}

	return returnNode.Next
}

func main() {
	sol := Solution{}

	list1 := createLinkedList([]int{2, 3, 4})
	list2 := createLinkedList([]int{1, 2})
	printLinkedList(sol.mergeTwoLists(list1, list2))

	list1 = createLinkedList([]int{1, 1, 1})
	list2 = createLinkedList([]int{1, 3, 4})
	printLinkedList(sol.mergeTwoLists(list1, list2))

	list1 = createLinkedList([]int{2})
	list2 = createLinkedList([]int{4})
	printLinkedList(sol.mergeTwoLists(list1, list2))

	list1 = createLinkedList([]int{1, 2, 4})
	list2 = createLinkedList([]int{1, 3, 4})
	solution := sol.mergeTwoLists(list1, list2)
	printLinkedList(solution)
}

// We use this block for LeetCode
// func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
//    returnNode := &ListNode{}
//    current := returnNode
//
//    for list1 != nil && list2 != nil {
//        if list1.Val <= list2.Val {
//            current.Next = list1
//            list1 = list1.Next
//        } else {
//            current.Next = list2
//            list2 = list2.Next
//        }
//        current = current.Next
//    }
//
//    if list1 != nil {
//        current.Next = list1
//    } else {
//        current.Next = list2
//    }
//
//    return returnNode.Next
//}
