class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        total = 0

        for i in range(len(nums1)):
            total += abs(nums1[i] - nums2[i])

        sorted_nums1 = sorted(nums1)
        max_improvement = 0

        for i in range(len(nums1)):
            old_diff = abs(nums1[i] - nums2[i])

            left = 0
            right = len(sorted_nums1)

            while left < right:
                mid = (left + right) // 2

                if sorted_nums1[mid] < nums2[i]:
                    left = mid + 1
                else:
                    right = mid

            if left < len(sorted_nums1):
                new_diff = abs(sorted_nums1[left] - nums2[i])
                max_improvement = max(
                    max_improvement,
                    old_diff - new_diff
                )

            if left > 0:
                new_diff = abs(sorted_nums1[left - 1] - nums2[i])
                max_improvement = max(
                    max_improvement,
                    old_diff - new_diff
                )

        return (total - max_improvement) % MOD