x=8
y=78
z=x/y
print(z)
print('i  added a print statement ')

def factorial_recursive(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    
    

factorial_recursive('3.0')