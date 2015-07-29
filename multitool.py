import os, sys, glob, math, random, login, gfx, config, functions, time

functions.load_sequence_complete()

functions.username_login()
time.sleep(0.05)
functions.password_login()
print ("\n[credentials have been verified! proceeding to main program " + "-".join(gfx.load_sequence) + "]\n")
time.sleep(0.1)

program = True
while (program == True):
    user_input = functions.choice_selecter()
    functions.validate_choice(user_input)
