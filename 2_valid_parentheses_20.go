// https://leetcode.com/problems/valid-parentheses/description/

package main

import "fmt"

// 100% solution

func isValid(s string) bool {
	valuesDict := map[rune]rune{
		'}': '{',
		')': '(',
		']': '[',
	}

	var stack []rune

	for _, char := range s {

		if opening, found := valuesDict[char]; found {

			if len(stack) > 0 && stack[len(stack)-1] == opening {
				stack = stack[:len(stack)-1]
				continue
			}
		}
		stack = append(stack, char)
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()[]{}")) // true
	fmt.Println(isValid("(]"))     // false
}
