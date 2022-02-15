    # This program calculates how many pizzas a group of student needs to order
    # 02/14/2022
    # CTI-110 P1HW2 - Pizza Order
    # Mateo Murillo
    #
# Enter number of students 
students = int(input('Enter number of students: '))
print()
# number of students multiply by 3 = the number of pizza slices each student will eat
pizza_slices = (students * 3)

# number of students divide by 2 = the number of needed pizzas 
pizzas = (students / 2)

# the following code prints out the input and output of the program
print('Number of Students: ', students)
print('Number of Pizza slices: ', pizza_slices)
print('Number of Pizzas needed: ', pizzas)

