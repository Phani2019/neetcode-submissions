class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        groups = defaultdict(int)
        for num in nums:
            groups[num] += 1
        return [
            num for num, count in groups.items()
            if count > len(nums) // 3
        ]