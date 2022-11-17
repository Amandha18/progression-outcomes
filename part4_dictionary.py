# dictionary program
# can enter multiple records and saves it in a dictionary

# define variables and dictionary
student_progression_outcomes = {}
pass_credits = 0
defer_credits = 0
fail_credits = 0

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

# reseting values entered in a previous program
def reset_values():
    global student_progression_outcomes,pass_credits,defer_credits,fail_credits
    student_progression_outcomes = {}
    pass_credits = 0
    defer_credits = 0
    fail_credits = 0

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

# box the progression outcomes
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

    print(top_left_corner+horizontal*21+sectioning_down+horizontal*(len(text)+5)+top_right_corner)
    print(vertical+"Progression Outcome: "+vertical+f" {text}    "+vertical)
    print(bottom_left_corner+horizontal*21+sectioning_up+horizontal*(len(text)+5)+bottom_right_corner)

# check whether the student id have the requirements
# first letter should be w and it should end with 7 digits
def validate_student_id(student_id):
    valid = False
    if len(student_id) == 8 and student_id.startswith('w'):
        letters_list = [letter for letter in student_id]
        for i in range(1,len(student_id)):
            if letters_list[i].isnumeric():
                valid = True
            else:
                valid = False
                break
    if valid is False:
        print("Inavlid Student ID\t e.g : w1234567, W1234567")
        return False

def validate_credits(credits):
    if credits > 120 or credits < 0 or credits % 20 != 0:
        print("Out of range\n")
    else:
        return True

# check whether the studnet record is already in the dictionary
def check_duplicate_student_id(student_id):
    if student_id in student_progression_outcomes:
        print(CRED,"Student ID already exist in the dictionary",CEND)
        reenter_entry = input("\nPress 'Y'(or any key) if you wish to re-enter student scores or 'Q' to quit: ").lower()
        if reenter_entry == 'q': # skip from re entering the student credits
            return True

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

# Main Program
def dictionary_program_main():
    reset_values() # reset the data that was entered earlier
    global pass_credits,defer_credits,fail_credits,student_progression_outcomes
    
    title = "P R O G R E S S I O N   O U T C O M E :  P A R T  4  -  D I C T I O N A R Y"
    add_title_border(title)
    print()

    run_program = "y"
    
    while run_program != "q":
        while True:
            try:
                # get student ID from user
                student_id = input("\nEnter student ID : ").lower()
                if validate_student_id(student_id) is False: # validate the student id format
                    continue
                if check_duplicate_student_id(student_id) is True: # check whether the student id already exist in the dictionary
                    continue

                # get credits from user
                pass_credits = int(input("Please enter credits at pass: "))
                if validate_credits(pass_credits) is True:
                    if pass_credits == 120:
                        outcome = progression_outcome(pass_credits,0)
                    else:
                        defer_credits = int(input("Please enter credits at defer: "))
                        if validate_credits(defer_credits) is True:
                            if pass_credits + defer_credits == 120:
                                outcome = progression_outcome(pass_credits,0)
                            elif pass_credits + defer_credits > 120:
                                print("Total Incorrect\n")
                                continue
                            else:
                                fail_credits = int(input("Please enter credits at fail: "))
                                if validate_credits(fail_credits) is True:
                                    if pass_credits + defer_credits + fail_credits == 120:
                                        outcome = progression_outcome(pass_credits,fail_credits)
                                    else:
                                        print("Total Incorrect\n")
                                        continue
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue

            except ValueError:
                print("Integer Required\n")
                continue
            
            else:
                # diplay student number and outcome
                add_outcome_border(outcome)
                print("\n")

                # save the student no, progression outcome in a list
                progression_outcome_string = (f"{outcome} - {pass_credits},{defer_credits},{fail_credits}")
                student_progression_outcomes[student_id] = progression_outcome_string

                # user input to run program multiple times
                run_program = input("Press 'Y' (or any key) to enter another set of data, or 'Q' to view the dictionary: ")
                run_program = run_program.lower() 
                break

    if run_program == "q":
        print("\nS T U D E N T   P R O G R E S S I O N   O U T C O M E S\n")
        # Iterate over the keys in dictionary, access value & print line by line
        for key in student_progression_outcomes:
            print(key, ' : ', student_progression_outcomes[key])

        print(CRED + "\nEND OF STAFF PROGRAM - DICTIONARY VERSION. RETURNING TO MAIN MENU..." + CEND)
        
