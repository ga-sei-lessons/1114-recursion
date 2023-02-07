# # lets make an error!
# def navel_gazer():
#     print("hmmm.....🤔")
#     # recursion is when a function invokes iteself
#     navel_gazer()


# navel_gazer() # start the recursive process

# base case -- this stops recursion from happening
# recursive case -- causes recursion to happen, always needs to drive state closer to the base case
# must invoke self recursive
# for (let i = 0; i < arr.length; i++) {
#     // block 
#     let my_num = 10
#     let my_string = 'hello'
# }

# function my_func() {
#     let my_num = 10
#     let my_string = 'hello'
#     my_func()
# }
# define a function that accepts a positve whole number as an argument 'n', and prints out all numbers between 0 and 'n'
# def print_to(n, current_num = 0): # current num is our recursive state
#     # solving this with iteration
#     # for i in range(0, n +1):
#     #     print(i)

#     # base case is we have reached n and printed all the nums
#     if current_num > n: 
#         return
    
#     # recursive case -- driving state towards the base case
#     print(current_num)
#     print_to(n, current_num + 1)


# print_to(20)

def reverse_print_to(n):
    # base case is n is 0, the lowest number we want to loop to
    if n == 0:
        return
    
    print(n)
    # recursive case -- use the arg as the state that drives towards the base case
    reverse_print_to(n - 1)

# reverse_print_to(500)

# calculate the sum of all values between 0 and a give number 'num'
# 5
# 5 + 4 + 3 + 2 + 1 = 15

def sum_to(num):
    # we will subract from num to get close to our base case
    if num == 0:
        return num
    
    # drive state towards base case + do recursive logic
    return num + sum_to(num - 1)

# allow python to recurse more
# import sys
# sys.setrecursionlimit(2000)
# print(sum_to(1998))

# detect if a string is a palindrome
# racecar
# aceca
# cec
# e

# anna
# nn
# 

# tomato
# False


def is_palindrome(str):
    # base case is the str has len of 0 or 1
    if len(str) < 2:
        return True

    # only recurse if the first letter equals the last letter
    if str[0] == str[len(str) - 1]:
        return is_palindrome(str[1:len(str) - 1])
    # stop recursion if they don't match
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("tomato"))
    