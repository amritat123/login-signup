import json
def sign_up():
    username=input("please enter your  user name:-")
    password1=input("please create your  password:- ")
    password2=input("confrom your password: ")
    dict={}
    if password1!=password2:
        print("both passward are not same😏")
    else:
        if "a" in password1 or "b" in password1 or "c" in password1 or "d" in password1 or "e" in password1 or "f" in password1 or "g" in password1 or "h" in password1 or "i"in password1 or "j" in password1 or "k" in password1 or "l" in password1 or "m" in password1 or "n" in password1 or "o" in password1 or "p"in password1 or "q" in password1 or "s" in password1 or "t" in password1 or "u" in password1 or "v" in password1 or "w"in password1 or "x" in password1 or "y" in password1 or "z"in password1:
            if "@" in password1 or "#" in password1 or "$" in password1:
                if "1" in password1 or "2" in password1 or "3" in password1 or "4" in password1 or "5" in password1 or "6" in password1 or "7" in password1 or "8"in password1 or "9"in password1:               
                    with open("main.json","r") as file:
                            all_data = json.load(file)
                    i=0
                    while i<len(all_data["user"]):
                        file=(all_data["user"][i])
                        if file["username"]==username:
                            print("**************😏you alredy exist😏 *****************")
                            break
                        i+=1
                    else:
                        dict["username"]=username
                        dict["passward"]=password1
                        all_data["user"].append(dict)

                        with open("main.json","w") as my_file:
                            json.dump(all_data,my_file,indent=4)
                        print()
                        print("congress",username,"😇your account sign-up sucessfully😇")
                        print()
                        details=input("enter the discreption:---😇")
                        Birthday_date=input("enter the birthday date😍:---")
                        Hobbis=input("enter the hobbis😍:---")
                        Gender=input("enter the gender😍:---")
                        dict_bio={}
                        dict_bio["Descreption"]=details
                        dict_bio["dob"]=Birthday_date
                        dict_bio["Hobbis"]=Hobbis
                        dict_bio["Gender"]=Gender
                        dict["profile"]=dict_bio
                        with open("main.json","w") as my_file:
                            json.dump(all_data,my_file,indent=4)
                else:
                    print("oops! number are not in password")
            else:
                print("sorry! special character are not in strong password")
        else:
            print("sorry ! alphabet are not in strong password ")
def login():
    my_username=input("please! enter the user name for login :")
    password_1=input("please enter the password for login :")
    my_data=open("main.json", "r")
    data=json.load(my_data)
    # print(data)
    my_data.close()
    i=0
    while i<len(data["user"]):
        file=(data["user"][i])
        if file["username"]==my_username:
                print(my_username, "😇!your account is login successfully:-😇")
                print("-------------------------------------------------")
                print()
                print("*****************😈your profile😈***********************")
                print()
                print("Username:-",my_username)
                print("Gender:-", file['profile']['Gender'])
                print("Bio:-", file['profile']["Descreption"])
                print("Hobbis:-", file['profile']['Hobbis'])
                print("Hobbis:-",file['profile']['Hobbis'])
                print("Dob:-", file['profile']['dob'])
                break
        i=i+1
    else:
         print("sorry! invalid username😈")
def main():
    print("WELCOME! login/signup:-:-")
    print("------------------------------------------------")
    print("enter the sign up and login 1/2=")
    print("-------------------------------------------------")
    user_want=input("do you want to sign-up😍 login your account😍:-")
    print("-----------------------------------------------------")
    if user_want=="1":
        sign_up()
    elif user_want=="2":
        login()
    else:
        print("sign_up or login😍")
main()


