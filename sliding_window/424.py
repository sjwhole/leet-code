from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = right = 0

        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1

            if right - left - counter.most_common(1)[0][1] > k:
                counter[s[left]] -= 1
                left += 1

        return right - left
