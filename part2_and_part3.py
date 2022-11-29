# saves the outcomes in a text file 
# display file data in terminal

# color codes 
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

# part 2
def display_data_in_terminal(progression_outcome_list,progression_credit_list):
    """ Display the listed data on screen
    parameters -> the 2 lists which store the progression outcomes and their credits in numerical form"""

    title = "  A L L   P R O G R E S S I O N  O U T C O M E S - S T A F F   V E R S I O N \n"
    print("\n-------------------------------------------------------------------------------------------------------")
    print(title)
    
    print("Progression Outcome".ljust(52) + "Credits\n")
    list_length = len(progression_outcome_list)
    for i in range(list_length):
        print(progression_outcome_list[i].ljust(50), progression_credit_list[i])
    print("\n-------------------------------------------------------------------------------------------------------")
    
# part 3
def save_in_text_file(progression_outcome_list,progression_credit_list):
    """ Saves multiple progression outcomes in a file. 
    Parameters -> list of outcomes and the credit list """

    file_path = "text_file_cw.txt"
    file_data = open(file_path, "w",encoding="UTF-8")
    
    # writes all the data into a txt file
    file_data.write("PROGRESSION OUTCOMES AND CREDITS LIST - FILE DATA\n")
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
        file_data = open(file_path,"r",encoding="UTF-8")
        print(file_data.read())
        file_data.close()

    else:
        print(CRED + "EXITING STAFF VERSION..." + CEND)
