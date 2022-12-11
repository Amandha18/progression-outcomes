from dictionary_version import dictionary_program_main
from student_version import add_title_border, student_main
from staff_version import program_options

# color codes when exiting program and to display progression outcome
CRED = "\033[91m" #red
CEND = "\033[0m"  #white

if __name__ =='__main__':

    title = "P R O G R E S S I O N   O U T C O M E  - C O U R S E W O R K"
    add_title_border(title)
    print()

    # main menu with 4 options
    while True:
        print("                              M A I N    M E N U")
        version_number = input("\nChoose the version\n\t\t1.Student Version\n\t\t2.Staff Version\n\t\t3.Staff Version with Dictionary\n\t\t4.Exit the Program\n\tEnter Option: ")
        print()
        if version_number == "1":
            student_main()
        elif version_number == "2":
            program_options()
        elif version_number == "3":
            dictionary_program_main()
        elif version_number == "4":
            print(CRED,"Option 4 entered. \nEXITING PROGRAM. THANK YOU!", CEND)
            exit()
        else:
            print("Input not Recognized")
