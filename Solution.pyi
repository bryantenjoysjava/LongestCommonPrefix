class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(string) for string in strs)
        prefix = ""
        for i in range(min_len):
            char = [string[i] for string in strs]
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break

        return prefix






