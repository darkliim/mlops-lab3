import re   

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
            print("espece de batard, lises bien les regles avant de rentrer ton putan de merde de prenom")

    return display_name
