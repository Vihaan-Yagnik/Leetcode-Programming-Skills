class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i = 1
        sub = arr[i-1] - arr[i]

        for i in range(2,len(arr)):
            if arr[i-1] - arr[i] != sub:
                return False

        return True


