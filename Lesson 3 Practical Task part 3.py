'''Interchange the values of two variables without using the third variable.'''

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a = a + b
b = a - b
a = a - b

print("After interchange:")
print("a =", a)
print("b =", b)