import os, sys, glob, math, random, login, gfx, config, time, urllib.request, re
from math import sqrt
from urllib.request import urlopen, HTTPError
re.compile('<title>(.*)</title>')

def load_sequence_complete():
    print ("loading " + "-".join(gfx.load_sequence) + " |100%")
    time.sleep(0.25)
    print ("loading complete " + "".join(gfx.load_sequence_bar) + " |done")
    time.sleep(0.05)
    print ("version: " + config.version_number)

def username_login():
    while True:
        inusername = input("enter username: ")
        try:
            inusername = str(inusername)
            if (inusername == login.username):
                print ("-".join(gfx.load_sequence) + " |valid username!")
                return True
            elif (inusername != login.username):
                print ("-".join(gfx.load_sequence) + " |invalid username!")
        except TypeError:
            print ("-".join(gfx.load_sequence) + " |invalid username!")

def password_login():
    while True:
        inpassword = input("enter password: ")
        try:
            inpassword = str(inpassword)
            if (inpassword == login.password):
                print ("-".join(gfx.load_sequence) + " |valid password!")
                return True
            elif (inpassword != login.password):
                print ("-".join(gfx.load_sequence) + " |invalid password!")
        except TypeError:
            print ("-".join(gfx.load_sequence) + " |invalid password!")

def choice_selecter():
    user_input = str(input(" >>> "))
    return user_input

def validate_choice(user_input):
    if (user_input in config.valid_choices):
        mainframe(user_input)
    elif (split_line_test(user_input) == True):
        mainframe(user_input)
    elif (any(c not in config.valid_cal_chars for c in user_input)):
        print (user_input + " is not a valid choice!")
    else:
        mainframe(user_input)

def mainframe(user_input):
    if (user_input == "end"):
        quit()
    elif (user_input == "help"):
        print ("0")
        choice_help()
    elif (split_line_test(user_input) == True):
        define_word(user_define_input)
    else:
        calculator(user_input)

def prev_ans():
    try:
        return config.prev_output
    except NameError:
        return 0

def calculator(user_input):
    global ans
    if any(c not in config.valid_cal_chars for c in user_input):
        print("- Invalid Equation | Bad characters")
        return
    """elif not any(c in user_input for c in "0123456789"):
        print("- Invalid Equation | No numbers found")
        return"""
    sys.stdout.write("calculating " + "-".join(gfx.load_sequence))
    time.sleep(0.3)
    print (" | 100%")
    try:
        ans = eval(user_input)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, ValueError):
        print ("- Invalid Equation | Error")
        return
    config.ans = ans
    print (ans)

def choice_help():
    print ("This program can currently do these things: %s" % (" - ".join(config.valid_choices)))
    while True:
        user_input = input(" Would you like to know more about these functions? Enter the choices listed above to proceed, no to cancel: ")
        if (user_input == "help"):
            print ("\n" + config.description_help + "\n")
        elif (user_input == "calculator"):
            print ("\n" + config.description_cal + "\n")
        elif (user_input == "end"):
            print ("\n" + config.description_end + "\n")

def define_word(user_define_input):
    srch = str(user_define_input[1])
    output_word=urllib.request.urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t")
    output_word=output_word.read()
    items=re.findall('<meta name="description" content="'+".*$",output_word,re.MULTILINE)
    for output_word in items:
        y=output_word.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation, synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                print ("Word not found!")
            else:
                print (z)
    else:
        print ("Word not found!")


def split_line_test(user_input):
    global user_define_input
    user_define_input = user_input.split()
    if (user_define_input[0] == "define"):
        return True
    return False