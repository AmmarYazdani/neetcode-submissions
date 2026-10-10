class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        left = 0
        right = len(numbers) - 1


        while left < right :

            Sum = numbers[left] + numbers[right]

            if target - Sum < 0 :
                right -= 1
            elif target - Sum > 0 :
                left += 1
            elif target == Sum:
                res.append(left + 1)
                res.append(right + 1)
                break
            else:
                break
        return res
        
                
            


        