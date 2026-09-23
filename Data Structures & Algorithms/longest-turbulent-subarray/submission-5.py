class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 2
        m = 2
        if len(arr) == 1 or len(arr) == 0:
            return len(arr)
        s = set(arr)
        if len(s) == 1:
            return 1
        while r < len(arr):
            print(l)
            print(r)
            if arr[r-1] > arr[r-2]:
                if arr[r] < arr[r-1]:
                    r += 1

                else:
                    l = r - 1
                    r += 1
            elif arr[r-1] < arr[r-2]:
                if arr[r] > arr[r-1]:
                    r += 1
                else:
                    l = r - 1
                    r += 1
                
            else:
                l = r - 1
                r += 1
            m = max(m, r - l)
        return m
