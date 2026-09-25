class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        toReturn = []
        for num in s1:
            if num in s2:
                toReturn.append(num)

        return toReturn
