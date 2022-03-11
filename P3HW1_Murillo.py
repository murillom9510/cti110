    # This program converts grade numbers to a letter grade
    # 03/10/2022
    # CTI-110 P3HW1
    # Mateo Murillo
    #

def main():
 


    

 # prints please enter score and stores it
    
    score = float(input('Please enter score: '))
    
 # system uses 10-point grading scale, converts grade number to a letter then prints it out
    if score >= 90:
        print('Your grade is: A')
    elif 80 <= score < 90:
        print('Your grade is: B')
    elif 70 <= score < 80:
        print('Your grade is: C')
    elif 60 <= score < 70:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

main()