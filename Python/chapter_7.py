# airtime_remaining = 15
# print (airtime_remaining)
# airtime_remaining = 7
# print(airtime_remaining )

# n = 5
# n = 3 * n + 1
# print (n)

# for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     invitation = 'Hi ' + f + '. Please come to my party on Saturday!'
# 
#     print(invitation)
# import sys
# def mysum(xs):
#     '''Sum all numbers in the list xs, and return the total. '''
#     runing_total= 0
#     for x in xs :
#         runing_total = runing_total + x
#     return runing_total

# def test(did_pass):
#     "Print The result of the test"
#     linenum = sys._getframe(1).f_lineno
#     if did_pass:
#         msg = 'Test at line {0} ok.'.format(linenum)
#     else :
#         msg = 'Test at line {0} failed.'.format(linenum)
#     print (msg)

# def sum_to(n):
#     ss = 0 
#     v = 1
#     while v <=n :
#         ss = ss + v
#         v = v + 1
#     return ss

# def sum_to(n):
#     ss = 0 
#     for v in range (n+1):
#         ss = ss + v
#     return ss

# def seq3np1(n):
#     while n != 1:
#         print(n, end = ', ')
#         if n % 2 == 0:
#             n = n //2
#         else:
#             n = n * 3 + 1
#     print(n, end = ".\n")
# seq3np1(3)
# seq3np1(19)
# seq3np1(21)
# seq3np1(16)

# def num_zero_and_five_digits(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         if digit == 0 or digit == 5:
#             count = count + 1
#         n = n // 10
#     return count
# print
# def num_digits(n):
#     count = 0
#     while n != 0:
#         count = count + 1
#         n = n // 10
#     return count
# print(num_digits(710))

# import random
# rng = random.Random()
# number = rng.randrange(1,100)
# gueses = 0
# msg = ""

# while True:
#     guess = int (input(msg + '\nGuess my number between 1 and 1000:'))
#     gueses += 1
#     if guess > number:
#         msg += str(guess) + 'is to high.\n'
#     elif guess > number :
#         msg += str(guess) + ' is to low.\n'
#     else:
#         break
# input("\n\nGreat, you got it in {0} guesses!\n\n".format(gueses))

# for i in [12,16,17,24,29,30]:
#     if i % 2 == 1:
#         continue
#     print(i)
# print('done')

# def print_mult_table(high):
#     for i in range(1, high+1):
#         print_multiples(i)

# def print_multiples(n, high):
#     for i in range (1, high+1):
#         print(n * i, end="   ")
#     print()

# def print_mult_table(high):
#     for i in range (1, high+1):
#         print_multiples(i, high)
# print_mult_table(7)

# def test_suite():
#     test(mysum([1,2,3,4]) == 10)
#     test(mysum([1.25,2.5,1.75]) == 5.5)
#     test(mysum([1,-2,3]) == 2)
#     test(mysum([ ]) == 0)
#     test(mysum(range(11)) == 55)
#     test(sum_to(4) == 10)
#     test(sum_to(1000) == 500500)
#     test(num_zero_and_five_digits(1055030250) == 7)
# test_suite()
# students = [("John", ["CompSci", "Physics"]),
# ("Vusi", ["Maths", "CompSci", "Stats"]),
# ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
# ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
# ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
# for (name, subjects) in students:
#     print(name,"takes",len(subjects), 'courses')
# counter = 0
# for (name, subjects)in students:
#     for s in subjects:
#         if s == "CompSci":
#             counter +=1
# print("The number of student taking CompSci is ",counter)

# def sqrt (n):
#     approx = n /20
#     while True:
#         better = (approx + n / approx)/2.0
#         if abs (approx - better) < 0.0001:
#             return better
#         approx = better
# print(sqrt(25.0))
import sys

# 1. Write a function to count how many odd numbers are in a list.
def odd_number(n):
    odd = 0
    for number in n:
        if number %2 == 1 :
            odd +=1
    return odd
# 2. Sum up all the even numbers in a list
def sum_even (n):
    odd_even = 0
    for number in n :
        if number %2 == 0:
            sum += number
    return odd_even
# 3. Sum up all the negative numbers in a list.
def negative_number(n):
    negative = -1
    for number in n :
        if number < 0:
            negative += number
    return negative
# 4. Count how many words in a list have length 5.
def sum_word (w):
    odd_word = 0
    for word in w :
        if len(word) == 5 :
            odd_word += 1
    return odd_word

# 5. Sum all the elements in a list up to but not including the first even number. (Write your unit
# tests. What if there is no even number?)
def without_first(n):
    total = 0
    first = True
    for num in n :
        if first == True and num %2 == 0:
            first == False
            continue
        else:
            total += num
    return total
# 6. Count how many words occur in a list up to and including the first occurrence of the word
# “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
def count_word(w):
    counter = 0
    for word in w :
        if word== 'sam':
            break
        else:
            counter +=1
    return counter

# 7. Add a print function to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.
def sqrt(n):
    counter = 0
    approx = n/2.0 
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs (approx - better) < 0.001:
            return better,counter
        counter += 1

# 8. Trace the execution of the last version of print_mult_table and figure out how it works.

def mult_table(t):
    res = ''
    for i in range (1,7):
        res += (t * 1) + '\t'
    res += '\t\n'
    return res
def print_mult_table():
    text = ''
    for i in range (1,7):
        print('Iterasi' (i))
        text += print_mult_table(i)
        print (text)

# 9. Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A
# call to print_triangular_numbers(5) would produce the following output:
# 1 1 1
# 2 2 3
# 3 3 6
# 4 4 10
# 5 5 15
# (hint: use a web search to find out what a triangular number is.)
def triangular_number(n):
    counter = 0
    result = 0
    for i in range (n) :
        counter +=1
        result += counter
        print (counter, '\t',result)
