class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # If partitionX is 0 it means nothing is there on the left side. Use -infinity for maxLeftX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # If partitionX is at end of array, use +infinity for minRightX
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is even
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1  # move left
            else:
                low = partitionX + 1  # move right
