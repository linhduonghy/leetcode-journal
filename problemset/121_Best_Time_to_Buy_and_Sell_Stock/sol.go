package main

func maxProfit(prices []int) int {

	minElement := prices[0]
	maxProfit := 0

	for _, cur := range prices {
		if cur-minElement > maxProfit {
			maxProfit = cur - minElement
		}

		if cur < minElement {
			minElement = cur
		}
	}
	return maxProfit
}