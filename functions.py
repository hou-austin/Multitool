import os, sys, glob, math, random, login, gfx, config, time

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
