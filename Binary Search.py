class Solution:
    def findKthSmall(self, arr, k):
        # code here
        low = 1
        high = k + len(arr)

        while low < high:
            mid = (low + high) // 2

            removed = 0

            for num in arr:
                if num <= mid:
                    removed += 1

            remaining = mid - removed

            if remaining < k:
                low = mid + 1
            else:
                high = mid

        return low
