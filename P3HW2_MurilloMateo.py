
    # This program will display number of slices and pizzas depending on number of people per pizza
    # 03/10/2022
    # CTI-110 P3HW2 - Pizza Order 2.0
    # Mateo Murillo
    #
# Enter number of students 
students = int(input('How many students do you want to order pizza for? '))
print()

# enter number of people per pizza
people_per = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
print()

# people per pizza option 1.5
students_one = students / 1.5
students_one = round(students_one)

# people per pizza option 2
students_two = students / 2
students_two = round(students_two)

# people per pizza option 3
students_three = students / 3
students_three = round(students_three)

#subtotals
subtotal_one = students_one * 5
subtotal_two = students_two * 5
subtotal_three = students_three * 5

#tax calculation
taxes_one = subtotal_one * 0.06
taxes_two = subtotal_two * 0.06
taxes_three = subtotal_three * 0.06

#final price subtotal + tax = total
total_one = subtotal_one + taxes_one
total_one = '%.2f' % round(total_one, 2)
total_two = subtotal_two + taxes_two
total_two = '%.2f' % round(total_two, 2)
total_three = subtotal_three + taxes_three
total_three = '%.2f' % round(total_three, 2)



# calculates the number of people per pizza and prints it out
if people_per == 1.5:
        print('----Pizza Order-------')
        print('Number of Students:',students)
        print('Pizzas Needed: ',students_one)
        print('Price $',total_one)
        print('-----------------------')
elif people_per == 2:
        print('----Pizza Order-------')
        print('Number of Students:',students)
        print('Pizzas Needed:',students_two)
        print('Price $',total_two)
        print('-----------------------')
elif people_per == 3:
        print('----Pizza Order-------')
        print('Number of Students:',students)
        print('Pizzas Needed:', students_three)
        print('Price $',total_three)
        print('-----------------------')
        
#outputs error message when invalid input is entered
else:
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2 or 3')
        print('Run program again')
