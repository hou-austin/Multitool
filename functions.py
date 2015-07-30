#---------- prerequisite code start
import os, sys, glob, math, random, gfx, config, time, urllib.request, re, requests, adminconsole_commands, encryption_standard
import math as mathlist
import encryption_standard as encrypt_s
from lxml import html
from urllib.request import urlopen, HTTPError
from time import gmtime, strftime
from pprint import pprint
math_list = dir(mathlist)
global activestate
activestate = False
re.compile('<title>(.*)</title>')
#---------- prerequisite code end

def load_sequence_complete():
    print ("loading " + "-".join(gfx.load_sequence) + " |100%")
    time.sleep(0.25)
    print ("loading complete " + "".join(gfx.load_sequence_bar) + " |done")
    time.sleep(0.05)
    print ("version: " + config.version_number)

def check_user_present():
    with open("login.txt", "r") as login:
        contents = login.read()
        if (contents == ""):
            return False
        else:
            return True

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        username = username.lower()
        password = password.encode("utf-8")
        if (encryption_standard.check_login(username, password)):
            print ("Welcome back %s!\n" % username)
            break
        else:
            print ("Invalid login as %s\n" % username)

def new_user_login(username, password):
    encryption_standard.new_user(username, password)

def choice_selecter(): #askes the user for input/command
    user_input = str(input(" >>> "))
    return user_input.lower()

def validate_choice(user_input):
    if (user_input == ""):
        return
    elif (user_input in config.valid_choices):
        mainframe(user_input)
    elif (split_line_test(user_input) == True):
        mainframe(user_input)
    elif not any([user_input in config.valid_cal_statements or c in config.valid_cal_chars for c in user_input]):
        print ("'" + user_input + "'" + " is not a valid choice!")
    else:
        calculator(user_input)

def mainframe(user_input): #links input to function
    if (user_input == "end"):
        quit()
    elif (user_input == "help"):
        choice_help()
    elif (split_line_test(user_input) == "define"):
        define_word(user_define_input)
    elif (user_input == "time"):
        show_time()
    elif (split_line_test(user_input)):
        if (user_define_input[0] == "define"):
            define_word(user_define_input)
        if (user_define_input[0] == "weather"):
            show_weather(user_define_input)
    elif (user_input == "adminconsole"): #activate adminconsole, looks for ADMINKEY first
        warning = input("\n[WARNING]: ADMINCONSOLE IS A COMMAND FOR DEBUGGING AN MAY CAUSE HARM TO YOUR COMPUTER, DO YOU WISH TO CONTINUE? ENTER [Y] TO CONTINUE, ENTER ANYTING TO CANCEL: ")
        if (warning == "y"):
            print("\n Proceeding -\n")
            if (import_encryption_admin() == True):
                password = input("Enter ADMINKEY: ")
                if (encryption_admin.admin_decrypt(password) == True):
                    print ("\n[ADMINCONSOLE] is now active\n")
                    activestate = True
                    active_adminconsole(activestate)
                else:
                    activestate = False
                    print ("\n[ADMINCONSOLE] activation has failed: Incorrect ADMINKEY\n")
    elif (user_input == "changelogin"):
        change_logincrentials()
    else:
        calculator(user_input)

"""def change_logincrentials(): #will be fixed so it will work with new encryption method
    while True:
        check_username = input("Enter current username: ")
        check_password = input("Enter current password: ")
        while True:
            if (encrypt_s.standard_decrypt_username(check_username)):
                if (encrypt_s.standard_decrypt_password(check_password)):
                    new_username = input("Enter new username: ")
                    new_password = input("Enter new password: ")
                    if (new_username == new_password):
                        print ("Cannot set them as the same!")
                        continue
                    with open("encryption_standard.py", "r") as file_in:
                        old_username = (encrypt_s.standard_change(check_username)).decode("utf-8")
                        old_password = (encrypt_s.standard_change(check_password)).decode("utf-8")
                        contents = file_in.read()
                        contents = contents.replace(old_username, encrypt_s.standard_change(new_username).decode("utf-8"))
                        contents = contents.replace(old_password, encrypt_s.standard_change(new_password).decode("utf-8"))
                        with open("encryption_standard.py", "w") as file_out:
                            file_out.write(contents)
                        print ("Username and password has been changed!")
                        break
        else:
            print ("Invalid username or password was entered! Try again -\n")
            continue
        break
"""

def import_encryption_admin(): #tries to look for encryption_admin file to import
    try:
        global encryption_admin
        import encryption_admin
        return True
    except ImportError:
        print ("\nThe required files are not present on your device, operation cancled -\n")
        return False

def find_illegal(user_input): #if there is a illegal command in calculator input, return False
    #a = re.sub(r'\([^)]*\)', '', user_input) #deletes quotations and everything inside them
    for illegal_string in config.illegal_statements:
        if (illegal_string in user_input):
            return False
    return True

def calculator(user_input):
    user_input_test = find_illegal(user_input)
    if (user_input_test == False):
        print("Illegal statement -")
        return
    sys.stdout.write("calculating " + "-".join(gfx.load_sequence))
    time.sleep(0.3)
    print (" | 100%")
    try:
        user_input = str(cal_input_replace(user_input))
        config.cal_ans = eval(str(user_input))
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, ValueError):
        print ("- Invalid Equation | Error")
        return
    print (config.cal_ans)

def cal_input_replace(user_input): #replaces math function with math.function
    for item in math_list:
        if (item == "e" or item == "pi"): #constants are special exception
            continue
        elif (item in user_input):
            new_item = ("math." + item)
            user_input = user_input.replace(item, new_item)
    print (user_input)

    return user_input.replace("~pi", "math.pi").replace("~e", "math.e").replace("ans", str(config.cal_ans)) #replaces ~constants with math.constants

def choice_help():
    print ("\nThis program can currently do these things: %s" % (" - ".join(config.valid_choices)))
    while True:
        user_input = input("\nWould you like to know more about these functions? Enter the choices listed above to proceed, enter [NO] to cancel: ")
        user_input = user_input.lower()
        if (user_input == "help"):
            print ("\n" + config.description_help + "\n")
        elif (user_input == "calculator"):
            print ("\n" + config.description_cal + "\n")
        elif (user_input == "end"):
            print ("\n" + config.description_end + "\n")
        elif (user_input == "define"):
            print ("\n" + config.description_define + "\n")
        elif (user_input == "time"):
            print ("\n" + config.description_time + "\n")
        elif (user_input == "adminconsole"):
            print ("\n" + config.description_adminconsole + "\n")
        elif (user_input == "no"):
            return
        else:
            print ("Please print something in the list above -\n")

def define_word(user_define_input):
    try:
        response = requests.get("http://dictionary.reference.com/browse/{}?s=t".format(user_define_input[1]))
    except IndexError:
        print("You have not entered a word!")
        return
    tree = html.fromstring(response.text)
    title = tree.xpath('//title/text()')
    print(title)
    print("\n")
    defs = tree.xpath('//div[@class="def-content"]/text()')
    defs = ''.join(defs)
    defs = defs.replace("() ", "")
    defs = defs.split('\n')
    defs = [d for d in defs if d]
    for d in defs:
        print(d)

def split_line_test(user_input):
    global user_define_input
    user_define_input = user_input.split()
    if (user_define_input[0] == "define"):
        return True
    if (user_define_input[0] == "weather"):
        return True
    return False

def show_time():
    print(time.ctime())# 'Mon Oct 18 13:35:29 2010'
    print(time.strftime('%l:%M%p %Z on %b %d, %Y')) # ' 1:36PM EDT on Oct 18, 2010'
    print(time.strftime('%l:%M%p %z on %b %d, %Y')) # ' 1:36PM EST on Oct 18, 2010'

def show_weather(user_define_input):
    print ("Retrieving Weather data | " + "-".join(gfx.load_sequence))
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + (user_define_input[1]))
    requested_data = r.json()
    print ("Data retrieved \n")
    kelvin_norm_temp = requested_data ["main"]["temp"]
    kelvin_max_temp = requested_data ["main"]["temp_max"]
    kelvin_min_temp = requested_data ["main"]["temp_min"]
    celcius_norm_temp = str(kelvin_celcius(kelvin_norm_temp))
    celcius_max_temp = str(kelvin_celcius(kelvin_max_temp))
    celcius_min_temp = str(kelvin_celcius(kelvin_min_temp))
    print ("Normal temperature is: %.1f" % float(celcius_norm_temp))
    print ("Highest temperature is: %.1f" % float(celcius_max_temp))
    print ("Lowest temperature is: %.1f" % float(celcius_min_temp))
    print ("\n")

def kelvin_celcius(temp):
    kelvin = float(273.15)
    temp = float(temp)
    output_temp = (temp - kelvin)
    return output_temp

def active_adminconsole(activestate):
    while activestate == True:
        command = input(">>> ")
        if (command == "adminconsole.exit()"):
            adminconsole_commands.exit()
            return
        try:
            after_exec = exec(command)
        except:
            print ("[ADMINCONSOLE]: ", sys.exc_info()[0])
