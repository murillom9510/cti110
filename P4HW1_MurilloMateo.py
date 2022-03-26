    # This program createst a list of scores and outputs the average
    # 03/25/2022
    # P4HW1 - Score List
    # Mateo Murillo
    #

#Defining grades
A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60

# stores the scores in a list
score_list = []

# Ask the user the enter number of scores
n = int(input('How many scores do you want to enter? '))
for i in range(0, n):
    #ask user to enter each individual score
    score = int(input('Enter Score: '))
    #assign score input to score list
    score_list.append(score)
    #if score invalid then remove from the list and ask user to enter score again
    if score < 0 or score > 100:
        score_list.remove(score)
        print('\nINVALID Score entered!!!! \nScore should be between 0 and 100')
        score = int(input('Enter Score: '))

# prints lower score from the list
print('-------------Results----------')
print("Lowest Score: ", (min(score_list)))

#removes lower score from the list
score_list.remove(min(score_list))

#prints modified list
print("Modified List: ", score_list)

# adds up all the scores
total = sum(score_list)

# gives a value base on the lenght of the list
lenght = len(score_list)

#divides the total by the lenght to get the average
average = total/lenght
average = round(average)

#prints total average
print('Scores Average: ', average)

# Using if/elif/else to find letter grade
if average >= A_GRADE:
    letterGrade = 'A'
elif average >= B_GRADE:
    letterGrade = 'B'
elif average >= C_GRADE:
    letterGrade = 'C'
elif average >= D_GRADE:
    letterGrade = 'D'
#If grade not A,B,C or D
else:
    letterGrade = 'F'
#print letter grade
print('Grade: ', letterGrade)
print('------------------------------')


