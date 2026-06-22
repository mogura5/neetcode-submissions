class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0
        right = 1
        partial_sum = 0
        
        while right < len(s):

            partial_sum += abs(ord(s[right]) - ord(s[left]))
            left += 1
            right += 1


        
        return partial_sum

        


            