#For loop
for j in "python":
    if j == "o":
        break
        print(j)

#MULTIPLICATION PROGRAM  BY USING FOR LOOP
for i in range(1,21):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

#USERNAME AND PASSWORD AND VALIDATION
    print()
user = "vinay"
password ="vinay123"
user_name = input("enter user name:")
pass_word = input("Enter password:")
if user == user_name and password == pass_word:
    print("Success both are Matched.")
else :
        print("Password is incorrect! try again!")


