#dictionary
from tabulate import tabulate

student_progression_outcomes = {}
pass_credits = 0
defer_credits = 0
fail_credits = 0

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

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
        exit()

def validate_credits(credits):
    if credits > 120 or credits < 0 or credits % 20 != 0:
        print("Out of range\n")
    else:
        return True

def check_duplicate_student_id(student_id):
    if student_id in student_progression_outcomes:
        print(CRED,"Student ID already exist in the dictionary",CEND)
        duplicate = input("\nPress 'Y'(or any key) if you wish to re-enter student scores or 'Q' to quit: ").lower()
        if duplicate == 'q':
            exit()

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
def main():
    global pass_credits,defer_credits,fail_credits,student_progression_outcomes
    
    title = "P R O G R E S S I O N   O U T C O M E   D I C T I O N A R Y"
    print(tabulate([[title]],tablefmt="fancy_grid"))
    print()

    run_program = "y"
    
    while run_program != "q":
        while True:
            try:
                # get student ID from user
                student_id = input("\nEnter student ID : ").lower()
                validate_student_id(student_id) # validate the student id format
                check_duplicate_student_id(student_id) # check whether the student id already exist in the dictionary

                # get credits from user
                pass_credits = int(input("Please enter your credits at pass: "))
                if validate_credits(pass_credits) is True:
                    if pass_credits == 120:
                        outcome = progression_outcome(pass_credits,0)
                    else:
                        defer_credits = int(input("Please enter your credits at defer: "))
                        if validate_credits(defer_credits) is True:
                            if pass_credits + defer_credits == 120:
                                outcome = progression_outcome(pass_credits,0)
                            elif pass_credits + defer_credits > 120:
                                print("Total Incorrect\n")
                                continue
                            else:
                                fail_credits = int(input("Please enter your credits at fail: "))
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
                print(tabulate([[student_id,outcome]],tablefmt="simple_outline"))
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

if __name__ =='__main__':
    main()

