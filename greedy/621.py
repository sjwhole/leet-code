from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        counter = Counter(tasks)
        while True:
            most_common = counter.most_common(n + 1)
            for task, cnt in most_common:
                counter.subtract(task)
                if counter[task] == 0:
                    del counter[task]
            if not counter:
                ans += len(most_common)
                break
            else:
                ans += n + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
