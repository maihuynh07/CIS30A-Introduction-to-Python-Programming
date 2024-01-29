#customer info checking functions
def verify(str):
    if(str.isdigit()): print(str,'is','digits')
    elif (str.isalpha()): print(str,'is','alphabets')
    else: print(str,'is','not digits, not alphabets')
def checkName(name):
    if(name.isalpha()): print(name)
    else: input('Enter a valid name')
def checkAge(age)
    if(age.isdigit()): print(age)
    else: input('Enter a valid age:')
def checkPhone(phone)
    if(phone.isdigit()): print(phone)
    else: input('Enter a valid phone')
def checkMS(maritalStatus):
    if(maritalStatus.isalpha()): print(maritalStatus)
    else: input('Enter a valid maritalStatus:')
def storeInfo(name,age,phone,maritalStatus):
    try:
        file = open('customer_infor.txt','w')
        file.write(name:+'\n')
        file.write(age:+'\n')
        file.write(phone:+'\n')
        file.write(maritalStatus:+'\n')
    finally:
        print('Information stored')
        file.close()
def readInfo()
    try:
        file = open('customer_infor.txt','r')
        print(file.read())
    finally:
        file.close()