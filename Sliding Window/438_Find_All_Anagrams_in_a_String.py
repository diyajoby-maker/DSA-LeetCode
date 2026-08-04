class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = {}
        win_count = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        left = 0
        result = []

        for right in range(len(s)):
            win_count[s[right]] = win_count.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                win_count[s[left]] -= 1

                if win_count[s[left]] == 0:
                    del win_count[s[left]]

                left += 1

            if win_count == p_count:
                result.append(left)

        return result
