# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:05:24 2019

@author: Administrator
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        d = self.construct_dict(wordList)
        queue, visited = deque([(beginWord, 1)]), set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    neigh_words = d.get(s, [])
                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))
            
        return 0
        
    def construct_dict(self, word_list):
        
        d = {}
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                d[s] = d.get(s, []) + [word]
        
        return d

if __name__ == '__main__':

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = Solution().ladderLength(beginWord, endWord, wordList)
