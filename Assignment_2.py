#Simple ATM System
def choice():   #Menu Selection
    opt = int(input("\nEnter your Choice: \n 1. Sign In (If you are an existing user) \n 2. Forgot Password (If you are an existing user) \n 3. Sign Up (If you are a new user) \n 4. Exit (If you don't want to continue) \n"))
    if (opt == 1): Sign_In()
    elif (opt == 2): Forgot_Password()
    elif (opt == 3): Sign_Up() 
    elif (opt not in (1,2,3,4)):
        print("Invalid Choice. Please select currect choice!\n")
        choice()
    elif (opt == 4): exit

data = {'uname':['abcd','efgh','ijkl'],
        'name':['ABCD','EFGH','IJKL'],
        'age':[26,25,25],
        'email':['abcd@gmail.com','efgh@gmail.com','ijkl@gmail.com'],
        'password':['qwertyuiop','asdfghjkl','zxcvbnm'],
        'amount':[50000,40000,35000]} 

cred = {'usr':['abcd','efgh','ijkl'],
        'pwd':['qwertyuiop','asdfghjkl','zxcvbnm'],
        'pin':[1111,2222,3333]}

def Sign_In():  #existing User Sign In
    uname = input("\nEnter your username: ")
    pwd = input("\nEnter your password: ")
    if uname in cred['usr'] and pwd in cred['pwd']:
        print("You have Successfully Logged in!")
        print("\nWelcome ", uname)
        transaction(uname)
    elif (uname not in cred['usr'] and pwd in cred['pwd']) or (uname in cred['usr'] and pwd not in cred['pwd']):
        print("\nInvalid Credentials..Please login again!!\n ")
        choice()
    elif uname not in cred['usr'] and pwd not in cred['pwd']:
        print("\nUser not found...Create new account!!\n ")
        choice() 

def Sign_Up():  #New User Sign Up 
    uname = input("\nEnter your username: ")
    data['uname'].append(uname)
    cred['usr'].append(uname)
    name = input("\nEnter your name: ") 
    data['name'].append(name)
    age = int(input("\nEnter your age: "))
    data['age'].append(age)
    email = input("\nEnter your email id: ") 
    data['email'].append(email)
    password = input("\nEnter your password: ")
    data['password'].append(password)
    cred['pwd'].append(password)
    pin = int(input("\nEnter pin for your account:  "))
    cred['pin'].append(pin)
    amount = (float(input("\nEnter the amount in your account: ")))
    data['amount'].append(amount)
    print("Congrats, you have successfully created your account!!")
    
def transaction(uname):   #After Sign In options for user 
    opt = int(input("\nEnter your Choice: \n 1. Check your Balance \n 2. Deposit Amount \n 3. Withdrawl Amount\n 4. Change Password\n 5. Change PIN\n 6. Logout\n"))
    if (opt == 1):
        for i in range(len(data['uname'])):
            if data['uname'][i] == uname:
                bal = data['amount'][i]
                print("Total Amount in your account is ", bal)
                transaction(uname)

    elif (opt == 2):
        dep = int(input("\nEnter amount to deposit in your account "))
        print("\nAmount is successfully credited in your account!!")
        for i in range(len(data['uname'])):
            if data['uname'][i] == uname:
                data['amount'][i] += dep
                data['d_trans'][i].append(dep)
                print("Updated balance in your account is ", data['amount'][i])
                transaction(uname)

    elif (opt == 3):
        w_draw = (int(input("\nEnter amount to withdraw ")))
        for i in range(len(data['uname'])):
            if data['uname'][i] == uname:
                if data['amount'][i] > w_draw:
                    data['amount'][i]-= w_draw
                    print("\nCollect your cash ",w_draw)
                    data['w_trans'][i].append(w_draw)
                    print("\nUpdated balance in your account is ",data['amount'][i]) 
                    transaction(uname)
                else:
                    print("\nSorry!! No amount in your account")
                    transaction(uname)

    elif (opt == 4): Password_Change(uname)

    elif (opt == 5): PIN_Change(uname)

    elif (opt == 6): 
        print("Logged out Successfully!!")
        exit
        
    elif (opt not in range(1,7)):
        print("Invalid Choice. Please select correct choice!\n")
        transaction(uname)

def Forgot_Password():   #Forgot Password option before Sign In
    email = input("\nPlease enter your email id for confirmation ")
    for i in range(len(data['email'])):
        if data['email'][i] == email:
            new_pswd = input("\nEnter new password ")
            new_pswd1 = input("\nPlease confirm the password ")
            if new_pswd == new_pswd1:
                data['password'][i] = new_pswd
                del new_pswd1
                print("\nPassword is Successfully Changed. Please login with your new password!!")
                print("\nYour new password is ",data['password'][i])
                choice()
            else: 
                print("\nPassword doesn't match. Please try again!!")
                Forgot_Password()
        else :
            continue
            Forgot_Password()

def Password_Change(uname):   #Password Change option after user Sign In
    for i in range(len(data['uname'])):
        if data['uname'][i] == uname:
            new_pswd = input("\nEnter new password ")
            new_pswd1 = input("\nPlease confirm the password ")
            if new_pswd == new_pswd1:
                data['password'][i] = new_pswd
                del new_pswd1
                print("\nPassword is Successfully Changed!!")
                print("\nYour new password is ",data['password'][i])
                transaction(uname)
            else: 
                print("\nPassword doesn't match. Please try again!!")
                Password_Change()
        else :
            continue
            Password_Change()

def PIN_Change(uname):  #PIN Change option after user Sign In
    for i in range(len(data['uname'])):
        if data['uname'][i] == uname:
            new_pin = input("\nEnter new pin ")
            new_pin1 = input("\nPlease confirm the pin ")
            if new_pin == new_pin1:
                cred['pin'][i] = new_pin
                del new_pin1
                print("\nPin is Successfully Changed!!")
                print("\nYour new Pin  is ",cred['pin'][i])
                transaction(uname)
            else: 
                print("\nPassword doesn't match. Please try again!!")
                PIN_Change()
        else :
            continue
            PIN_Change()

choice()
 



    

