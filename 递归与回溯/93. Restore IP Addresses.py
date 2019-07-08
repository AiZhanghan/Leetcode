# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:45:12 2019

@author: Administrator
"""
class Solution:
    def restoreIpAddresses(self, s):
        
        solutions = []
        self.restore_ip(s, solutions, 0, '', 0)
        return solutions
        
    def restore_ip(self, ip, solutions, idx, restored, count):
        
        if count > 4:
            return
        
        if count == 4 and idx == len(ip):
            solutions.append(restored)
            
        for i in range(1, 4):
            if idx + i > len(ip):
                break
            s = ip[idx: idx + i]
            if (s[0] == '0' and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            self.restore_ip(ip, 
                            solutions, 
                            idx + i, 
                            restored + s + ('' if count == 3 else '.'),
                            count + 1)

if __name__ ==  '__main__':
    s = "25525511135"
    res = Solution().restoreIpAddresses(s)