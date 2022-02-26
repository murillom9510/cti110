    # This program createst a list of scores and outputs the average
    # 02/25/2022
    # P2HW2 - Score Avg
    # Mateo Murillo
    #

# Ask the user the enter the scores
num1 = input('Enter Score #1: ')
num2 = input('Enter Score #2: ')
num3 = input('Enter Score #3: ')
num4 = input('Enter Score #4: ')
num5 = input('Enter Score #5: ')
num6 = input('Enter Score #6: ')
num7 = input('Enter Score #7: ')

# stores the scores in a list
scores_list = list(map(int,(num1, num2, num3, num4, num5, num6, num7)))

#lowest number 
low = min(scores_list)

#removes lower score from the list
scores_list.remove(min(scores_list))

# adds up all the scores
total = sum(scores_list)


# adds up the list and divides it by its lenght 
avg = total/len(scores_list)

# rounds up the total by two decimals
avg = round(avg, 2)

#display lowest number, modified list and average
print("Lowest number:",low)
print('Average:',avg)
print('Modified List:', scores_list)

