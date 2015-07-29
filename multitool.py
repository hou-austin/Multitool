import os, sys, glob, math, random, login, gfx, config, functions, time

path = "/Users/DarkLeviathan/GitHub/Multitool/" #creates path to folder (can be changed by commenting this line out and creating new one)
dirs = os.listdir( path )

functions.load_sequence_complete()

functions.username_login()
functions.password_login()
functions.verify_credentials()
