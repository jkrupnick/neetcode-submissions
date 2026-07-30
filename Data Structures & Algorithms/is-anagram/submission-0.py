class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}

        for char in s:
            if char in my_dict:
                my_dict[char]+=1
            else:
                my_dict[char]=1
        for char in t:
            if char in my_dict and my_dict[char]>0:
                my_dict[char]-=1
            else:
                return False
        if (my_dict[max(my_dict,key=my_dict.get)] > 0):
            return False
        else:
            return True
            
        