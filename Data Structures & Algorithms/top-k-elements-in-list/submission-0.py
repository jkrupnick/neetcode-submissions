class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        mode = []

        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]] = 1
        for i in range(k):
            currMode = max(my_dict,key=my_dict.get)
            mode.append(currMode)
            my_dict.pop(currMode)
        return mode
                

        