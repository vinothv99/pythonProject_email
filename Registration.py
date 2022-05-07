import re

def register():
    db = open("file.txt", "r")
    email = input("Create the email address:")
    create_password = input("Create the password:")
    confirm_password = input("Confirm the password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if re.search('^[a-z 0-9]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}',email):
        pass
    else:
        print("email endered is in valid")
        register()
    if create_password != confirm_password:
        print("Password is not same as confirm password")
    elif len(create_password) < 5:
        print("Password too short")
        register()
    elif email in d:
        print("Email already taken")
        register()
    elif len(create_password) <= 16:
        flag = 0
        if not re.search('[a-z]', create_password):
            flag = 1
            print("password doesnot contain Lowercase")
            register()
        elif not re.search('[A-Z]', create_password):
            flag = 1
            print("password doesnot contin Uppercase")
            register()
        elif not re.search('[0-9]', create_password):
            flag = 1
            print("password doesnot contain Numbers")
            register()
        elif (flag == 0):
            db = open("file.txt", "a")
            db.write(email+", "+create_password+"\n")
            print("email created successfully")

#register()

def login():
    db = open("file.txt", "r")
    email_login = input("Enter the created email id")
    Password_login = input("Enter the Password")
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    if email_login in d:
        if Password_login in f:
            print("Welcome", email_login)
        else:
            print("Password entered is incorrect")
            print("please login again")
            login()
    else:
        print("You have not yet registere")
        print("Register below")
        register()
#login()

def forgot():
    db = open("file.txt", "r")
    email_login = input("Enter the created email id")
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    if email_login in d:
        for j in range (len(f)):
            value = f[j]
        print(value)
    else:
        print("Email is incorrect")
        register()
#forgot()

def access():
    lt = ["1.Register","2.Login","3.Forgotpassword"]
    print(lt)
    v = int(input())
    for i in range(1,lt):




access()

