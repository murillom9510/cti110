    # This program adds up multiple items then adds taxes and prints the output
    # 02/25/2022
    # CTI-110 P2HW1 - Total Purchases
    # Mateo Murillo
    #
# Ask the user the enter the store item prices
num1 = input('Enter price of item #1: ')
num2 = input('Enter price of item #2: ')
num3 = input('Enter price of item #3: ')
num4 = input('Enter price of item #4: ')
num5 = input('Enter price of item #5: ')

# adds up all the items
sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)

#adds the taxes to the items and rounds it up to two decimal points
taxes = (sum * 0.07)
taxes = round(taxes, 2)

#adds the taxes and subtotal to get the final result and rounds it up to two decimal points
total = (taxes + sum)
total = round(total, 2) 

print('Subtotal: ', sum)
print('Sales Tax: ', taxes)
print('Total: ', total)