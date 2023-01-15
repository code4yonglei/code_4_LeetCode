class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_ele = sum(nums)
        sum_digit = 0
        for num in nums:
            list_digits = str(num)
            sum_digit += sum([int(list_digit) for list_digit in list_digits])
        diff = sum_ele - sum_digit
        return diff if diff>0 else -diff 
