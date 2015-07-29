import os, sys, glob, math, random, login, gfx, config, time, urllib.request, re, requests
from math import sqrt
from lxml import html
from urllib.request import urlopen, HTTPError
from time import gmtime, strftime
from pprint import pprint
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
                print ("-".join(gfx.load_sequence) + " | valid username!")
                return True
            elif (inusername != login.username):
                print ("-".join(gfx.load_sequence) + " | invalid username!")
        except TypeError:
            print ("-".join(gfx.load_sequence) + " | invalid username!")

def password_login():
    while True:
        inpassword = input("enter password: ")
        try:
            inpassword = str(inpassword)
            if (inpassword == login.password):
                print ("-".join(gfx.load_sequence) + " | valid password!")
                return True
            elif (inpassword != login.password):
                print ("-".join(gfx.load_sequence) + " | invalid password!")
        except TypeError:
            print ("-".join(gfx.load_sequence) + " | invalid password!")

def choice_selecter():
    user_input = str(input(" >>> "))
    return user_input

def validate_choice(user_input):
    if (user_input in config.valid_choices):
        mainframe(user_input)
    elif (split_line_test(user_input) == True):
        mainframe(user_input)
    elif (any(c not in config.valid_cal_chars for c in user_input)):
        print ("'" + user_input + "'" + " is not a valid choice!")
    else:
        mainframe(user_input)

def mainframe(user_input):
    if (user_input == "end"):
        quit()
    elif (user_input == "help"):
        print ("0")
        choice_help()
    elif (user_define_input == "define"):
        define_word(user_define_input)
    elif (user_input == "time"):
        show_time()
    elif (split_line_test(user_input)):
        if (user_define_input[0] == "define"):
            define_word(user_define_input)
        if (user_define_input[0] == "weather"):
            show_weather(user_define_input)
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
    elif not any("ans" in user_input or c in user_input for c in "0123456789"):
        print("- Invalid Equation | No numbers found")
        return
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
        elif (user_input == "define"):
            print ("\n" + config.description_define + "\n")

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
    defs = '\n'.join(defs)
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
    print ("Normal temperature is: %.1f" % (celcius_norm_temp))
    print ("Highest temperature is: %.1f" % (celcius_max_temp))
    print ("Lowest temperature is: %.1f" % (celcius_min_temp))
    print ("\n")

def kelvin_celcius(temp):
    kelvin = float(273.15)
    temp = float(temp)
    output_temp = (temp - kelvin)
    return output_temp
