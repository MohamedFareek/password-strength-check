def password_strength_check(password):
    def suggesion():
        print()
       
        print("Suggestions to improve your password:")

        if(having_upper==False):
            print("- Add uppercase letters (A-Z)")
        if(having_lower==False):
            print("- Add lowercase letters (a-z)")
        if(having_num==False):
            print("- Add numbers (0-9)")
        if(having_len==False):
            print("- Make it at least 8 characters long")
        if(having_special==False):
            print("- Add special characters (e.g., @, #, $, %)")
    count=0
    having_upper=False
    having_lower=False
    having_num=False
    having_special=False
    having_len=False

    special_char="!@#$%^&*()-_+="

    for i in password:
        if(i.isupper()):
            count+=1
            having_upper=True
            break
    for i in password:
        if(i.islower()):
            count+=1
            having_lower=True
            break
    for i in password:
        if(i.isdigit()):
            count+=1
            having_num=True
            break
    for char in special_char:
        if(char in password):
            count+=1
            having_special=True
    if(len(password)>7):
        count+=1
        having_len=True

    if(count>4):
        print("Its a Strong password")
    elif(count>=3):
        print("its a medium password")
        suggesion()
    else:
        print("its is a weak password")
        suggesion()
        

print("Wekcom to Passsword strength checker!")
password=input("Enter your password:")
password_strength_check(password)