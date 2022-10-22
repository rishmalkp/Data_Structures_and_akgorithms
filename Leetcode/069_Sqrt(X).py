'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        m=(l+h)>>1
        while l<=h:
            if m*m==x:
                return m
            elif m*m>x:
                h=m-1
            else:
                l=m+1
            m=(l+h)>>1
        return m