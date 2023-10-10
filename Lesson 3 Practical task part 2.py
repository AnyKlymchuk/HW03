A''' four-digit natural number is specified:
 - find the product of the digits of this number
 - write the number in reverse order
 - in ascending order, you need to sort the numbers included in the given number'''

number = int(input("Enter a four-digit natural number: "))

digit_1 = number % 10
digit_2 = (number // 10) % 10
digit_3 = (number // 100) % 10
digit_4 = (number // 1000) % 10

product_of_digits = digit_1 * digit_2 * digit_3 * digit_4
print(f"Product of the digits: {product_of_digits}")

reverse_number = int(str(number)[::-1])
print(f"Number in reverse order: {reverse_number}")

sorted_number = int(''.join(sorted(str(number))))
print(f"Number with digits sorted in ascending order: {sorted_number}")