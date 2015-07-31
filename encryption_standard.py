#---------- prerequisite code start
import sys, hashlib, unicodedata, random
users = {}
#---------- prerequisite code end

def check_login(username, password):
    with open("login.txt", "r") as login:
        contents = login.read()
        lines = contents.split("\n")
        for line in lines:
            info = line.split(" ")
            if len(info) <3:
                continue
            details = {}
            details["hash"] = info[1]
            details["salt"] = info[2]
            users[info[0]] = details
    if (username in users):
        hasher = hashlib.sha512()
        salt = users[username]["salt"]
        hash_password = users[username]["hash"]
        hasher.update(password)
        salt = salt.encode("utf-8")
        hasher.update(salt)
        input_password = repr(hasher.digest())
        input_password = input_password[2:][:-1]
        if (hash_password == input_password):
            return True
        return False

def salt_hash():
    salt = str(random.randint(0, 10000))
    return salt.encode("utf-8")

def new_user(username, password):
    with open("login.txt", "a") as login:
        login.write(username + " ")
        hasher = hashlib.sha512()
        salt = (salt_hash())
        hasher.update(password)
        hasher.update(salt)
        input_password = repr(hasher.digest())
        salt = salt.decode("utf-8")
        input_password = input_password[2:][:-1]
        login.write(input_password + " " + salt + "\n")
        print ("New user %s was created!" % username)

def check_user_exist(username, password):
    with open("login.txt", "r") as login:
        contents = login.read()
        lines = contents.split("\n")
        for line in lines:
            info = line.split(" ")
            if len(info) <3:
                continue
            details = {}
            details["hash"] = info[1]
            details["salt"] =info[2]
            users[info[0]] = details
        if (username in users):
            hasher = hashlib.sha512()
            salt = users [username]["salt"]
            salt = salt.encode("utf-8")
            password = password.encode("utf-8")
            hasher.update(password)
            hasher.update(salt)
            hash_p = repr(hasher.digest())
            hash_p = hash_p[2:][:-1]
            if (hash_p == users[username]["hash"]):
                return True
            else:
                return False
        else:
            return False

def change_credentials(new_username, new_password, old_username, old_password):
    with open("login.txt", "r") as login:
        contents = login.read()
        lines = contents.split("\n")
        for line in lines: #assigns users dictionary
            info = line.split(" ")
            if len(info) <3:
                continue
            details = {}
            details["hash"] = info[1]
            details["salt"] =info[2]
            users[info[0]] = details
        new_password = new_password.encode("utf-8")
        del users[old_username] #old username is no longer in users
        hasher = hashlib.sha512()
        salt = salt_hash()
        hasher.update(new_password)
        hasher.update(salt)
        hasher_p = repr(hasher.digest())
        hasher_p = hasher_p[2:][:-1]
        details = {}
        details["hash"] = hasher_p
        details["salt"] = salt
        users[new_username] = details
        with open("login.txt", "w") as login2:
            for user in users:
                new_hashs = users[user]["salt"].decode("utf-8")
                contents = user + " " + users[user]["hash"] + " " + new_hashs + "\n"
                login2.write(contents)
