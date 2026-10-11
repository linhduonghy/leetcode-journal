package main

func intersect(nums1 []int, nums2 []int) []int {
    
    
    result := []int{}
    
    counter := [1001]int {}
    
    for _, value := range nums1 {
        counter[value] += 1
    }
    
    for _, value := range nums2 {
        if counter[value] > 0 {
            result = append(result, value)
            counter[value] -= 1
        }
    }
    
    
    return result
}