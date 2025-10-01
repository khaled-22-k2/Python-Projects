import re
import sys
import getpass

#defined dual
def strength_label(pw: str) -> str:
    if len(pw) <8:
        raise ValueError("the passwd is less then 8")
#use regular expression 
    has_lower= bool(re.search(r"[a-z]", pw))
    has_upper= bool(re.search("[A-Z]", pw))
    has_digit= bool(re.search("[0-9]", pw))
    has_symbol= bool(re.search("[A-Za-z0-9]", pw))

    score = sum([has_lower,has_upper,has_digit,has_symbol])
    if score == 1:
        return "very weak"
    elif score == 2:
        return "weak"
    elif score == 3:
        return "good"
    elif score == 4 and len(pw) > 12:
        return "very strong"
    else:
        return "strong"
#main code 
if __name__ == "__main__":
#loop for choices
    while True:
        print("choose what you want!")
        print("1. test a passwd")
        print("2. exit")

        choice = input("type your choice: ")
        if choice == "1":
#use getpass to input passwd
            password = getpass.getpass("type your passwd: ")
            try:
                label = strength_label(password)
                print(f"rate:  {label}")
            except ValueError as e:
                print("error: {e}")

        elif choice == "2":
            print("exit successfully")
            sys.exit(0)

        else:
            print("please choose from the list!")


#end of code 






