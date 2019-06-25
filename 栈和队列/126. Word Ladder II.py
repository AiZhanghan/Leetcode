# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:20:47 2019

@author: Administrator
"""
from collections import deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        d = self.construct_dict(wordList)
        q = deque()
        q.append([beginWord, [beginWord]])
        visited = set()
        visited.add(beginWord)
        
        while q:
            word, path = q.popleft()
            
#            if word == endWord:
#                res.append(path)
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                neigh_words = d.get(s, [])
                for neigh in neigh_words:
                    if neigh not in visited:
                        if neigh == endWord:
                            new_path = path + [neigh]
                            if not res:
                                res.append(new_path)
                            elif res and len(res[0]) == len(new_path):
                                res.append(new_path)
                        else:
                            new_path = path + [neigh]
                            q.append([neigh, new_path])
                            visited.add(neigh)
            
        return res
        
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
    res = Solution().findLadders(beginWord, endWord, wordList)
