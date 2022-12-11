# staff version validation and outcomes
# display multiple outcomes
# saves progression outcomes in a list
# display horizontal histogram

from student_version import add_title_border,validate_credits,progression_outcome

# define and assign values for the variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progression_outcome_list = []
progression_credit_list = []

# color codes when exiting program and to display progression outcome
CRED = "\033[91m" #red
CBLUE = "\033[34m" #blue
CEND = "\033[0m"  #white

def reset_stored_data(): 
    """Resets the variables to its initial values"""
    
    global pass_credits,defer_credits,fail_credits,progress_count,trailer_count,retriever_count,exclude_count,progression_credit_list,progression_outcome_list
    pass_credits = 0
    defer_credits = 0
    fail_credits = 0
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0
    progression_outcome_list = []
    progression_credit_list = []


def horizontal_histogram():
    """ Print a horizontal histogram based on the progression outcomes """
    if not progression_outcome_list:
        print("No data available! Please make a new record.")

    else:
        global progress_count,trailer_count,retriever_count,exclude_count
        progress_count = progression_outcome_list.count("Progress")
        trailer_count = progression_outcome_list.count("Progress (module trailer)")
        retriever_count = progression_outcome_list.count("Do not progress - module retriever")
        exclude_count = progression_outcome_list.count("Exclude")

        title = "                               H O R I Z O N T A L   H I S T O G R A M\n"
        print("\n-------------------------------------------------------------------------------------------------------")
        print(title)
        print("PROGRESS\t",progress_count,"\t: ","*"*progress_count)
        print("TRAILER\t\t",trailer_count,"\t: ","*"*trailer_count)
        print("RETRIEVER\t",retriever_count,"\t: ","*"*retriever_count)
        print("EXCLUDED\t",exclude_count,"\t: ","*"*exclude_count)
        print(f"\n{progression_outcome_list.__len__()} outcomes in total")
        print("-------------------------------------------------------------------------------------------------------")

# part 2
def display_data_in_terminal():
    """ Display the listed data on screen
    parameters -> the 2 lists which store the progression outcomes and their credits in numerical form"""
    if not progression_outcome_list:
        print("No data available! Please make a new record.")

    else:
        title = "                              A L L   P R O G R E S S I O N  O U T C O M E S\n"
        print("\n-------------------------------------------------------------------------------------------------------")
        print(title)
        
        print("Progression Outcome".ljust(52) + "Credits\n")
        list_length = len(progression_outcome_list)
        for i in range(list_length):
            print(progression_outcome_list[i].ljust(50), progression_credit_list[i])
        print("\n-------------------------------------------------------------------------------------------------------")
    
# part 3
def save_in_text_file():
    """ Saves multiple progression outcomes in a file. 
    Parameters -> list of outcomes and the credit list """

    file_path = "text_file_cw.txt"
    file_data = open(file_path, "w",encoding="UTF-8")
    
    # writes all the data into a txt file
    list_length = len(progression_outcome_list)
    for i in range(list_length):
        outcome = progression_outcome_list[i].ljust(50)
        result = f"\n{outcome}  {progression_credit_list[i]}"
        file_data.write(result)
    file_data.close()

    print("Data saved in text file!!!\n\tfile path: ",file_path)

    # reads the file and display data in terminal
    read_file = input("\nEnter 'Y'(or any key) to read the data in text file or 'Q' to exit program : ").lower()
    if read_file != "q":
        read_text_file()
    else:
        print(CRED + "'Q ENTERED. EXITING STAFF VERSION..." + CEND)

def read_text_file():
    if not progression_outcome_list: # Notifies the user if the program is displaying data recorded in the last program run
        print(CRED,"\nDisplaying data recorded in the last program run...",CEND)

    print("\n-------------------------------------------------------------------------------------------------------")
    print("                                          F I L E    D A T A")
    file_data = open("text_file_cw.txt","r",encoding="UTF-8")
    print(file_data.read())
    file_data.close()
    print("\n-------------------------------------------------------------------------------------------------------")

# Extention of the staff version
def extention_menu():
    """ Menu option to choose to display listed progression outcomes and file handeling"""

    global progression_outcome_list,progression_credit_list
    menu_option = input("Enter 'Y'(or any key) to view all the data in terminal and 'Q' to quit the program : ").lower()
    if menu_option != "q":
        display_data_in_terminal() # part 2

        # File Handeling
        menu_option = input("\nEnter 'Y'(or any key) to save the data in a text file and 'Q' to quit the program : ").lower() 
        if menu_option != "q":
            save_in_text_file() # part 3
        else:
            print(CRED + "'Q' ENTERED. EXITING STAFF VERSION..." + CEND)
          
    else:
        print(CRED + "'Q' ENTERED. EXITING STAFF VERSION..." + CEND)

# Main Staff Program
def staff_main():
    reset_stored_data() # reset all the variables to it's initial value
    global pass_credits,defer_credits,fail_credits

    title = " S T A F F    V E R S I O N  -  N E W    R E C O R D "
    add_title_border(title)
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
                    continue # program continues to ask user for valid input

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
                break      # exit the loop when user enters q

    if run_program == 'q':
        horizontal_histogram() # display horizontal histogram
    extention_menu() # menu to display all the data in terminal, file saving or exit

def program_options():
    title = " S T A F F    V E R S I O N "
    add_title_border(title)
    print()

    run_staff = True
    while run_staff is True:

        print("                             S T A F F   V E R S I O N    -    M E N U")

        program_options = input("\n\t1. Enter a New Record\n\t2. View Saved Data Records\n\t3. Return to Main Menu\nOption number: ")
        if program_options == "1":
            staff_main()
        elif program_options == "2":
            sub_menu = True

            while sub_menu is True:
                print("\n                  S T A F F    V E R S I O N  -  S A V E D   R E C O R D S  M E N U")
                sub_option = input("\n\t1. View Horizontal Histogram\n\t2. Display Saved Data\n\t3. Display File Data\n\t4. Return to Menu\nOption number: ")
                if sub_option == "1":
                    horizontal_histogram()
                elif sub_option == "2":
                    display_data_in_terminal()
                elif sub_option == "3":
                    read_text_file()
                elif sub_option == "4":
                    sub_menu = False
                else:
                    print("Option Not Recognized")
        elif program_options == "3":
            run_staff = False
        else:
            print("Option Not Recognized")
    print("\n-------------------------------------------------------------------------------------------------------")
        
    
if __name__ == "__main__":
    program_options()
