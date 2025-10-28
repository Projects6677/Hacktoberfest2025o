class Solution:
    def peakElement(self, arr):
        # Code here
        start, end = 0, len(arr) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == len(arr) - 1 or arr[mid] > arr[mid+1]):
                return mid
            
            # If left neighbor is greater, peak must be on left side
            elif mid > 0 and arr[mid-1] > arr[mid]:
                end = mid - 1
            
            # Otherwise, peak must be on right side
            else:
                start = mid + 1
        
        return -1
