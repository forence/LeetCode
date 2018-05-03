class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        subStr = s[0]
        maxStrLen = 1
        for tail in range(1, len(s)):
            idx = subStr.find(s[tail])
            if idx == -1:
                subStr += s[tail]
            else:
                if len(subStr) > maxStrLen:
                    maxStrLen = len(subStr)
                subStr = subStr[idx + 1:] + s[tail]
        if len(subStr) > maxStrLen:
            maxStrLen = len(subStr)
        return maxStrLen



sol = Solution()
print sol.lengthOfLongestSubstring("cbc")
