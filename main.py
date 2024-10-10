import os
import json
import pandas as pd
from Student import Student
from Employe import Employe
from Person import Person


def mainScreen():
    print("1. Save a New Entry")
    print("2. Search By Id")
    print("3. Print Ages Average")
    print("4. Print All Names")
    print("5. Print All IDs")
    print("6. Print All Entries")
    print("7. Print Entry By index")
    print("8. Save All Entry")
    print("9. Exit")


def saveAllDatatoFile(list_of_people):
    people_list = []
    my_path = os.getcwd()
    os.path.exists(my_path)
    try:
        with open("conf.json") as json_file:
            loaded_file = json.load(json_file)
        for person in list_of_people:
            people_list.append(person.informationToDic(loaded_file))
        output_file_name = input("What is Your Output File Name ? ")
        list_of_persons_df = pd.DataFrame(people_list)
        list_of_persons_df.to_csv(my_path + "//" + output_file_name, index=False)
        print("Saved Successfully ")
    except FileNotFoundError:
        print("The File conf.json in Not Exist in : " + my_path)


def functhatPrintPerson(person_list, index):
    person_list[index].printMySelf()


def saveNewEntry(person_list, list_for_age_avg, person_dic, num_of_people):
    while True:
        user_id = input("Enter Id Number ")
        user_age = input("Enter User Age ")
        if user_id.isdigit() and user_age.isdigit():
            user_id = int(user_id)
            user_age = int(user_age)
            break
        else:
            print("Something Wrong, Id and Age Should Be a Numbers Try Again ")
    user_name = input("Enter User Name ")
    employee_or_student = input("you are employee or student : ")
    if employee_or_student == "student":
        per = Student(user_name, user_age, user_id)
        per.inputFromUser()
        person_list.append(per)
    elif employee_or_student == "employee":
        per = Employe(user_name, user_age, user_id)
        per.inputFromUser()
        person_list.append(per)
    else:
        per = Person(user_name, user_age, user_id)
        person_list.append(per)
    print("ID [" + str(per.getId()) + "] Added Successfully")
    list_for_age_avg[0] = list_for_age_avg[0] + user_age
    person_dic[user_id] = num_of_people
    num_of_people += 1
    return num_of_people


def searchById(user_list, user_dic):
    chosen_id = input("Which Id You Looking For : ")
    if chosen_id.isdigit() and int(chosen_id) in user_dic:
        return functhatPrintPerson(user_list, user_dic[int(chosen_id)])
    print("Id Not Found")


def printAgesAverage(list_for_calc_avg, person_list):
    if len(person_list) == 0:
        return print("There Is No Person to Calculate Age Average")
    avg = list_for_calc_avg[0] / len(person_list)
    print("The Average of ALL Ages : is " + str(avg))


def printAllNames(user_list):
    print("The names Are : ")
    for person in user_list:
        print(person.getName())
        print("")


def printAllId(user_list):
    print("The IDs Are : ")
    for person in user_list:
        print(person.getId())


def exitFunction():
    while True:
        yes_no = input("Are you Sure Want to Exit? y/n ")
        if yes_no == "y":
            return False
        elif yes_no == "n":
            return True
        else:
            print("You Can Choose just y/n")


def printAllEntry(user_list):
    for person in user_list:
        person.printMySelf()


def findPersonByLocation(list_of_person):
    chosen_index = input("Please What Index you looking for ")
    try:
        chosen_index = int(chosen_index)
        functhatPrintPerson(list_of_person, chosen_index)
    except:
        print("Index Not Found")


# Start From Here Main
people_list_all = []
people_dict_all = {}
number_of_people = 0
list_for_avg_calc = [0]
check_loop = True
while check_loop:
    mainScreen()
    user_choice = input("Please Enter Your Choice: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            number_of_people = saveNewEntry(people_list_all, list_for_avg_calc, people_dict_all, number_of_people)
        elif user_choice == 2:
            searchById(people_list_all, people_dict_all)
        elif user_choice == 3:
            printAgesAverage(list_for_avg_calc, people_list_all)
        elif user_choice == 4:
            printAllNames(people_list_all)
        elif user_choice == 5:
            printAllId(people_list_all)
        elif user_choice == 6:
            printAllEntry(people_list_all)
        elif user_choice == 7:
            findPersonByLocation(people_list_all)
        elif user_choice == 8:
            saveAllDatatoFile(people_list_all)
        elif user_choice == 9:
            check_loop = exitFunction()
    else:
        input("The [" + user_choice + "] Dosnt Exist PRESS ENTER tO Chose Another One")
    input("Press Enter to Continue")
print("GoodBye")
