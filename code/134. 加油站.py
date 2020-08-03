class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        Args:
            gas: list[int]
            cost: list[int]
        
        Return:
            int
        """
        total_tank = 0
        cur_tank = 0
        start_position = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            if cur_tank < 0:
                cur_tank = 0
                start_position = i + 1
        return start_position if total_tank >= 0 else -1


# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         """
#         Args:
#             gas: list[int]
#             cost: list[int]
        
#         Return:
#             int
#         """
#         res = -1
#         for i in range(len(gas)):
#             if gas[i] >= cost[i] and self.can_complete_circuit(gas, cost, i):
#                 res = i
#                 break
#         return res
    
#     def can_complete_circuit(self, gas, cost, start):
#         """
#         Args:
#             gas: list[int]
#             cost: list[int]
#             start: int
        
#         Return:
#             bool
#         """
#         res = True
    
#         pre_state = gas[start]
#         pre = start
#         for _ in range(len(gas)):
#             if pre_state >= cost[pre]:
#                 cur = (pre + 1) % len(gas)
#                 cur_state = pre_state - cost[pre] + gas[cur]
#                 pre = cur
#                 pre_state = cur_state
#             else:
#                 res = False
#                 break
#         return res


# if __name__ == "__main__":
#     gas = [1, 2, 3, 4, 5]
#     cost = [3, 4, 5, 1, 2]
#     print(Solution().canCompleteCircuit(gas, cost))