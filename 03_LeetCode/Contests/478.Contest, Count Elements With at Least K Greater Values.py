def countElements(self, nums: List[int], k: int) -> int:
        qualified = 0
        for i in range(len(nums)):
            strictlyGreater = 0
            for j in range(len(nums)):
                if strictlyGreater == k:
                    qualified += 1
                    break
                    if nums[j] > nums[i]:
                        strictlyGreater += 1
        return qualified



# JAVA
# not mine answer

class Solution {
    public int countElements(int[] nums, int k) {
        int n = nums.length;
        
        Arrays.sort(nums);
        
        int count = 0;

        if(k == 0) return n;
        for(int i = 0; i < n-k; i ++){
            if(nums[i] < nums[n-k]) count++;
        }
        return count;
    }
}


# Q1. Count Elements With at Least K Greater Values
# Medium
# 4 pt.
# You are given an integer array nums of length n and an integer k.

# An element in nums is said to be qualified if there exist at least k elements in the array that are strictly greater than it.

# Return an integer denoting the total number of qualified elements in nums.

#  

# Example 1:

# Input: nums = [3,1,2], k = 1

# Output: 2

# Explanation:

# The elements 1 and 2 each have at least k = 1 element greater than themselves.
# ​​​​​​​No element is greater than 3. Therefore, the answer is 2.

# Example 2:

# Input: nums = [5,5,5], k = 2

# Output: 0

# Explanation:

# Since all elements are equal to 5, no element is greater than the other. Therefore, the answer is 0.

#  

# Constraints:

# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k < n©leetcode