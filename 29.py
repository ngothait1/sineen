#question 1
def addItem(my_list, item):
    my_list.append(item)
    return my_list
    
#question 2    
def listSortlowtoHigh(list):
    list.sort()
    return list
        
def listSortHighToLow(list):
    list.sort(reverse=True)
    return list

def printMaxnum(list):
    listSortHighToLow(list)
    return list[0]
    
def printMinnum(list):
    listSortlowtoHigh(list)
    return list[0]
    
def thebiggestNum(list):
    listSortHighToLow(list)
    new_list = list[:5]
    return new_list
    
#question 3

def sortStrlist(mystr):
    str_list = mystr.split("|")
    str_list.sort()
    return str_list
    
    
numlist = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70] 
print(printMinnum(numlist))
print(printMaxnum(numlist))
print(thebiggestNum(numlist))

my_str = "16|11|20|-2|9|19|7|5|10|5|20|-9|16|7|4|2|-5|2|-3|10"
print(sortStrlist(my_str))