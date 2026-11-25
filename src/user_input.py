import re   
from datetime import datetime, date

def ask_username ():
    while True:
        name = input("Enter your name:").strip()
        if len(name) > 0 and name.lower() not in ["admin", "root", "moderator", "mod", "null"]:
            break
        else: 
            print("Enter a valid name! You should not use the words admin, root, moderator, mod, null")
    return name

def ask_mail():
    while True:
        mail = input("enter your mail: ").strip()
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if len(mail) > 0 and re.match(pattern, mail) is not None:
            break
        else:
            print("You should enter your mail!")
    return mail

def ask_display_name():
    while True:
        display_name = input("Pls enter your display name:").strip()
        pattern = "^[A-Za-z][A-Za-z0-9_]*$"

        if len(display_name) == 0:
            display_name = ask_username()
            break
        elif len(display_name) >= 3 \
        and len(display_name) <= 20 \
        and re.match(pattern, display_name) \
        and display_name.lower() not in ["admin", "root", "moderator", "mod", "null"] :
            break
        else:
            print("Please respect the name format!")

    return display_name

def ask_birth_date():
    while True:
        birth_date = input("Pls enter your birthdate:").strip()
        pattern = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$"

        if re.fullmatch(pattern, birth_date):

            try:

                birth_transformed = datetime.strptime(birth_date, "%d/%m/%Y").date()
                if birth_transformed > date.today():
                    print("Please enter the date in the past!")
                else:
                    return birth_transformed
                
            except ValueError("Pls use correct date format!"):
                print("Pls enter the correct date format!")

        else:print("Pls respect the date format!")
            
    

        
