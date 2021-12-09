#This program accepts first name and last name from user and formulates a login name for the user
import random
def main():
    first_name = input('Enter first name here: ')
    last_name = input('Enter last name here: ')

    like = "no"
    while like == "no":
        num = random.randint(1, 20)
        print("Your username is: ")
        #We convert our
        user_name = (str(first_name[ : num]) + str(last_name[num : ]) + str(num))
        print(user_name)
        print("Do want want this username?")
        like = input("Enter yes if you accept and no if you want a different user_name: ")

    print("Enter your password: ")

#Call the main function
main()

