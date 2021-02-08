def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}
    for i,val in enumerate(nums):
        req = target - val
        if numMap.get(req) == None:
            numMap[val] = i
            continue
        return [numMap[req], i]
