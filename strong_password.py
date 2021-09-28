def strong_password():

    password=input("please enter the strong password :-")
    if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i"in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p"in password or "q" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w"in password or "x" in password or "y" in password or "z"in password:
        if "@" in password or "#" in password or "$" in password:
            if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8"in password or "9"in password:
                print("congrates this is strong password")
            else:
                print("oops! special charactor are not in password")
        else:
            print("sorry! numbers are not in strong password")
    else:
        print("sorry ! alphabet are not in strong password ")
strong_password()





        



                    