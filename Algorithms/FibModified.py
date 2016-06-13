# Enter your code here. Read input from STDIN. Print output to STDOUT

f0, f1, n = (int(i) for i in raw_input().strip().split())

result_dict = {}

def fib(n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    if n in result_dict:
        return result_dict[n]
    else:
        result_dict[n] = pow(fib(n-1),2) + fib(n-2)
        return result_dict[n]

result = 0
for i in range(n):
    result = fib(i)
print result