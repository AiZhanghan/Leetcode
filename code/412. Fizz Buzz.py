class Solution:
    def fizzBuzz(self, n):
        """
        Args:
            n: int
        
        Return:
            list[str]
        """
        res = []
        fizz_buzz_dict = {
            3: "Fizz",
            5: "Buzz"
        }

        for num in range(1, n + 1):
            num_str = ""
            for key in fizz_buzz_dict:
                if num % key == 0:
                    num_str += fizz_buzz_dict[key]
            if not num_str:
                num_str = str(num)
            res.append(num_str)
        
        return res
            