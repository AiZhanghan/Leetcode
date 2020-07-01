class Solution:
    def isNumber(self, s):
        """
        :param s: str

        :return: bool
        """
        try:
            float(s)
            return True
        except Exception:
            return False
