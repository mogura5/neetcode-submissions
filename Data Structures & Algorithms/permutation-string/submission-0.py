class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        window = ""

        while right <= len(s2) - 1:
 
            window = ''.join(s2[left:right + 1])

            count = Counter(window)
            count1 = Counter(s1)

            if count == count1:
                return True
            else:
                left += 1
                right += 1
        return False



        