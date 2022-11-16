# saves the outcomes in a text file 
# display file data in terminal
# option to open it in notepad

import webbrowser

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

def display_data_in_terminal(progression_outcome_list,progression_credit_list):
    title = "  A L L   P R O G R E S S I O N  O U T C O M E S - S T A F F   V E R S I O N \n"
    print("\n-------------------------------------------------------------------------------------------------------")
    print(title)
    
    print("Progression Outcome".ljust(52) + "Credits\n")
    for i in range(len(progression_outcome_list)):
        print(progression_outcome_list[i].ljust(50), progression_credit_list[i])

def save_in_text_file(progression_outcome_list,progression_credit_list):
    file_path = "text_file_cw.txt"
    file_data = open(file_path, "w")
    
    # writes all the data into a txt file
    file_data.write("PROGRESSION OUTCOMES AND CREDITS LIST\n")
    result = "\n".join("{} \t-\t {}".format(x, y) for x, y in zip(progression_outcome_list, progression_credit_list))
    file_data.write(result)
    file_data.close()

    print("Data saved in text file!!!\n\tfile path: ",file_path)

    # reads the file and disaply data in terminal
    print()
    file_data = open(file_path,"r")
    print(file_data.read())
    file_data.close()

    # opens file as a text file/notepad
    open_file = input("\nEnter 'Y'(or any key) to view all the data in a text file or 'Q' to exit program : ").lower()
    if open_file != "q":
        webbrowser.open(file_path)
    else:
        print(CRED + "END OF PROGRAM file ..." + CEND)
        
    
