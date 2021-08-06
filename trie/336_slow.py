from collections import defaultdict
from typing import List


def is_palindrome(word: str):
    return word == word[::-1]


class TrieNode:
    def __init__(self):
        self.end = -1
        self.idx = []
        self.children = defaultdict(TrieNode)


class Solution:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.idx.append(idx)
        node.end = idx

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        global i
        ans = []
        palindromes = [idx for idx, word in enumerate(words) if is_palindrome(word)]

        for idx, word in enumerate(words):
            self.insert(word, idx)

        for idx, word in enumerate(words):
            node = self.root

            if word == "":
                for i in palindromes:
                    if i != idx:
                        ans.append([i, idx])
                        ans.append([idx, i])
                continue

            reversed_word = word[::-1]

            for i, char in enumerate(reversed_word):
                if char not in node.children:
                    i -= 1
                    break

                node = node.children[char]

                if node.end != -1:
                    if is_palindrome(reversed_word[i + 1:]):
                        if node.end != idx:
                            ans.append([node.end, idx])
            if i == len(word) - 1:
                for j in node.idx:
                    if is_palindrome(words[j][i + 1:]) and len(words[j]) > len(word):
                        if [j, idx] not in ans:
                            ans.append([j, idx])

        return ans
