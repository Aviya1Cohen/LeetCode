class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1    
        if n < 0:
            return 1/self.myPow(x, -n)
        if not n%2:
            return self.myPow(x*x, n/2)
            
        return x*self.myPow(x, n-1)
