import os
import pandas as pd
import json
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
            people_list.append({loaded_file["name"]: person.getName(),
                                loaded_file["id"]: person.getId(),
                                loaded_file["age"]: person.getAge()})
        output_file_name = input("What is Your Output File Name ? ")
        list_of_persons_df = pd.DataFrame(people_list)
        list_of_persons_df.to_csv(my_path + "//" + output_file_name, index=False)
        print("Saved Successfully ")
    except FileNotFoundError:
        print("The File conf.json in Not Exist in : " + my_path)


def functhatPrintPerson(person_list, index):
    print("ID : " + str(person_list[index].getId()))
    print("Name : " + person_list[index].getName())
    print("Age : " + str(person_list[index].getAge()))


def saveNewEntry(person_list, list_for_age_avg):
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
        year_of_study = input("what year you are: ")
        avg_score = input("what is your average : ")
        per = Student(user_name, user_age, user_id, year_of_study, avg_score)
        person_list.append(per)
    elif employee_or_student == "employee":
        field_of_work = input("what is your work: ")
        salary = input("what is your salary : ")
        per = Employe(user_name, user_age, user_id, field_of_work, salary)
        person_list.append(per)
    else:
        per = Person(user_name, user_age, user_id)
        person_list.append(per)
    print("ID [" + str(per.getId()) + "] Added Successfully")
    list_for_age_avg[0] = list_for_age_avg[0] + user_age


def searchById(user_list):
    chosen_id = input("Which Id You Looking For : ")
    if chosen_id.isdigit():
        chosen_id = int(chosen_id)
        for i, person in enumerate(user_list):
            if chosen_id == person.getId():
                return functhatPrintPerson(user_list, i)
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


#Start From Here Main
people_list_all = []
list_for_avg_calc = [0]
check_loop = True
while check_loop:
    mainScreen()
    user_choice = input("Please Enter Your Choice: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            saveNewEntry(people_list_all, list_for_avg_calc)
        elif user_choice == 2:
            searchById(people_list_all)
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
