# Student Version with Validations and the Progression Outcome
# Install tabulate using pip install tabulate

import time
from part1_staff_version import staff_main
from tabulate import tabulate # used to draw the border in the title

def validate_credits(credits):
    if credits > 120 or credits < 0 or credits % 20 != 0:
        print("Out of range")
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

# Main Program
def main():
    
    title = "S T U D E N T    V E R S I O N"
    print(tabulate([[title]],tablefmt="fancy_grid"))
    print()
    
    while True:
        try:
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

        except ValueError:
            print("Integer Required")
            continue

        else:
            print(tabulate([["Your Progression Outcome: ",outcome]],tablefmt="simple_outline"))
            print("\n\n")
            break

if __name__ =='__main__':
    main()
    time.sleep(3)
    staff_main() # after main is excecuted the program loops to the staff version
