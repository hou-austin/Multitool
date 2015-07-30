#---------- prerequisite code start
import os, sys, glob, math, random, gfx, config, functions, time, requests, adminconsole_commands, urllib.request,re
#---------- prerequisite code end

functions.load_sequence_complete()
if (functions.check_user_present()==True):
    functions.login()
elif (functions.check_user_present()==False):
    print ("\nWelcome to Multitool! Because this program has not been setup yet, no credentials have been stored (don't worry, the credentials are safely encrypted!). So please follow the instructions below to setup Multitool.\n")
    while True:
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        username = username.lower()
        password = password.encode("utf-8")
        if (" " in username):
            print ("\nInvalid username chosen - username cannot contain spaces!\n")
            continue
        functions.new_user_login(username, password)
        print("\nWelcome %s to Multitool, a program developed to give users the ability do many things. Because this is open-sourced, the community can contribute to it and add more functions. To begin, type: 'help'" %username)
        break
time.sleep(0.1)

print ("Enter your command after ' >>> '. Type 'help' if you need assistance.\n")

program = True
while (program == True):
    user_input = functions.choice_selecter()
    functions.validate_choice(user_input)
