from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        Args:
            tasks: list[str]
            n: int
        
        Return:
            int
        """
        length = len(tasks)
        if length <= 1:
            return length
        
        task_map = Counter(tasks)
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        max_task_count = task_sort[0][1]
        res = (max_task_count - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] != max_task_count:
                break
            res += 1
        return res if res >= length else length