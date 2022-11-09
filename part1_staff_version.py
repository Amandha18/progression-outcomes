# staff version validation and outcomes
# saves progression outcomes in a list
# display horizontal histogram

from tabulate import tabulate # used to draw the border in the title
from part2_and_part3 import progression_outcome_list,progression_credit_list,display_data_in_terminal,save_in_text_file

# define and assign values for the variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

# color codes for exiting program and display progression outcome
CRED = "\033[91m" #red
CBLUE = "\033[34m" #blue
CEND = "\033[0m"  #white

def validate_credits(credits):
    if credits > 120 or credits < 0 or credits % 20 != 0:
        print("Out of range\n")
    else:
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

# Horizontal Histogram for the outcomes
def horizontal_histogram():
    global progress_count,trailer_count,retriever_count,exclude_count
    progress_count = progression_outcome_list.count("Progress")
    trailer_count = progression_outcome_list.count("Progress (module trailer)")
    retriever_count = progression_outcome_list.count("Do not progress - module retriever")
    exclude_count = progression_outcome_list.count("Exclude")

    title = "                   H O R I Z O N T A L   H I S T O G R A M\n"
    print("\n-------------------------------------------------------------------------------------------------------")
    print(title)
    print("PROGRESS\t",progress_count,"\t: ","*"*progress_count)
    print("TRAILER\t\t",trailer_count,"\t: ","*"*trailer_count)
    print("RETRIEVER\t",retriever_count,"\t: ","*"*retriever_count)
    print("EXCLUDED\t",exclude_count,"\t: ","*"*exclude_count)
    print(f"\n{progression_outcome_list.__len__()} outcomes in total")
    print("-------------------------------------------------------------------------------------------------------")

# Extentions of the staff version
# Menu option for listed output and text file handeling
def menu():
    menu_option = input("Enter 'Y'(or any key) to view all the data in terminal and 'Q' to quit the program : ").lower()
    if menu_option != "q":
        display_data_in_terminal()
        menu_option = input("\nEnter 'Y'(or any key) to save the data in a text file and 'Q' to quit the program : ").lower()
        if menu_option != "q":
            save_in_text_file()
        else:
            print(CRED + "'Q' ENTERED. END OF PROGRAM ..." + CEND)
            exit()
    else:
        print(CRED + "'Q' ENTERED. END OF PROGRAM ..." + CEND)
        exit()

# Main Staff Program
def staff_main():
    global pass_credits,defer_credits,fail_credits

    title = "S T A F F    V E R S I O N  -  H I S T O G R A M    I N C L U D E D"
    print(tabulate([[title]],tablefmt="fancy_grid"))
    print()
    run_program = "y"
    
    while run_program != "q":
        while True:
            try:
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
                # save the outcome and the credits in a list
                progression_outcome_list.append(outcome)
                progression_credit_list.append([pass_credits,defer_credits,fail_credits])
                print(CBLUE + f"Progression Outcome: {outcome} " + CEND)

                # ask user preference to enter multiple data
                run_program = input("Press 'Y' (or any key) to enter another set of data, or 'Q' to view the histogram: ")
                run_program = run_program.lower() 
                print() 
                break      

    if run_program == 'q':
        horizontal_histogram()
    menu() # menu to display all the data in terminal, file saving or exit

