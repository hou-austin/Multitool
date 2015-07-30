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
        login.write(input_password + " " + salt + "\n")
        print ("New user %s was created!" % username)

#encode input to utf-8
