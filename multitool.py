import os, sys, glob, math, random, login, gfx, config, functions, time

functions.load_sequence_complete()

functions.username_login()
time.sleep(0.05)
functions.password_login()
print ("\n[credentials have been verified! proceeding to main program " + "-".join(gfx.load_sequence) + "]\n")
time.sleep(0.1)

print ("Welcome to Multitool! A program designed to be easily configurable and to use. This program allows the user to do many things both simple and complicated. If you ever need help, just type: 'help' after: ' >>> ' \n")

program = True
while (program == True):
    user_input = functions.choice_selecter()
    functions.validate_choice(user_input)
