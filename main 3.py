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
    
    
def saveNewEntry(my_dic, list_for_help_calc):
    while True:
        user_id = input("Enter Id Number ")
        user_age = input("Enter User Age ")
        if checkIfNumber(user_id) == True and checkIfNumber(user_age) == True:
            user_id = int(user_id)
            user_age = int(user_age)
            break
        else:
            print("Something Wrong, Id and Age Should Be a Numbers Try Again ")
    user_name = input("Enter User Name ")
    my_dic[user_id] = [user_name, user_age]  
    print("ID [" + str(user_id) + "] Added Succesfully")
    list_for_help_calc[0] = list_for_help_calc[0] + user_age
    list_for_help_calc[1] = len(my_dic)
    
        
def searchById(user_dict):
    id_search = int(input("Please What is The Id to look For "))
    if id_search in user_dict:  
        print("ID : " + str(id_search))
        print("Name : " + user_dict[id_search][0])
        print("Age : " + str(user_dict[id_search][1]))
    else:
        print("User Not Found ")
        

def printAgesAverage(list_help_calc):
    if list_help_calc[1] == 0:
        return print("There Is No Person to Calculate Age Average")
    avg = list_help_calc[0] / list_help_calc[1]    
    print("The Average of ALL Ages : is " + str(avg))
    
def printAllNames(user_dict):
    print("The Name Are : ")
    for user_name in user_dict:
        print(user_dict[user_name][0])
 
    
def printAllId(user_dict):
    print("The IDs Are : ")
    for name_of_id in user_dict:
        print(name_of_id)


def eXitFun():
    while True:
        yes_no = input("Are you Sure Want to Exit? y/n ")
        if yes_no == "y":
            return False
        elif yes_no == "n":
            return True
        else:
            print("You Can Choose just y/n")
        
        
def printAllEntry(user_dict):
    for user in user_dict:
        print("ID : " + str(user))
        print("Name : " + user_dict[user][0])
        print("Age : " + str(user_dict[user][1]))
        print("")

        
def SearChByIndex(user_dict):
    chosen_index = input("Please What Index you looking for ")
    if checkIfNumber(chosen_index) and int(chosen_index) < len(user_dict):
        chosen_index = int(chosen_index)
    for index, user in enumerate(user_dict):
        if chosen_index == index:
            print("ID : " + str(user))
            print("Name : " + user_dict[user][0])
            print("Age : " + str(user_dict[user][1]))
            print("")
            break
    print("Index Not Found ")
        
        
#Start From Here Main 
the_dict = {}
list_help_calc = [0, 0]
check_loop = True
while check_loop:
    mainScreen()
    user_choice = input("Please Enter Your Choice: ")
    if checkIfNumber(user_choice):
        user_choice = int(user_choice)
        if user_choice == 1:
            saveNewEntry(the_dict, list_help_calc)
        elif user_choice == 2:
            searchById(the_dict)
        elif user_choice == 3:
            printAgesAverage(list_help_calc)
        elif user_choice == 4:
            printAllNames(the_dict)
        elif user_choice == 5:
            printAllId(the_dict)
        elif user_choice == 6:
            printAllEntry(the_dict)
        elif user_choice == 7:
            SearChByIndex(the_dict)
        elif user_choice == 8:
            check_loop = eXitFun()    
    else:
        input("The [" + user_choice + "] Dosnt Exist PRESS ENTER tO Chose Another One")
    input("Press Enter to Continue")    
print("GoodBye")    

    


