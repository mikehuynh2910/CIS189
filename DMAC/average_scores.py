"""
Program: average_scores.py
Author: Sang Huynh
Last date modified: 06/12/2022

The purpose of this program is to practice with basic function
"""

def main():
    try:
        #Input your first name, your last name, your age
        last_name = input("Enter Last Name : ")
        first_name = input("Enter First Name : ")
        if first_name.isnumeric() == True or last_name.isnumeric() == True:
            raise Exception("Error! Have to insert the String!")
        age = int(input("Enter your age : "))
        num_scores = 3
        # num_scores which will be used to cacluate average, and this is constant
        #Get score from screen by user input
        score1 = int(input("Enter first score : "))
        score2 = int(input("Enter second score: "))
        score3 = int(input("Enter third score : "))
        if score1 < 0 or score2 < 0 or score3 < 0 or age < 1:
            raise Exception("Error! Insert a positive number!")
    except Exception as e:
        print(e)
    else:
        #find average score
        avg = (score1 + score2 + score3)/num_scores
        # print the required output
        print(last_name, ",", first_name, "age:", age, "average grade:%.2f" % avg)

    if __name__ == "__main__":
        main()
