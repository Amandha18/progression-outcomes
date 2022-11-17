# Student Version with Validations and the Progression Outcome
# Install tabulate using pip install tabulate

from part1_staff_version import staff_main
from part4_dictionary import dictionary_program_main

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

# add border around the title
def add_title_border(text):
    # unicodes for box drawing 
    # double line
    # https://en.wikipedia.org/wiki/Box-drawing_character#Unicode

    horizontal = "\u2550"
    top_left_corner ="\u2554"
    top_right_corner = "\u2557"
    vertical = "\u2551"
    bottom_right_corner ="\u255D"
    bottom_left_corner = "\u255A"

    print(top_left_corner+horizontal*(len(text)+10)+top_right_corner)
    print(vertical+f"     {text}     "+vertical)
    print(bottom_left_corner+horizontal*(len(text)+10)+bottom_right_corner)

# box the progression outcome of the student
def add_outcome_border(text):
    # unicodes for box drawing 
    # single line
    # https://en.wikipedia.org/wiki/Box-drawing_character#Unicode

    horizontal = "\u2500"
    top_left_corner ="\u250C"
    top_right_corner = "\u2510"
    vertical = "\u2502"
    bottom_left_corner ="\u2514"
    bottom_right_corner = "\u2518"
    sectioning_down = "\u252C"
    sectioning_up = "\u2534"

    print(top_left_corner+horizontal*26+sectioning_down+horizontal*(len(text)+5)+top_right_corner)
    print(vertical+"Your Progression Outcome: "+vertical+f" {text}    "+vertical)
    print(bottom_left_corner+horizontal*26+sectioning_up+horizontal*(len(text)+5)+bottom_right_corner)

# validates whether credits are lower or equal than 120 and divisible by 20
def validate_credits(credits): 
    if credits > 120 or credits < 0 or credits % 20 != 0:
        print("Out of range")
    else:
        return True

# returns the progression outcome based on pass credits and fail credits
def progression_outcome(pass_credits,fail_credits): 
    if pass_credits == 120:
        outcome = "Progress"
    elif pass_credits == 100:
        outcome = "Progress (module trailer)"
    elif fail_credits == 120 or fail_credits == 100 or fail_credits == 80:
        outcome = "Exclude"
    else:
        outcome = "Do not progress - module retriever"
    return outcome

# Student Version Main Program
def student_main():
    
    title = "S T U D E N T    V E R S I O N"
    add_title_border(title)
    print()
    
    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
            if validate_credits(pass_credits) is True:
                if pass_credits == 120:  # if credits add upto 120, it returns the outcome
                    outcome = progression_outcome(pass_credits,0)
                else: # if credits does not add upto 120, ask the user for other credits
                    defer_credits = int(input("Please enter your credits at defer: "))
                    if validate_credits(defer_credits) is True:
                        if pass_credits + defer_credits == 120:
                            outcome = progression_outcome(pass_credits,0)
                        elif pass_credits + defer_credits > 120:
                            print("Total Incorrect")
                            continue
                        else:
                            fail_credits = int(input("Please enter your credits at fail: "))
                            if validate_credits(fail_credits) is True:
                                if pass_credits + defer_credits + fail_credits == 120:
                                    outcome = progression_outcome(pass_credits,fail_credits)
                                else:
                                    print("Total Incorrect")
                                    continue
                            else:
                                continue
                    else:
                        continue
            else:
                continue

        except ValueError: # user input is not an integer
            print("Integer Required")
            continue

        else:
            add_outcome_border(outcome)
            print()
            break
    print(CRED + "END OF STUDENT VERSION. RETURNING TO MAIN MENU.." + CEND)
    

if __name__ =='__main__':

    title = "P R O G R E S S I O N   O U T C O M E  - C O U R S E W O R K"
    add_title_border(title)
    print()

    # main menu with 4 options
    while True:
        version_number = input("\nChoose an option from the Menu\n\t1.Student Version\n\t2.Staff Version\n\t3.Staff Version with Dictionary\n\t4.Exit the Program\nEnter Option: ")
        print()
        if version_number == "1":
            student_main()
        elif version_number == "2":
            staff_main()
        elif version_number == "3":
            dictionary_program_main() 
        elif version_number == "4":
            print(CRED + "Option 4 entered. \nEXITING PROGRAM. THANK YOU!" + CEND)
            exit()
        else:
            print("Input not Recognized")
        
       
