# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:28:13 2019

@author: 54949
"""
import re

class Solution:
    def wordBreak(self, s, wordDict):
        
        wordDict.sort(key = lambda x: len(x), reverse = True)
        self.memo = [None for _ in range(len(s) + 1)]
        
        return self.word_break(s, wordDict)
    
    def word_break(self, s, word_dict):
        '''
        能否break s
        '''
        if not s:
            return True
        # False
        if self.memo[len(s)] != None:
            return self.memo[len(s)]
        
        for i in range(len(word_dict)):
            if re.match(word_dict[i], s):
                res = self.word_break(re.sub(word_dict[i], '', s, count = 1), word_dict)
                if res:
                    self.memo[len(s)] = True
                    return True
        self.memo[len(s)] = False
        return False
                
if __name__ == '__main__':
    s = 'aaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    word_dict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    res = Solution().wordBreak(s, word_dict)