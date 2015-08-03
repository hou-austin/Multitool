#---------- prerequisite code start
import os
#---------- prerequisite code end

version_number = ("Alpha 1.7.6 pre-release") #version number of the program
"""
version history -----
Alpha 1.0.0: the program basics are written and files are created
Alpha 1.1.0: login and help is implemented
Alpha 1.2.0 pre-release: a buggy version with a calculator and other bug fixes for previous releases
Alpha 1.2.1: the calculator is fixed and one more function is added. Other bugs have been fixed as well
Alpha 1.2.3: the calculator is fixed further and one more function is added. Other bugs have been fixed as well
Alpha 1.3.0 pre-release: a dictionary is being implemented
Alpha 1.3.0: a dictionary/define function is implemented with a few graphical glitches only when long definitions are displayed.
Alpha 1.3.6 pre-release: implementing time and weather function
Alpha 1.3.6: two functions were added: time and weather. A major security flaw in the calculator function is patched
Alpha 1.4.0 pre-release: the calculator function will be changed where mathematical constants can be used without compromising security.
Alpha 1.4.0: the calculator function is changed where mathematical constants and other equations/expressions can be used without compromising security.
Alpha 1.5.0 pre-release: an admin password is added while an admin console is being implemented.
Alpha 1.5.0: an adminconsole with custom functions in addition to regular python commands is added although it requires a local ADMINKEY decryption file and the ADMINKEY in order to be accessed.
Alpha 1.6.0 pre-release: a huge security overhaul to the login system will be implemented
Alpha 1.6.0: a huge security overhaul to the login system is added alo-ng with a "tutorial" system upon first launch
Alpha 1.6.2: bug fixes for the new login system. password inputs are now blanked out and valid inputs list has been fixed
Alpha 1.6.4 pre-release: bug fixes in adminconsole and help and more custom functions made for debugging are added to adminconsole
Alpha 1.6.4: bug fixes in adminconsole and help and more custom functions made for debugging are added to adminconsole
Alpha 1.7.0 pre_release: adding password changing and creating a new user function
Alpha 1.7.0: added user credential chaning and create new user functions
Alpha 1.7.3 pre_release: attempting to fix bug in adminconsole.run_function with delete user and encrypt/decrypt files function in the works
Alpha 1.7.3: Bug is not fixed (cannot pass stings in adminconsole.run_function). Delete user is not added but encyrptfile and decryptfile functions are added. Help function is cleaned up to look nicer.
Alpha 1.7.6 pre_release: Adding news function to the program.

"""

#default_path = "/foo*" #creates path to default folder (can be changed by replacing foo* and uncommenting this line and the one below it)
#default_dirs = os.listdir(default_path) #uncomment this line if you wish to add a directory
cal_ans = 0 #edit this value (keep .0) to see what the prev_output in the calculator is
valid_cal_chars = ("~0123456789-+/*()\n") #edit this to change the accepted characters for calculation
valid_cal_commands = ("ans")
valid_choices = ("help", "calculator", "end", "define", "time", "weather", "adminconsole", "changelogin", "newlogin", "clearscreen", "encryptfile", "decryptfile", "news") #edit this to change/add validated choices
illegal_statements = ["quit", "os.", "sys.", "shutil.", "import", "path", "dir", "builtins", "_", "{", "}", "lambda"] #edit this to change/add invalid statements in the calculator program
description_help = ("[HELP] - You are currently in the help function, which is used to learn more about functions within this program. It can also contain future planned updates from time to time.") #edit this to change the message shown when user asks for description of help
description_cal = ("[CALCULATOR] - The calcuator is buit directly in so you do not have to call it with the 'calculator' command. You can simply enter (ex): 1*1 to start calculating. A '~' must be used in front of a constant to work, ie: ~pi, ~e") #edit this to change the message shown when user asks for description of calculator
description_end = ("[END] - This command can be used to end the program when it prompts you for the next request.") #edit this to change the message shown when user asks for description of the end command
description_define = ("[DEFINE] - This command requires a second word after it so it can search the definition up and display it.") #displays the description for the define function
description_time = ("[TIME] - This command displays time in this format: 12:00AM PST on July 29, 2015 ") #displays the description of the time function
description_weather = ("[WEATHER] - This command requires a second word (a city name with no spaces if its is a multi-word city name) after it. It will show the temperature of the city. More outputs will be added.") #displays the description of the weather function
description_adminconsole = ("[ADMINCONSOLE] - This command  requires a key file in the Multitool folder with the password to it. If the correct password is entered, the user will be able to use the python shell like how it can usually be used within the multitool program. It is made for debugging although it can be an extremely powerful tool with custom functions in addition to regular python commands.") #displays the description of the adminconsole function
description_changelogin = ("[CHANGELOGIN] - This command changes user credentials.") #displays the description of the change_logincrentials function
description_newlogin = ("[NEWLOGIN] - This command addes a new user.") #displays the description of the create_newuser function
description_clearscreen = ("[CLEARSCREEN] - This command clears the screen") #displays the description of the create_newuser function
description_encryptfile = ("[ENCRYPTFILE] - This command requires a filename (and extention) or the path to the file to work. It will encrypt the file, but it is not as secure as the password encryption method because this one is reversable.") #displays the description of the encryptfile function
description_decryptfile = ("[DECRYPTFILE] - This command requires a filename (and extention) or the path to the file to work. It will decyrpt the file.") #displays the description of the create_newuser function
