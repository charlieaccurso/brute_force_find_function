class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if haystack[i] == needle[0]: # a match occurs
                if i + len(needle) > len(haystack): # needle extends past the length of haystack
                    return -1
                
                else:
                    match_index= i
                    needle_index= 0
                    while match_index < i + len(needle):
                        if haystack[match_index] == needle[needle_index]:
                            match_index+= 1
                            needle_index+= 1
                            if match_index == i + len(needle):
                                return i
                        else:
                            break
        return -1
                
