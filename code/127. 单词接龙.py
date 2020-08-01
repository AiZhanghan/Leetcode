import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Args:
            beginWord: str
            endWord: str
            wordList: list[str]
        
        Return:
            int
        """
        if endWord not in wordList:
            return 0
        self.build_graph(wordList)

        queue = collections.deque()
        queue.append(beginWord)
        visited = set(beginWord)
        count = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    pattern = word[: i] + "*" + word[i + 1:]
                    for next_word in self.graph[pattern]:
                        if next_word == endWord:
                            return count + 1
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)
                    self.graph[pattern] = []
            count += 1
        return 0

    def build_graph(self, wordList):
        """
        Args:
            wordList: list[str]
        
        Return:
            dict{str: list[str]}
        """
        self.graph = collections.defaultdict(list)
        length = len(wordList[0])
        for word in wordList:
            for i in range(length):
                pattern = word[:i] + "*" + word[i + 1:]
                self.graph[pattern].append(word)

