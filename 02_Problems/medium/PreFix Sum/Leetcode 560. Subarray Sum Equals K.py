class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        map = defaultdict(int)
        map[0] = 1

        for num in nums:
            prefixSum += num
            if prefixSum - k in map:
                count += map[prefixSum - k]
            map[prefixSum] += 1

        return count
    
    # Approach will be update later as i need to arrange some things for that.
    # 
    # 
    # 
    # 