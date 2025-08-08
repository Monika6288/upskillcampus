import json
import string 
import random
from  pathlib import Path
from pprint import pprint

PASSWORD_LENGTH = 13

def gen_password():
    gen_lowerletter = random.choices(string.ascii_lowercase, k=4)
    gen_upperletter = random.choices(string.ascii_uppercase, k=4)
    gen_digits = random.choices(string.digits, k=4)
    gen_symbols = random.choices("!@#$%^&*?_-`~", k=4)

    password = random.choices(gen_lowerletter+gen_digits+gen_upperletter+gen_symbols, k=PASSWORD_LENGTH)
    joined_password = "".join(password)
    print(joined_password)

    

def save_password(name, password):
    current_saves =  Path("Passwords.json").read_text()
    
    user_passwords = [
        current_saves.replace("\"", "").strip("[]"),
        {"name":name, "password":password}
    ]
    upload_password = json.dumps(user_passwords)

    Path("Passwords.json").write_text(upload_password)

def Password_manager():
    print("Welcome to password manager ")
    print("type (open) to get saved password or type (gen)\n to generate password if you want leave password\n manager type exit and (save)")
    while True:
        
        user = input("/>> ").lower()

        if user == "open":
            open_pass = Path("Passwords.json").read_text()
            print(open_pass)
            continue
        elif user == "gen":
            gen_password()
            print("do you want to save this password")
            user_data = input("(y/n)>> ").lower()

            if user_data == "y":
                name = input(" type the name of password/>> ")
                password = input("copy genrated password and paste here/>>")
                save_password(name, password)
                print(f"password {password} has been saved under the name {name}")
            elif user_data == "n":
                pass
        elif user == "save":
            name = input("input name/> ")
            password = input("input password/> ")    
            save_password(name, password)
            print(f"password {password} has been saved under the name {name}")
        elif user =="exit":
            print("ok see  you later")
            break

        else:
            pass
            
        
if __name__ == "__main__":
    Password_manager()



    

