func runningSum(nums []int) []int {
    sums := []int{}
    sum := 0
    for i := 0; i < len(nums); i++ {
        sum = sum + nums[i]
        sums = append(sums, sum)
    }
    return sums
}