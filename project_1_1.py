import time

name = input ("Please Enter Your Name ")
print ("Hi "+ name +" Please Choose 2 Number ")
str_number_1 = input("First Number ")
str_number_2 = input("Second Number ")
print("Than You For Choosing Two Numbers The First "+ str_number_1 +" The Second is " +str_number_2)
int_number_1 = int (str_number_1)
int_number_2 = int (str_number_2)
if (int_number_1%2==0):
    print("The First Number is Even ")
else:
    print("The First Number is Odd ")
if (int_number_2%2==0):
    print("The Second Number is Even ")
else:
    print("The Second Number is Odd ")    

if (int_number_1%2==0 and int_number_2%2==0):
    print("Both Numbers Are Even") 
else : 
    print("One is Even , And one Is Odd")
operator = input("Choose Operator(* , - , / , +)") 
if (operator=="+"):
    result = int_number_1+int_number_2
elif(operator=="-"):
     result = int_number_1-int_number_2   
elif(operator=="*"):
     result = int_number_1*int_number_2     
elif(operator=="/"):
    if(int_number_2!=0):
        int_or_float = input(" You Choose / , would you like The Result as integer  y/n ? ")
        if (int_or_float=="y"):
         result =  int_number_1/int_number_2 
         result=int(result)
        else:
         result = float(int_number_1)/float(int_number_2)
    else:
        print("You Cant Devide By 0")     
else:
    print("The oparator cand recognize chose another one ")

if(int_number_2!=0 and (operator=="+" or operator=="*" or operator=="-" or operator=="/")):
   print(str_number_1 + operator + str_number_2 + " = " + str(result))
   print("Thank You "+ name + " . " + time.ctime())  
else:
    print("Thank You "+ name + " . " + time.ctime())   
