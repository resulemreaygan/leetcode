/*
Author: Resul Emre AYGAN
*/

package _go

func containsDuplicate(nums []int) bool {
	if len(nums) <= 1 {
		return false
	}

	resultSet := make(map[int]struct{})

	for _, num := range nums {
		if _, isExists := resultSet[num]; isExists {
			return true
		}

		resultSet[num] = struct{}{}
	}

	return false
}
