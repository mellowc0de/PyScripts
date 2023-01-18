# Factorial Example - without recursion
# 1! = 1
# 2! = 2*1=2 = 2 * factorial(1)
# 3! = 3*2*1=6 = 3 * factorial(2)
# 4! = 4*3*2*1=24 = 4 * factorial(3)
# 5! = 5*4*3*2*1=120 = 5 * factorial(4)

# def factorial(number):
#     if number == 1:
#         return 1
    
#     prev = 1
#     for i in range(2, number + 1):
#         prev *=i
#     return prev

# for num in range(1,11):
#     print(num, factorial(num))

# Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print('Factorial of 5 is:', factorial(5))