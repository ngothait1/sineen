def mainScreen():
    print("1. Save a New Entry")
    print("2. Search By Id")
    print("3. Print Ages Average")
    print("4. Print All Names")
    print("5. Print All IDs")
    print("6. Print All Entries")
    print("7. Print Entry By index")
    print("8. Exit")


def checkIfNumber(user_input):
    char_flag = True
    for num in user_input:
        if num != "9" and num != "8" and num != "7" and num != "6" and num != "5" and num != "4" and num != "3" and num != "2" and num != "1" and num != "0":
           char_flag = False
    return char_flag
    
    
def userChoseone(my_dic):
        while True:
            user_id = input("Enter Id Number ")
            user_age = input("Enter User Age ")
            if checkIfNumber(user_id) and checkIfNumber(user_age) == True:
                user_id = int(user_id)
                user_age = int(user_age)
                break
            else:
                print("Something Wrong, Id and Age Should Be a Numbers Try Again ")
        user_name = input("Enter User Name ")
        my_dic[user_id] = [user_name, user_age]  
        print("ID [" +str(user_id)+ "] Added Succesfully")
        input("Press Enter To Continue")
        return my_dic
        
def userChoseTwo(user_dict):
    id_search = int(input("Please What is The Id to look For "))
    if id_search in user_dict:  
        print("ID : " +str(id_search))
        print("Name : " +user_dict[id_search][0])
        print("Age : " +str(user_dict[id_search][1]))
        input("Press Enter to Continue")
    else:
        input("User Not Found, Press Enter To Back to Main")
        

def userChoseThree(user_dict):
    sum = 0
    for age in user_dict:
        sum += user_dict[age][1]
    avg = sum / len(user_dict)    
    return avg
    
def userChoseFour(user_dict):
    print("The Name Are : ")
    for names in user_dict:
        print(user_dict[names][0])
    input("Press Enter to Continue")
    
def userChoseFive(user_dict):
    print("The IDs Are : ")
    for names in user_dict:
        print(names)
    input("Press Enter to Continue")

def userChoseEight():
    yes_no = input("Are you Sure Want to Exit? y/n ")
    if yes_no == "y":
        return False
    elif yes_no == "n":
        return True
    else:
        print("You Can Choose just y/n")
        userChoseEight()
        
def userChoseSix(user_dict):
    for user in user_dict:
        print("ID : " +str(user))
        print("Name : " +user_dict[user][0])
        print("Age : " +str(user_dict[user][1]))
        print("")
        input("Press Enter to Continue")
        
def userChoseSeven(user_dict):
    chosen_index = input("Please What Index you looking for ")
    if checkIfNumber(chosen_index):
        chosen_index = int(chosen_index)
    for index, user in enumerate(user_dict):
        if chosen_index == index:
            print("ID : " +str(user))
            print("Name : " +user_dict[user][0])
            print("Age : " +str(user_dict[user][1]))
            print("")
            input("Press Enter to Continue")
            break
    input("Index Not Found,Press Enter To Back to Main")
        
        
#Start From Here Main 
the_dict = {}
check_loop = True
while check_loop:
    mainScreen()
    user_choice = input("Please Enter Your Choice: ")
    if checkIfNumber(user_choice):
        user_choice = int(user_choice)
    if user_choice == 8:
        check_loop = userChoseEight()
    elif user_choice == 1:
         userChoseone(the_dict)
    elif user_choice == 2:
         userChoseTwo(the_dict)
    elif user_choice == 3:
         print("The Average of ALL Ages : is " +str(userChoseThree(the_dict)) )
         input("Press Enter to Continue")
    elif user_choice == 4:
        userChoseFour(the_dict)
    elif user_choice == 5:
        userChoseFive(the_dict)
    elif user_choice == 6:
        userChoseSix(the_dict)
    elif user_choice == 7:
        userChoseSeven(the_dict)
    else:
        input("The [" +user_choice+ "] Dosnt Exist PRESS ENTER tO Chose Another One")
print("GoodBye")    

    


