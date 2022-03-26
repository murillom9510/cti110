
    # This program will display number of slices and pizzas depending on number of people per pizza. The program also ask the user if he wants to run it again at the end.
    # 03/25/2022
    # CTI-110 P3HW2 - Pizza Order 3.0
    # Mateo Murillo
    #

import math 

# creating a while loop that runs when = True
while True:
# Enter number of students 
    students = int(input('How many students do you want to order pizza for? '))
# enter number of people per pizza
    people = float(input('Enter number of people per pizza (1.5, 2 or 3): '))


# if people per pizza is valid then calculate the number of pizzas and price
    if people == 1.5 or people == 2 or people == 3:
        whole_pizzas = math.ceil(students / people)
        price = whole_pizzas * 5
        price = price + (price * 0.06)
        price = '%.2f' % round(price, 2)
        print('----Pizza Order-------')
        print('Number of Students: ', students)
        print('Pizzas Needed: ', whole_pizzas)
        print('Price: $', price)
        print('-----------------------')
 # ask user if they want to run the program again and to answer by entering N or Y       
        again=str(input('Would you like to run program again type (Y for yes) or (Enter any other key to exit program): '))
        if again == 'Y':
            again = True
        else: 
            break
 # if the input for people per pizza is invalid then else runs        
    else:
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2 or 3')
# program will keep asking for a valid number for the people per pizza until a valid number is entered
        people = float(input('\nEnter number of people per pizza again. (1.5, 2 or 3): '))
        if people == 1.5 or people == 2 or people == 3:
            whole_pizzas = math.ceil(students / people)
        price = whole_pizzas * 5
        price = price + (price * 0.06)
        price = '%.2f' % round(price, 2)
        print('----Pizza Order-------')
        print('Number of Students: ', students)
        print('Pizzas Needed: ', whole_pizzas)
        print('Price: $', price)
        print('-----------------------')
 # ask user if they want to run the program again and to answer by entering N or Y 
        again=str(input('Would you like to run program again type (Y for yes) or (Enter any other key to exit program): '))
        if again == 'Y':
            again = True
        else: 
            break


