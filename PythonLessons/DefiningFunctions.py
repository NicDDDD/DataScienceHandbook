# Defiinng Functions

# Lambda expression

sqr = lambda x: x*x
five_squared = sqr(5)


def squared_func(x):
    return x*x

srq2 = squared_func(5)


def apply_to_evens(a_list,a_func):
    return [a_func(x) for x in a_list if x%2==0]

my_list = [1,2,3,4,5,6,7,8]
sqrs_of_evens = apply_to_evens(my_list, lambda x:x*x)

