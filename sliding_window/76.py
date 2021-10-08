from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        cnt = len(t)
        needs = Counter(t)

        left = 0
        for right, char in enumerate(s, 1):
            cnt -= needs[char] > 0
            needs[char] -= 1

            if cnt == 0:
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1
                if not end or right - left < end - start:
                    start, end = left, right

                needs[s[left]] += 1
                left += 1
                cnt += 1

        return s[start: end]
