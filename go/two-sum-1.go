/*
Author: Resul Emre AYGAN
*/

package _go

func twoSum(nums []int, target int) []int {
	indexSet := make(map[int]int)

	for index, number := range nums {
		tempNumber := target - number

		if tempIndex, ok := indexSet[tempNumber]; ok {
			return []int{tempIndex, index}
		}

		indexSet[number] = index
	}
	return nil
}
