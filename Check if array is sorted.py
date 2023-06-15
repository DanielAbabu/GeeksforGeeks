def arraySortedOrNot(self, arr, n):
        left=0
        right=1
        while right<n:
            if arr[left]>arr[right]:
                return 0
            left+=1
            right+=1
        return 1
