# import collections
#
# return an array including the max of sliding window
# @param arr int整型一维数组 the arr
# @param w int整型 the window size
# @return int整型一维数组
#
class Solution:
    def slidingwindowMax(self , arr , w ):
        # write code here
        res = [max(arr[:w])]
        stack = [max(arr[:w])]
        for r in range(w, len(arr)):
            # if queue[0] == arr[r - w]:
                # queue.popleft()
            while stack and stack[-1] < arr[r]:
                stack.pop()
            stack.append(arr[r])
            if stack[0] == arr[r - w]:
                stack.pop(0)
            res.append(stack[0])
                
            
        return res
    
if __name__ == "__main__":
    arr = [314333,887675,216887,-330381,-242884,695988,-547708,-560572,-298552,35784]
    w = 3
    print(Solution().slidingwindowMax(arr, w))
