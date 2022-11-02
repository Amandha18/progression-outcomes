# saves the outcomes in a list
# saves the outcomes in a text file and open it in notepad
import webbrowser

progression_outcome_list = []
progression_credit_list = []

def display_data_in_terminal():
    title = "  A L L   P R O G R E S S I O N  O U T C O M E S - S T A F F   V E R S I O N \n"
    print("\n-------------------------------------------------------------------------------------------------------")
    print(title)
    
    print("Progression Outcome".ljust(52) + "Credits\n")
    for i in range(len(progression_outcome_list)):
        print(progression_outcome_list[i].ljust(50), progression_credit_list[i])

def save_in_text_file():
    file_path = "text_file_cw.txt"
    file_data = open(file_path, "w")
    
    file_data.write("PROGRESSION OUTCOMES AND CREDITS LIST\n")
    result = "\n".join("{} \t-\t {}".format(x, y) for x, y in zip(progression_outcome_list, progression_credit_list))
    file_data.write(result)
    file_data.close()

    print("Data saved in text file!!!\n\tfile path: ",file_path)

    open_file = input("\nEnter 'Y' to view all the data in text file : ").lower()
    if open_file == "y":
        webbrowser.open(file_path)
    else:
        exit()