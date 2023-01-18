# def func(x, y, z):
#     return x + 4 * y + 5 * z
 
# print(func(1, z=2, y=3))

# def func(x):
#     if x == 0:
#         return 0
#     return x + func(x - 1)
 
# print(func(3))

# def func(x=2, y=3):
#     return x * y
 
# print(func(y=2, 3))

# def exp(num):
#     global result
#     result = num * num
 
# exp(5)
# print(result)


# part1 = 'test'
 
# def func(email, domain = 'rediff.com'):
#     domain = 'gmail.com'
#     print(email, domain, sep='@')
 
# part2 = 'yahoo.com'
 
# func(part1, part2)
# func(part1, 'hotmail.com')
# print(part1, part2, sep='@')

# def hash(n):
#     var = '#'
#     for i in range(n):
#         var += var
#     return var
 
# for _ in hash(1):
#     print(_, end='*')


# def Employee(name , id):
#     print(name,id)
    
# Employee(id=123,name = "Sandy")
# Employee(name = "Mandy" , id =234)
# Employee(name = "Candy" , 456)


# def f1():
#     global x
#     x = "Wow"*2
#     print(x)
#     x = 'welcome'
# x = 5
# f1()
# print(x)


# def week(day = 'Sunday'):
#     if day == 'Sunday':
#         print("Holiday")
#     else:
#         print("Working day")
 
# week()
# week('Monday')


def swap(a, b):
    a, b = b, a
    return (a, b)
 
a = "Python2"
b = "Python3"
a, b = swap(a, b)
print(a, b)