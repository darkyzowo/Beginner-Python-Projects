# Given 2 integers, find their sum

def calc(number1, number2):
    sum_total = number1 + number2
    product = number1 * number2
    return sum_total, product

number1 = int(input())
number2 = int(input())

sum_total, product = calc(number1, number2)

if product <= 1000:
    print("The result is", product)
else:
    print(sum_total)
