// https://leetcode.com/problems/longest-substring-without-repeating-characters/

package main

import (
	"fmt"
)

// beats 100%

func lengthOfLongestSubstring(s string) int {
	result := 0
	left := 0
	char_map := make(map[byte]int)

	for right := 0; right < len(s); right++ {
		if index, found := char_map[s[right]]; found && index >= left {
			left = index + 1
		}
		char_map[s[right]] = right

		current_len := right - left + 1
		if current_len > result {
			result = current_len
		}
	}

	return result
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb")) // 3
	fmt.Println(lengthOfLongestSubstring("bbbbb"))    // 1
	fmt.Println(lengthOfLongestSubstring("pwwkew"))   // 3
}
