from collections import defaultdict
from typing import List


def is_palindrome(word: str):
    return word == word[::-1]


class TrieNode:
    def __init__(self):
        self.palindrome_word_ids = []
        self.word_id = -1
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, idx, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(idx)
            node = node.children[char]
            node.val = char
        node.word_id = idx

    def search(self, idx, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if is_palindrome(word):
                    result.append([idx, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != idx:
            result.append([idx, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([idx, palindrome_word_id])

        return result


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results += trie.search(i, word)

        return results
