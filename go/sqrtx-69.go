/*
Author: Resul Emre AYGAN
*/

package _go

func mySqrt(x int) int {
	// Binary Search

	left := 0
	right := x

	for left <= right {
		mid := (left + right) / 2

		if mid*mid == x {
			return mid
		}

		if mid*mid < x {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return right
}
