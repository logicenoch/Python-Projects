# #if the first operand is false, retrun otherwise return
# #the second operand.
# print(0 or 30)
# print(10 or 100)
# print(200 or 0)
# print(not 0)

# #Use of "in" to check

# if 'E' in 'Okeke Enoch Chibuzo':
#     print("Enoch dey on ground")
# else:
#     print("D good boy no dey on ground")

# #Use of "in" to loop
# for i in "okeke Enoch Chibuzo":
#     print(i, end="")

# print("\r")

# #Using "is" to check objects identity
# #string is immutable
# #hence occupy same memory location
# print(' ' is ' ')

# #Using "is" to check objects identity
# #Dictionary is mutable
# #hence occupy diff. memory location
# print({} is {})

# Global variable
# count = 5

# def some_func():
#     global count
#     count = count + 1
#     print(count)
# some_func()

# Chains of characters
# s = 1+2+3 +\
#     4+5+6 +\
#     7+8+9
# print(s)
print("My name is {} and I'm {}years old!".format('Okeke Enoch', int(2)))

#We can also specify the position of the objects
print("{0} - {1}".format('England', 'Britain'))
print("{1} - {0}".format('England', 'Britain'))

#We can also format with the f-strings
print(f"I love {'Geeks'} for \"{'Geeks'}\"")

#We can also use dictionary 
data = {'Soup': 12, 'Beans': 36 , 'Drinks' : 10 }
print("Soup: {0[Soup]:d}, Beans: {0[Beans]:d}, Drinks: {0[Drinks]:d}".format(data))

data = dict(fun = "Geeks for Geeks", adj = "Portal")
print("I love {fun} computer {adj}".format(**data))

#Formating using the string method

cstr = "I love CodeWithLogic"

print("Center aligned string with fillchr: " )
print(cstr.center(40, '#'))

print("Left aligned string with fillchr: " )
print(cstr.ljust(40, '-'))

print("Center aligned string with fillchr: " )
print(cstr.rjust(40, '-'))






