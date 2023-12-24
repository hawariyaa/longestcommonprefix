# longest common prefix
# what we want here is to see if how many of the letters form each array are similar in prefix way
# example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# bescially checking if the first letter is simalr and is the second letter simialr
# if they are to return those
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
str = ["happy", "hanny", "hawi"]
answer = Solution()
new = answer.longestCommonPrefix(str)
print(new)
