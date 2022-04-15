# This program stores scores in a list and calculates a final grade
# 04/14/2022
# CTI-110 P5HW1 - Score List
# Mateo Murillo
#

#define function create list
def createList():
    #create a empty list
    data = []
    #loop for i
    n = int(input('How many scores do you want to enter? '))
    for i in range(0, n):
        score = int(input('Enter Score: '))
    #assign score input to score list
        data.append(score)
        #restart program if invalid score is entered
        if score<0 or score>100:
            print('\nINVALID Score entered!!!! \nScore should be between 0 and 100')
            return createList
    # return the score to store in the list
    return data


#Define function analyze data
def analyzeData(data):
    # IF data is empty then
    # return 0 for all values
    if data==None:
        print("List was not created")
        return  0,0,0
    # get mimimum from data
    minimum = min(data)
    # get total of data
    total = sum(data)
    # get average
    average = total/len(data)
    average = round(average)
    return minimum,total,average

def display(data,result):

    # initialise local variables
    # minimum, maximim, total, avergae with the value
    # from result

    minimum, total, average = result
    # IF data is empty then
    # print empty list
    if data==None:
        print("Orignal data: []")

    #     ELSE print orignal data
    else:
        print("")


    print("---------------------")
    print("Lowest Score: ", minimum)
    print("Average: ", average)

    # defining letter grades
    A_GRADE = 90
    B_GRADE = 80
    C_GRADE = 70
    D_GRADE = 60

    # assigning grade letter base on the average
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
    print("Grade: ", letterGrade)

    # If the data list is empty then print empty set
    if data ==None:
        print("Set: {}")
        return

    data = set(data)
    data.remove(min(data))
    print("Modified List: ",data)

#defining the menu
def menu():
    print("""-----------MENU-------------
1) Create List
2) Display Results
3) Exit
----------------------------------\n""")
    inp = int(input())
    #if input is not a menu option, show menu again
    if inp<1 or inp>3:
        # Call menu
        return menu()
    # return  user input
    return  inp

#defining main
def main():
    data = None
    # Runs until the user chooses to exit menu by typing 3
    while True:
        reply = menu()
        if reply == 1:
            data = createList()
        if reply == 2:
            display(data,list(analyzeData(data)))
        if reply == 3:
            exit(0)


if __name__=="__main__":
    main()
