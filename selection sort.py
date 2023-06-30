class Solution: 
    def select(self, arr, i):
        minx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minx]:
                minx = j
        return minx
    def selectionSort(self, arr,n):
        for i in range(n-1):
            index = self.select(arr, i)
            arr[i], arr[index] = arr[index], arr[i]
        return arr
