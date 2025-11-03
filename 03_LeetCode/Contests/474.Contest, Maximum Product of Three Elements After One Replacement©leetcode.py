def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        nums.sort()
        return nums[len(nums)-1]*nums[len(nums)-2]*100000