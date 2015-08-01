#---------- prerequisite code start
#---------- prerequisite code end

def exit():
    print ("\n[ADMINCONSOLE]: Exiting -\n")
    return False

def test():
    print ("\n[ADMINCONSOLE]: True -\n")

def run_function(module):
    try:
        function = module
        module = module.split(".")
        if (module[0] != "adminconsole_commands"):
            import_module = module[0]
            import_module = str("import "+ import_module)
            print (import_module)
            exec ("%s" % import_module)
            print (function)
            exec (function)
        else:
            function = module[1]
            exec (function)
    except:
        print ("[ADMINCONSOLE]: Invalid module or function was entered - ")
