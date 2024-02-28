"""
def fib(n):
    if n == 1 or n==2:
        return 1
    else:
        return fib(n- 1) + fib(n - 2)
print (fib(6))
"""
def fib(n, calls_cont):
    if  n in calls_cont:
        return calls_cont[n]
    
    elif n == 0:
         calls_cont[n] = (1, 0)
         return calls_cont[n]
    elif n == 1:
         calls_cont[0] = (1, 1)
    else:
        fib_n_1, fib1= fib(n - 1, calls_cont)
        fib_n_2, fib2= fib(n - 2, calls_cont)
        call_total = fib_n_1 + fib_n_2 + 1
        fib_result = fib1 + fib2

        calls_cont[n] = (call_total, fib_result)
        return calls_cont[n]
test = int(input())

for num in range(test):
    n = int(input())
    rest, num_calls = fib(n,{})
print(f"fib = {num_calls - 1} calls = {rest}")