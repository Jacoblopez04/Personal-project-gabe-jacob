start_key2 = input("Would you like to make an account?(yes or no)\n")
if start_key2 != "yes":
    quit("Thank you for your time.")

if start_key2 == "yes":
    pass

start_key1 = True

username = input("Please enter the username you would like.\n")

temp_pass = input("Please enter the password you would like.\n")

while start_key1 == True:
    temp_pass2 = input("Please re-enter your password.\n")
    if temp_pass2 != temp_pass:
        print('The passwords do not match.')
        continue
    
    if temp_pass2 == temp_pass:
        password1 = temp_pass2
        break

login_data = {"username": username, "password": password1}
login_p1 = input("Your account has been successfully created.\nWould you like to log in right now?(yes or no)\n")
if login_p1 != "yes":
    quit("Thank you for your time.")
else:
    pass

login_ready = True

login_valid = False

while login_ready == True:
    login_p2 = input("Please enter your username.\n")

    login_p3 = input("Please enter your password.\n")
    if login_p3 != password1:
        print("The username or password is incorrect. Please log in with valid details.\n")
        continue
    
    if login_p2 == username and login_p3 == password1:
        login_valid== True
        break
quit

