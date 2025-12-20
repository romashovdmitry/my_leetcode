// https://leetcode.com/problems/group-anagrams/description/

package main

import (
	"sort"
)

func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[string][]string)

	for _, word := range strs {
		sBytes := []byte(word)
		sort.Slice(sBytes, func(i, j int) bool {
			return sBytes[i] < sBytes[j]
		})
		sortedKey := string(sBytes)
		anagramMap[sortedKey] = append(anagramMap[sortedKey], word)
	}
	result := make([][]string, 0, len(anagramMap))

	for _, group := range anagramMap {
		result = append(result, group)
	}

	return result
}
