login1 = input('Login >>> ')
password1 = input('Password >>> ')
password_check1 = input('Put password again >>> ')
requierement1 = login1.isalpha() == True
requierement2 = password1.isalnum() == True
if requierement1 == True and requierement1 == True:
    if password1 == password_check1:
        print('Login accepted')
        print('You have been un-logined by teacher, please login again')
        login2 = input('Login >>> ')
        password2 = input('Password >>> ')
        password_check2 = input('Put password again >>> ')
        if login2.isalpha() == True and password2.isalnum() == True:
            requierement3 = login1 == login2
            requierement4 = password1 == password2
            if requierement3 == True and requierement4 == True:
                if password2 == password_check2:
                    print('Youre logged-in')
                else:
                    print('Your passwords arent equal')
            else:
                print('Your data isnt correct, try again')
        else:
            print('Your data isnt correct, try again')
    else:
        print('Try again, passwords arent equal')
else:
    print('Your data isnt correct, try again')
