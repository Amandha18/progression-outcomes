# saves the outcomes in a text file 
# display file data in terminal
# option to open it in notepad

import webbrowser

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

# part 2
# displaying listed data in terminal
def display_data_in_terminal(progression_outcome_list,progression_credit_list):
    title = "  A L L   P R O G R E S S I O N  O U T C O M E S - S T A F F   V E R S I O N \n"
    print("\n-------------------------------------------------------------------------------------------------------")
    print(title)
    
    print("Progression Outcome".ljust(52) + "Credits\n")
    for i in range(len(progression_outcome_list)):
        print(progression_outcome_list[i].ljust(50), progression_credit_list[i])
    print("\n-------------------------------------------------------------------------------------------------------")
    
# part 3
# writing and reading data from a file
def save_in_text_file(progression_outcome_list,progression_credit_list):
    file_path = "text_file_cw.txt"
    file_data = open(file_path, "w")
    
    # writes all the data into a txt file
    file_data.write("PROGRESSION OUTCOMES AND CREDITS LIST - FILE DATA\n")
    for i in range(len(progression_outcome_list)):
        outcome = progression_outcome_list[i].ljust(50)
        result = f"\n{outcome}  {progression_credit_list[i]}"
        file_data.write(result)
    file_data.close()

    print("Data saved in text file!!!\n\tfile path: ",file_path)

    # reads the file and display data in terminal
    read_file = input("\nEnter 'Y'(or any key) to read the data in text file or 'Q' to exit program : ").lower()
    if read_file != "q":
        file_data = open(file_path,"r")
        print(file_data.read())
        file_data.close()

        # opens file as a text file/in notepad
        open_file = input("\nEnter 'Y'(or any key) to view all the data in a text file(notepad) or 'Q' to exit program : ").lower()
        if open_file != "q":
            webbrowser.open(file_path)
            print(CRED + "END OF STAFF VERSION. RETURNING TO MAIN MENU..." + CEND)
        else:
            print(CRED + "EXITING STAFF VERSION..." + CEND)
    else:
        print(CRED + "EXITING STAFF VERSION..." + CEND)
