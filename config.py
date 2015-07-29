import os, sys, glob, math, random, login, gfx, functions, time

version_number = ("1.3.0") #version number of the program
"""
version history -----
1.0.0: the program basics are written and files are created
1.1.0: login and help is implemented
1.2.0 pre-release: a buggy version with a calculator and other bug fixes for previous releases
1.2.1: the calculator is fixed and one more function is added. Other bugs have been fixed as well
1.2.3: the calculator is fixed further and one more function is added. Other bugs have been fixed as well
1.3.0 pre-release: a dictionary is being implemented
1.3.0: a dictionary/define function is implemented with a few graphical glitches only when long definitions are displayed.

"""

default_path = "/Users/DarkLeviathan/GitHub/Multitool/" #creates path to folder (can be changed by commenting this line out and creating new one)
default_dirs = os.listdir( default_path )
ans = ("0.0") #edit this value (keep .0) to see what the prev_output in the calculator is
valid_cal_chars = ("0123456789-+/*ansqrt() \n") #edit this to change the accepted characters for calculation
valid_choices = ("help", "calculator", "end", "define") #edit this to change/add validated choices
description_help = ("[HELP] - You are currently in the help function, which is used to learn more about functions within this program. It can also contain future planned updates from time to time.") #edit this to change the message shown when user asks for description of help
description_cal = ("[CALCULATOR] - The calcuator is buit directly in so you do not have to call it with the 'calculator' command. You can simply enter (ex): 1*1 to start calculating.") #edit this to change the message shown when user asks for description of calculator
description_end = ("[END] - This command can be used to end the program when it prompts you for the next request.") #edit this to change the message shown when user asks for description of the end command
description_define = ("[DEFINE] - This command requires a second word after it so it can search the definition up and dis play it.")
