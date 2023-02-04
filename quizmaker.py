print("Welcome to your Quiz! ")
userFirstName = input("Enter your first name. ")
userLastName = input("Enter your last name. ")
studentID = input("Input your ID, starts with the letter “A” and then 5 numbers: ")
validID = True
while validID == True:
    if len.studentID < 7 and studentID.index(0) == 'A':
        validID = True;
    else:
        validID = False;
    
