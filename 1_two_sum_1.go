// Two Sum: https://leetcode.com/problems/two-sum/

package main

func twoSum(nums []int, target int) []int {
	prevMap := make(map[int]int)

	for i, n := range nums {

		diff := target - n

		if index, ok := prevMap[diff]; ok {

			return []int{index, i}
		}

		prevMap[n] = i
	}

	return []int{}
}
