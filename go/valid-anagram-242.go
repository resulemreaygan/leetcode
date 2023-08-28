/*
Author: Resul Emre AYGAN
*/

package _go

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	// rune for utf-8 char
	counts := make(map[rune]int)

	for _, value := range s {
		counts[value]++
	}

	for _, value := range t {
		counts[value]--

		if counts[value] < 0 {
			return false
		}
	}

	return true
}
