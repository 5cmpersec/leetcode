class Solution:
	def findMedianSortedArrays(self, nums1, nums2):
		m,n = len(nums1), len(nums2)
		if m > n:
			nums1, nums2, m, n = nums2, nums1, n, m
		imin, imax, half_len = 0, m, (m+n) // 2
		while imin <= imax:
			i = (imin+imax) // 2
			j = half_len - i
			if i > 0 and nums1[i-1] > nums2[j]:
				imax = i - 1
			elif i < m and nums1[i] < nums2[j-1]:
				imin = i + 1
			else:
				if i == 0: max_of_left = nums2[j-1]
				elif j == 0: max_of_left = nums1[i-1]
				else: max_of_left = max(nums1[i-1], nums2[j-1])

				if i == m: min_of_right = nums2[j]
				elif j == n: min_of_right = nums1[i]
				else: min_of_right = min(nums1[i], nums2[j])

				if (m+n) % 2 == 1:
					return min_of_right
				return (max_of_left + min_of_right) / 2
			

if __name__ == '__main__':
	sol = Solution()
	print(sol.findMedianSortedArrays([1,3], [2]))
	print(sol.findMedianSortedArrays([1,2], [3,4]))
