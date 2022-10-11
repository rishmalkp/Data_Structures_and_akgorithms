"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position==0:
        return 0
    r=[-1]*(position+1)
    r[0]=0
    r[1]=1
    
    for i in range(2, position+1):
        r[i]= r[i-1]+r[i-2]
        
    return r[position]

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
