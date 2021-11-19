from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            ans.append(l + r)
                        elif expression[i] == "-":
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        return ans
