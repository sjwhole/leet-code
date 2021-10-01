from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_valid(now, cnt):
            for i in range(now + 1, now + cnt + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        idx = 0
        while idx < len(data):
            cur = data[idx]
            if (cur >> 7) == 0:
                idx += 1
            elif (cur >> 5) == 0b110 and is_valid(idx, 1):
                idx += 2
            elif (cur >> 4) == 0b1110 and is_valid(idx, 2):
                idx += 3
            elif (cur >> 3) == 0b11110 and is_valid(idx, 3):
                idx += 4
            else:
                return False
        return True
