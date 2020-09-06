import itertools
from typing import List
from typing import Iterable

from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []

        # group words that are one distance apart
        wildCardGrouping = self.createWildCardGrouping(wordList)

        def findNeighbors(word: str) -> Iterable:
            return itertools.chain.from_iterable(
                wildCardGrouping[word[:i] + '*' + word[i+1:]]
                for i in range(len(word)))

        # Stores the words visited so far
        visitedWords, backwardPathTracker = {beginWord}, list()

        bfsWords = {beginWord}
        while bfsWords:
            newBfsWords, wordTracker = set(), defaultdict(list)

            for tailWord in bfsWords:
                for neighbor in findNeighbors(tailWord):
                    if neighbor not in visitedWords:

                        wordTracker[neighbor].append(tailWord)
                        newBfsWords.add(neighbor)

            visitedWords = visitedWords.union(newBfsWords)

            bfsWords = newBfsWords
            backwardPathTracker.append(wordTracker)

            if endWord in bfsWords:
                return self.recreatePathsFromPathTracker(endWord, backwardPathTracker)

        return []

    @staticmethod
    def createWildCardGrouping(wordList: List[str]) -> dict:
        grouping = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                grouping[word[:i] + '*' + word[i+1:]].append(word)
        return grouping

    @staticmethod
    def recreatePathsFromPathTracker(endWord: str, backwardPathTracker: List[dict]):
        wordPaths = [[endWord]]

        n = len(backwardPathTracker)
        for ind in reversed(range(n)):
            wordPaths = [
                [word] + wordPath
                for wordPath in wordPaths
                for word in backwardPathTracker[ind][wordPath[0]]]
        return wordPaths
