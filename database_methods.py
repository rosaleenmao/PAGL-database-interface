

# ensures arguments are passed in correctly
# returns string that represents that the main method should do
def check_arguments(argv):
    n = len(argv)

    # meets conditions to display help message
    if n == 2 and ((argv[1] == "help") or (argv[1] == "-h") or (argv[1] == "-help")):
        return "help"

    # check if user wants to show all modules
    elif n == 2 and ((argv[1] == "show_all") or (argv[1] == "-sa")):
        return "show all"

    # not help message and doesn't have right number of arguments
    if n != 3:
        exit("Incorrect number of inputs : %d. "
             "First include what you want to use, then the file or title your module" % (n - 1))

    # check if user wants to add module
    if (argv[1] == "add_module") or (argv[1] == "-am"):
        check_csv(argv[2])
        return "add module"

    # check if user wants to add data
    elif (argv[1] == "add_data") or (argv[1] == "-ad"):
        check_csv(argv[2])
        return "add data"

    # check if user wants to remove module
    elif (argv[1] == "remove_module") or (argv[1] == "-rm"):
        return "remove module"

    # check if user wants to remove data
    elif (argv[1] == "remove_data") or (argv[1] == "-rd"):
        return "remove data"

    # check if user wants to show a specific module
    elif (argv[1] == "show_module") or (argv[1] == "-sm"):
        return "show module"

    # at this point, we know the user hasn't entered a valid command
    else:
        exit("You did not give a valid action. "
             "If you want to see the possible commands, try this command : $ %s help" % argv[0])


# ensures that argument is csv
def check_csv(csv_file):
    if csv_file[-4:] != ".csv":
        exit("To add data or a module, you have to pass in a csv file.")


# prints help message in console
# TODO
def help_message():
    print("dog")


# ensures that csv fields are formatted correctly
# TODO
def check_fields(cat):
    print()


# insert a new module into the database
# TODO
def insert_module(cat):
    print(cat)


# remove a module from the database
# TODO
def remove(cat):
    print(cat)


# insert new data into an existing module in the database
# TODO
def insert_module_data(cat):
    print(cat)


# remove data from an existing module in the database
# TODO
def remove_module_data(cat):
    print(cat)


# show what is stored in an existing module in the database
# TODO
def show_module(cat):
    print(cat)
