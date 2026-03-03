def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5)) 

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  