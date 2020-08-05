class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        Args:
            numerator: int
            denominator: int
        
        Return:
            str
        """
        if numerator == 0:
            return "0"
        
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        if not b:
            return "".join(res)
        
        res.append(".")
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            loc[b] = len(res)
        return "".join(res)
